from collections import Counter
import emoji
import re
import json

with open('/data2/ljiayi/projects/nlp/ELCo/benchmark_data/exp-entailment/test.json', 'r') as f:
    test_data = json.load(f)

# Read and process w_win.txt
w_win_counts = Counter()
with open('w_win.txt', 'r') as f:
    for line in f:
        if line.startswith('Indices'):
            # Get the indices line and split into individual numbers
            indices = next(f).strip().split(', ')
            # Count each index
            w_win_counts.update(indices)

# Read and process wo_win.txt  
wo_win_counts = Counter()
with open('wo_win.txt', 'r') as f:
    for line in f:
        if line.startswith('Indices'):
            # Get the indices line and split into individual numbers
            indices = next(f).strip().split(', ')
            # Count each index
            wo_win_counts.update(indices)

#print("Counts from w_win.txt (>5 occurrences):")
w_win_emojis = {}
for idx, count in sorted(w_win_counts.items(), key=lambda x: int(x[0])):
    text = test_data[int(idx)]['sent1']
    text = text.replace("This is ", "", 1)
    # split by "[EM] ""
    emoji_names = [part.strip() for part in text.split("[EM]") if part.strip()]
    emoji_names = [re.sub(r"[^\w\d_]", "", name) for name in emoji_names]
    for emoji_name in emoji_names:
        emoji_symbol = emoji.emojize(f":{emoji_name}:", language="alias")
        if emoji_symbol not in w_win_emojis:
            w_win_emojis[emoji_symbol] = 0
        w_win_emojis[emoji_symbol] += count

#print("\nCounts from wo_win.txt (>5 occurrences):")
wo_win_emojis = {}
for idx, count in sorted(wo_win_counts.items(), key=lambda x: int(x[0])):
    text = test_data[int(idx)]['sent1']
    text = text.replace("This is ", "", 1)
    # split by "[EM] ""
    emoji_names = [part.strip() for part in text.split("[EM]") if part.strip()]
    emoji_names = [re.sub(r"[^\w\d_]", "", name) for name in emoji_names]
    for emoji_name in emoji_names:
        emoji_symbol = emoji.emojize(f":{emoji_name}:", language="alias")
        if emoji_symbol not in wo_win_emojis:
            wo_win_emojis[emoji_symbol] = 0
        wo_win_emojis[emoji_symbol] += count

print(f"w_win_emojis: {w_win_emojis}")
print(f"wo_win_emojis: {wo_win_emojis}")

results = {
    "with_description_wins": w_win_emojis,
    "without_description_wins": wo_win_emojis
}

with open('emoji_wins.json', 'w') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
