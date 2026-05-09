credit_numb = "1234-5678-9123"
print(credit_numb[0])
print(credit_numb[0:4])
print(credit_numb[-1])

last_digits = credit_numb[-4:]
print(f"XXXX-XXXX-{last_digits}")

invert_numb = credit_numb[::-1]
print(invert_numb)