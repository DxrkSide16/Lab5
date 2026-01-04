print("Input:")
lines = []
for _ in range(3):
    lines.append(input())

print("Output:")
for line in lines:
    new_name = ""
    space_flag = False
    for ch in line:
        if ch == " ":
            if not space_flag:
                new_name += "_"
                space_flag = True
        else:
            new_name += ch
            space_flag = False
    print(new_name)
