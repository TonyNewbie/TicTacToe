text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
length = int(input())
shorter_list = [word for word_line in text for word in word_line if len(word) <= length]
print(shorter_list)
