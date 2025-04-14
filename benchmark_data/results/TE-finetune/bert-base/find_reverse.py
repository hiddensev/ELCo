import csv
from collections import defaultdict

# Read the CSV files
with_desc_data = defaultdict(list)
without_desc_data = defaultdict(list)

# Process with_desc.csv
with open('with_desc.csv', 'r') as f:
    current_section = ''
    for line in f:
        line = line.strip()
        # Check if this is a section header
        if line.startswith('***') and line.endswith('***'):
            current_section = line.strip('* \n')
            # Skip the header row
            next(f)
            continue
        if current_section and line:
            # Parse the CSV line
            parts = line.split(',')
            if parts and parts[0].isdigit():  # Make sure it's a data row
                with_desc_data[current_section].append(parts[0])

# Process without_desc.csv
with open('without_desc.csv', 'r') as f:
    current_section = ''
    for line in f:
        line = line.strip()
        # Check if this is a section header
        if line.startswith('***') and line.endswith('***'):
            current_section = line.strip('* \n')
            # Skip the header row
            next(f)
            continue
        if current_section and line:
            # Parse the CSV line
            parts = line.split(',')
            if parts and parts[0].isdigit():  # Make sure it's a data row
                without_desc_data[current_section].append(parts[0])

# Find differences and write results
with open('wo_win.txt', 'w') as wo_win, open('w_win.txt', 'w') as w_win:
    for section in with_desc_data.keys():
        wo_win.write(f"\n{section}\n")
        w_win.write(f"\n{section}\n")
        
        # Find indices in without_desc but not in with_desc
        w_winners = set(without_desc_data[section]) - set(with_desc_data[section])
        w_win.write("Indices in without_desc but not in with_desc:\n")
        w_win.write(", ".join(sorted(w_winners, key=lambda x: int(x))) + "\n")
        
        # Find indices in with_desc but not in without_desc  
        wo_winners = set(with_desc_data[section]) - set(without_desc_data[section])
        wo_win.write("Indices in with_desc but not in without_desc:\n")
        wo_win.write(", ".join(sorted(wo_winners, key=lambda x: int(x))) + "\n")
