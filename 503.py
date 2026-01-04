print("Input:")
lines = []
for _ in range(3):
    lines.append(input())

print("Output:")
for s in lines:
    total = 0
    prev = 0
    i = len(s) - 1
    while i >= 0:
        ch = s[i]
        if ch == "I":
            curr = 1
        elif ch == "V":
            curr = 5
        elif ch == "X":
            curr = 10
        elif ch == "L":
            curr = 50
        elif ch == "C":
            curr = 100
        elif ch == "D":
            curr = 500
        elif ch == "M":
            curr = 1000
        else:
            curr = 0

        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
        i -= 1

    print(total)
