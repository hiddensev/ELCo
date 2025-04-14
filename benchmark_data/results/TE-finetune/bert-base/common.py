import json

# Read emoji_wins.json
with open('emoji_wins.json', 'r') as f:
    emoji_wins = json.load(f)

with_desc = emoji_wins['with_description_wins']
without_desc = emoji_wins['without_description_wins']

# Get all unique emojis
all_emojis = set(with_desc.keys()) | set(without_desc.keys())

# Calculate differences
differences = {}
for emoji in all_emojis:
    with_count = with_desc.get(emoji, 0)
    without_count = without_desc.get(emoji, 0)
    differences[emoji] = with_count - without_count

sorted_differences = dict(sorted(differences.items(), key=lambda x: x[1]))
# Write results to file
with open('emoji_differences.json', 'w') as f:
    json.dump(sorted_differences, f, ensure_ascii=False, indent=2)
