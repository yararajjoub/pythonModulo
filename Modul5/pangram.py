def is_pangram(textLista):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lowercase_text = textLista.lower()
    for item in lowercase_text:
        if item in alphabet:
            alphabet.remove(item)
    if len(alphabet) == 0:
        return True
    else:
        return False


text = 'This is just any text.'
if is_pangram(text):
    print('The text is a pangram.')
else:
    print('The text is not a pangram.') # This will be printed
