s = input("请输入一行字符：")
alpha_count = 0
digit_count = 0
space_count = 0
other_count = 0
for char in s:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == ' ':
        space_count += 1
    else:
        other_count += 1
print(f"英文字符: {alpha_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
