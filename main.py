s=input("请输入一行字符:")
alpha=digit=space=other=0
for char in s:
    if char.isalpha():
         alpha += 1
    elif char.isdigit():
         digit += 1
    elif char =='':
        space += 1
    else:
        other += 1
print("英文字符:",alpha)
print("数字:",digit)
print("空格:",space)
print("其他字符:",other)
