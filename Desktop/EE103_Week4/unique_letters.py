s = "abcabc"
unique_chars = ""

for char in s:
    if char not in unique_chars:
        unique_chars += char

print("Number of unique letters:", len(unique_chars))