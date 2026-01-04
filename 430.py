line = input()
n_raw = input()

n = ""
for ch in n_raw:
    if ch != " ":
        n += ch

count = 0
current = ""

for ch in line:
    if ch != " ":
        current += ch
    else:
        if current == n:
            count += 1
        current = ""

if current == n:
    count += 1

print(count)

line = input()
n_raw = input()

n = ""
for ch in n_raw:
    if ch != " ":
        n += ch

count = 0
current = ""

for ch in line:
    if ch != " ":
        current += ch
    else:
        if current == n:
            count += 1
        current = ""

if current == n:
    count += 1

print(count)
