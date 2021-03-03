from itertools import takewhile

def proteins(strand):
	translation = {
		'AUG': 'Methionine',
		'UUU': 'Phenylalanine',
		'UUC': 'Phenylalanine',
		'UUA': 'Leucine',
		'UUG': 'Leucine',
		'UCU': 'Serine',
		'UCC': 'Serine',
		'UCA': 'Serine',
		'UCG': 'Serine',
		'UAU': 'Tyrosine',
		'UAC': 'Tyrosine',
		'UGU': 'Cysteine',
		'UGC': 'Cysteine',
		'UGG': 'Tryptophan',
		'UAA': 'STOP',
		'UAG': 'STOP',
		'UGA': 'STOP'
	}
	n = 3
	codons = [strand[i:i+n] for i in range(0, len(strand), n)]
	return list(takewhile(lambda x: x != 'STOP', [translation[codon] for codon in codons]))