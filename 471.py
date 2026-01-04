print("Input:")
line = input()

nums = []
current = ""
for ch in line:
    if ch != " ":
        current += ch
    else:
        if current != "":
            nums.append(int(current))
            current = ""
if current != "":
    nums.append(int(current))

positives = []
negatives = []

for n in nums:
    if n > 0:
        positives.append(n)
    elif n < 0:
        negatives.append(n)

positives.sort(reverse=True)
negatives.sort()

result = positives + negatives

print("Output:")
print(" ".join(str(x) for x in result))
