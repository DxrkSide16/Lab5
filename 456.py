print("Enter binary numbers (4-bit) separated by commas:")
line = input()

result = ""
current = ""

for ch in line:
    if ch != ",":
        current += ch
    else:
        value = 0
        for b in current:
            value = value * 2 + (b == "1")
        if value % 5 == 0:
            if result != "":
                result += ","
            result += current
        current = ""

value = 0
for b in current:
    value = value * 2 + (b == "1")
if value % 5 == 0:
    if result != "":
        result += ","
    result += current

print("Output:")
print(result)
