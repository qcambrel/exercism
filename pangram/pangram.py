from string import ascii_lowercase

def is_pangram(sentence):
	letters = [char.lower() for char in sentence if char.isalpha()]
	letters_in_sentence = ''.join(sorted(set(letters)))
	return letters_in_sentence == ascii_lowercase