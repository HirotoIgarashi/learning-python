import random

# 開始
#   コンピュータの手を決める
random_choice = random.randint(0, 2)
# print("The computer choses", random_choice)

if random_choice == 0:
    computer_choice = "rock"
elif random_choice == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

print("The computer choices", computer_choice)

# じゃんけん中
#   ユーザの手を取得する
# user_choice = input("rock, paper or scissors? ")
user_choice = ""
while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    user_choice = input("rock, paper or scissors? ")
# print("You chose", user_choice, "and the computer chose", computer_choice)
# if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
#     print("User chose", user_choice)

#       ユーザの手がグー、チョキ、パー以外の時は再度入力を促す
#   コンピュータの手とユーザの手で判定する
# if computer_choice == "paper" and user_choice == "rock":
#     winner = "Computer"

#       コンピュータが勝った時の出力
#       ユーザが勝った時の出力
#       あいこの時は再度入力を促す
if computer_choice == user_choice:
    winner = "Tie"
elif computer_choice == "paper" and user_choice == "rock":
    winner = "Computer"
elif computer_choice == "rock" and user_choice == "scissors":
    winner = "Computer"
else:
    winner = "User"

# print("The", winner, "wins")
if winner == "Tie":
    print("We both chose", computer_choice + ", play again.!")
else:
    print(winner, "won. The computer chose", computer_choice + ".")

# ゲーム終了
