import random

# 入力を数値に変換する (文字などを受け付けた場合はNoneを返す)
def convert_integer(user_input):
    try:
        return int(user_input)
    except ValueError:
        return None

def main():
    answer = random.randint(1, 100)  # 回答となる数字
    count = 0  # 何回で当てられたか数える変数

    print("1 から 100 までの数字を当ててください。")

    while True:
        user_input = convert_integer(input("入力してください: "))

        if user_input is None:
            print("不正な入力です。整数を入力してください。")
            continue

        if user_input < 1 or user_input > 100:
            print("1から100までの数字を入力してください")
            continue

        count += 1

        if user_input < answer:
            print("もっと大きい数です")
        elif user_input > answer:
            print("もっと小さい数です")
        else:
            print("正解!", count, "回で当てました")
            break

# 実行
main()