def is_armstrong_number(number):
	digits = list(map(int, list(str(number))))
	n = len(digits)
	raised_digits = [digit**n for digit in digits]
	return sum(raised_digits) == number