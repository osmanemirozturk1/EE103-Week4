f = 0.264
binary_frac = "0."

while f > 0:
    f = f * 2
    int_part = int(f)
    binary_frac += str(int_part)
    f = f - int_part

print(f"Binary representation of the fraction {binary_frac}")