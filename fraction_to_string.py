#!/usr/bin/env python

# Possible improvements for fraction_str:
#     - Implement rounding
#     - Implement early termination when the number ends with 0000...
#     - Don't print the dot for integer numbers or when num_digits == 0

# Converts an integer to a digit character 0, 1, ..., 9, a, b, .., z
def digit(k):
	return str(k) if k < 10 else chr(ord('a') + k - 10)

# Convert an integer to a string in the given base
def integer_str(k, base):
	return digit(k) if k < base else integer_str(k // base, base) + digit(k % base)

# Convert a fraction c / d < 1 to the representation in the positional
# number system with the given base and the given number of digits
def fractional_str(c, d, num_digits, base):
	assert c < d
	c *= base
	quotient = c // d
	return '' if num_digits == 0 else digit(quotient) + fractional_str(c - quotient * d, d, num_digits - 1, base)

# Convert a fraction to the representation in the positional number system with
# the given base and the given number of digits. Note that num_digits is the
# number of digits behind behind the point, not the number of total digits!
def fraction_str(c, d, num_digits, base = 10):
	assert num_digits > 0
	sign = 1
	if c < 0:
		sign = -sign
		c = -c
	if d < 0:
		sign = -sign
		d = -d
	quotient = c // d
	rest = c - quotient * d
	sign = '-' if sign == -1 else ''
	return sign + integer_str(quotient, base) + '.' + fractional_str(rest, d, num_digits, base)
