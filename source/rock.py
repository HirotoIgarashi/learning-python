import random

print("You rock!")
# 開始
#   コンピュータの手を決める
random_choce = random.randint(0, 2)
print("The computer choses", random_choce)

# じゃんけん中
#   ユーザの手を取得する
#       ユーザの手がグー、チョキ、パー以外の時は再度入力を促す
#   コンピュータの手とユーザの手で判定する
#       コンピュータが勝った時の出力
#       ユーザが勝った時の出力
#       あいこの時は再度入力を促す
# ゲーム終了
