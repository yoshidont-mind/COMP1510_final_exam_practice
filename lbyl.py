def divide(a, b):
    if b != 0:  # 0で割る前に確認
        return a / b
    else:
        return "Error: division by zero"


# 使用例
result = divide(10, 2)
print(result)  # 5を出力
