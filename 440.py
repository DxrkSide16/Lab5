data = input()

nums = []
current = ""

for ch in data:
    if ch != " ":
        current += ch
    else:
        nums.append(int(current))
        current = ""

nums.append(int(current))

x1 = nums[0]
y1 = nums[1]
x2 = nums[2]
y2 = nums[3]

dx = x2 - x1
dy = y2 - y1

dist = (dx * dx + dy * dy) ** 0.5

dist = int(dist * 100 + 0.5) / 100

if dist == int(dist):
    print(str(int(dist)) + ".00")
elif int(dist * 10) == dist * 10:
    print(str(dist) + "0")
else:
    print(dist)
