def divide(a, b):
    try:
        return a / b  # まず割り算を試みる
    except ZeroDivisionError:  # エラーを捕捉
        return "Error: division by zero"


# 使用例
result = divide(10, 0)
print(result)  # エラーメッセージを出力
