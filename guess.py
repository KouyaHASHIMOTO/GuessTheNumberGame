import random

count = 0

choice = input("難易度を選んでください(1: 易しい, 2: 普通, 3: 難しい):")

if choice == "1":
    max_number = 10
elif choice == "2":
    max_number = 100
else:
    max_number = 1000


border = max_number // 10

answer = random.randint(1, max_number)

print("1から", max_number, "までの数字を当ててください")

while True:
    if count >= 10:
        result = "ゲームオーバー"
        print("回数制限に達しました終了します")
        break

    text = input("入力してください: ")

    try:
        guess = int(text)

    except ValueError:
        print("数字を入力してください")
        continue

    diff = abs(guess - answer)

    if diff > border:
        level = "かなり"
    else:
        level = "少し"

    count += 1

    if guess > answer:
        print("あなたの数字は", level, "大きいです")
    elif guess < answer:
        print("あなたの数字は", level, "小さいです")
    else:
        result = "正解"
        print("正解!", count, "回で当てました")
        break

with open("history.txt", "a", encoding="utf-8") as f:
    f.write(f"範囲 1~{max_number} / {count} 回で{result}\n")
