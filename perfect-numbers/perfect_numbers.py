def classify(number):
	if number <= 0:
		raise ValueError('Number must be a positive integer.')
	factors = [k for k in range(1, number) if number % k == 0]
	categories = {
		sum(factors) == number: 'perfect',
		sum(factors) > number: 'abundant',
		sum(factors) < number: 'deficient'
	}
	return categories[True]