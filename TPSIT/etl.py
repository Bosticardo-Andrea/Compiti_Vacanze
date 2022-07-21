def transform(old_data):
    new_data = {}
    for x, letters in old_data.items():
        for letter in letters:
            new_data[letter.lower()] = x
    return new_data