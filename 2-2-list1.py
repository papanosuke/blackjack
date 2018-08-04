import random
#
#  使う変数の宣言
#  (player_hand,player_money,dealer_hand)
#  (RANK,SUIT)
#  (turn)
#
#  トランプデッキを作ってシャッフルする関数
#  (make_deck)
#
#  手札の情報を表示する関数
#  (print_player_hand,print_dealer_hand)
#
#  ポイントを換算する関数
#  (get_point)
#
#  プレイヤーの思考パターンを記述する関数
#  (player_op)
#
#  ディーラーの思考パターンを記述する関数
#  (dealer_op)
#
#  勝敗判定とそれに伴って変化するチップを計算する関数
#  (win_lose)
#
# turn = 1
#
#  デッキを作る
while(player_money > 0):
	#  変数の初期化
	#  ベットする額
	#  お互いにカードを2枚ずつ引く
	#  プレイヤーのターン
	#  ディーラーのターン
	#  手札の公開
	#  勝敗の判定
	turn += 1
print("ゲームオーバー")
