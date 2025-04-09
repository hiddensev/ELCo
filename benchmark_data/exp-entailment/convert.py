import json
import csv

# Read JSON file
with open('val.json', 'r') as f:
    data = json.load(f)


mapping = {
    "Direct": 0,
    "Metaphorical": 1,
    "Semantic list": 2,
    "Reduplication": 3,
    "Single": 4,
}
# Write to CSV file
with open('val.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(['sent1', 'sent2', 'label', 'strategy'])
    
    # Write data rows
    for item in data:
        sent1 = item['sent1'].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(':', '')
        # Convert emoji list string to format with [EM] tokens
        writer.writerow([sent1, item['sent2'], item['label'], mapping[item['strategy']]])

