decimal_num = int(input("Enter a decimal integer: "))
binary_str = ""

if decimal_num == 0:
    binary_str = "0"
else:
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2

print(f"Binary representation: {binary_str}")
