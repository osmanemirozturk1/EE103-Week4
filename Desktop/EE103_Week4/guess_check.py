for a in range(11):
    for b in range(11):
        for c in range(11):
            if a + b + c == 10 and b == a - 2 and c == a * 2:
                print(f"Alyssa sold {a} tickets")
                