#!/usr/bin/env python

# Return the list of digits of n, in the given base
def int_digits(n, base):
	return [n] if n < base else int_digits(n // base, base) + [n % base]

# Return a tuple (digit_list, period), where
#     digit_list is the list of digits
#     period is the period of the digits
#     (when period == 3, this means the last 3 digits repeat)
def frac_digits(c, d, base):
	digit_list = []
	c = c % d
	numerators = {}
	period = 0
	while True:
		if c in numerators:
			return digit_list, period - numerators[c]
		numerators[c] = period
		c *= base
		quotient = c // d
		digit_list.append(quotient)
		c -= quotient * d
		period += 1

# Return a description of the digits of c/d in the given base.
# This description is a tuple (digits, integer_digits, period), where
#     digits is the list of digits
#     integer_digits is the number of digits before the point
#     period is the period with which the digits repeat
#     (when period == 3, this means the last 3 digits repeat)
def fraction(c, d, base = 10):
	integer_part = c // d
	rest = c - integer_part * d
	integer_digits = int_digits(integer_part, base)
	fractional_digits, period = frac_digits(rest, d, base)
	return integer_digits + fractional_digits, len(integer_digits), period

# Obtain the nth fractional digit from a fraction description. Note
# that this function is oblivious about the base -- it depends on the
# programmer to make sure that fraction is called with the right base.
def get_fractional_digit(frac, n):
	_, int_digits, _ = frac
	return get_digit(frac, n + int_digits)

# Obtain the nth digit from a fraction description. Note that this
# function is oblivious about the base -- it depends on the programmer
# to make sure that fraction is called with the right base.
def get_digit(frac, n):
	assert n > 0
	n -= 1
	digits, int_digits, period = frac
	if n < len(digits):
		return digits[n]
	return digits[-period:][(n - len(digits)) % period]

# Does the given fraction description has a finite expansion?
# Note that this function is oblivious about the base -- it depends on
# the programmer to make sure that fraction is called with the right base.
def has_finite_expansion(frac):
	digits, int_digits, period = frac
	return period == 1 and digits[-1] == 0

# Get the digit corresponding to base^n
def get_significant_digit(frac, n):
	digits, int_digits, period = frac
	if n > int_digits:
		return 0
	n = int_digits - 1 - n
	if n < 0:
		return 0
	if n < len(digits):
		return digits[n]
	return digits[-period:][(n - len(digits)) % period]

