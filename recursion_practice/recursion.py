# 以下に、スライドに記載された3つのチャレンジを解くためのPythonコードを示します。

# チャレンジ1: 再帰を使ってnthのフィボナッチ数を見つける関数
def fibonacci(n):
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# チャレンジ2: 再帰を使ってフレーズが回文かどうか判定する関数
def is_palindrome(phrase):
    # フレーズを小文字に変換し、非アルファベット文字を除去する
    phrase = ''.join(c for c in phrase.lower() if c.isalpha())
    # フレーズが空か、一文字なら真を返す
    if len(phrase) <= 1:
        return True
    # 最初と最後の文字が同じなら、それを取り除いて再帰的にチェックする
    if phrase[0] == phrase[-1]:
        return is_palindrome(phrase[1:-1])
    return False


# チャレンジ3a: 再帰を使ってべき乗を計算する関数（正の指数のみ）
def simple_exponent(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent should be a non-negative integer.")
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * simple_exponent(base, exponent - 1)


# チャレンジ3b: 再帰を使ってべき乗を計算する関数（負の指数も許容）
def simple_exponent_modified(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / simple_exponent_modified(base, -exponent)
    else:
        return base * simple_exponent_modified(base, exponent - 1)


# テストケース
# チャレンジ1: 6番目のフィボナッチ数
fibonacci_6 = fibonacci(6)

# チャレンジ2: "Madam" と "Hello" が回文かどうか
palindrome_check_1 = is_palindrome("Madam")
palindrome_check_2 = is_palindrome("Hello")

# チャレンジ3a: 3の4乗
exponent_3_4 = simple_exponent(3, 4)

# チャレンジ3b: 3の-4乗
exponent_3_negative_4 = simple_exponent_modified(3, -4)

print(fibonacci_6, palindrome_check_1, palindrome_check_2, exponent_3_4, exponent_3_negative_4)
