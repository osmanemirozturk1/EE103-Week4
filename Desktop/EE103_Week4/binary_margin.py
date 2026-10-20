target_f = 0.1
f = target_f
binary_frac = "0."
current_val = 0.0
weight = 0.5

while abs(current_val - target_f) >= 0.0001:
    f = f * 2
    int_part = int(f)
    binary_frac += str(int_part)
    f = f - int_part

    if int_part == 1:
        current_val += weight

    weight /= 2
print(f"Binary representation of 0.1 an acceptable error: {binary_frac}")