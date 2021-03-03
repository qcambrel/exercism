def slices(series, length):
	if length > len(series):
		raise ValueError('Slice length cannot be greater than the length of the series.')
	elif length <= 0:
		raise ValueError('Slice length must be greater than zero.')
	else:
		return [series[i:i+length] for i in range(len(series)+1-length)]