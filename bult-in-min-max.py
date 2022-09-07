def maximum(value1, value2, value3):
	"""Return the maximum of three values."""
	max_value = value1
	if value2 > max_value:
		max_value = value2
	if value3 > max_value:
		max_value = value3
	return max_value

def minimum(value1, value2, value3):
	"""Return the minimum of three values"""
	min_value = value1
	if value2 < min_value:
		min_value = value2
	if value3 < min_value:
		min_value = value3
	return min_value


print (maximum(12, 27, 36))

print (max(12, 27, 36))


print (minimum(12, 27, 36))

print (min(15, 9, 27, 14))