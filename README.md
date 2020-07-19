# Python fractions

This code demonstrates how fractions can be expanded in an arbitrary base.

If you just want to print some arbitrary number of digits of a given fraction, use the functions in `fraction_to_string.py`. If you want to efficiently be able to find the nth digit of a fraction, use the functions in `fractions.py`.

## Examples

Obtain the decimal expansion of 1/5 up to 4 digits behind the dot:

```
$ python -i fraction_to_string.py
>>> fraction_str(1, 5, 4):
'0.200'
```

Obtain the binary expansion of 1/123 up to 300 digits behind the dot:

```
$ python -i fraction_to_string.py
>>> fraction_str(1, 123, 300, 2)
'0.000000100001010011010000001000010100110100000010000101001101000000100001010011010000001000010100110100000010000101001101000000100001010011010000001000010100110100000010000101001101000000100001010011010000001000010100110100000010000101001101000000100001010011010000001000010100110100000010000101001101'
```

Does the fraction 1/12 have a finite decimal expansion?

```
$ python -i fractions.py
>>> has_finite_expansion(fraction(1, 12))
False
```

Does the fraction 1/12 have a finite expansion in base 6?

```
$ python -i fractions.py
>>> has_finite_expansion(fraction(1, 12, 6))
True
```

What is the second digit of 1/5?

```
$ python -i fractions.py
>>> get_digit(fraction(1, 5), 2)
2
```

Note that 1/5 is represented as 0.2, so the second digit is 2. If this is an issue, I recommend that you use `get_significant_digit` or `get_fractional_digit`.

What is the 99th digit behind the dot of 1/101?

```
$ python -i fractions.py
>>> get_fractional_digit(fraction(1, 101), 99)
9
```

What is the digit corresponding to 10^-10 in the decimal expansion of 1/7?

```
$ python -i fractions.py
>>> get_significant_digit(fraction(1, 7), -10)
8
```
