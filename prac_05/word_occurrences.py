text = "this is a collection of words of nice words this is a fun thing it is"
print(f"Text: {text}")

word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_word_length = max(len(word) for word in word_counts)
for word in sorted(word_counts):
    print(f"{word:{max_word_length}}: {word_counts[word]}")