def add_prefix_un(word):
    return "un" + word
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    with_prefix = [prefix + word if word != prefix else word for word in vocab_words]
    return " :: ".join(with_prefix)
def remove_suffix_ness(word):
    if word[-5] == 'i':return word[:-5] + 'y'
    else:return word[:-4]
def adjective_to_verb(sentence, index):
    sentence_arr = sentence.replace(".","").split(' ')
    return sentence_arr[index] + "en"