import json
import csv

# Read JSON file
with open('test.json', 'r') as f:
    data = json.load(f)

mapping = {
    "Direct": 0,
    "Metaphorical": 1,
    "Semantic list": 2,
    "Reduplication": 3,
    "Single": 4,
    "Negative": 6,
}
# Write to CSV file
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(['sent1', 'sent2', 'label', 'strategy'])
    for item in data:
        # no description
        # sent1 = item['sent1'].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(':', '')
        # with description
        descs = [desc.split('2.')[0].replace('1.', '').replace('The image features', '').replace('\n', '').strip().strip('.') for desc in item['generated_description']]
        sent1 = 'This is ' + ' and '.join(descs)
        # Convert emoji list string to format with [EM] tokens
        writer.writerow([sent1, item['sent2'], item['label'], item['strategy']])

