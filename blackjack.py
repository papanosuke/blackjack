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
#(RANK)=数字
#(SUIT)=スート
RANK,SUIT = 0,1
def get_point(hand):
    result = 0
    for card in hand:
        if card[RANK] > 10:
            num = 10
        else:
            num = card[RANK]
        result = result + num
    return result
#
def make_deck():
    suits = ["S","H","D","C"]
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)
    return deck
#
def main():
    turn = 1
    player_money = 100

#  デッキを作る
    while(player_money > 0):
        print("ターン：",turn)
        print("所持金",player_money)
#
#   プレイヤーの手札格納用リスト
        player_hand = []
#   ディーラーの手札格納用リスト
        dealer_hand = []
#   デッキ作成
        deck = make_deck()
        #print(deck)
        for i in range(2):
    #   デッキからプレイヤーの手札へ
            player_hand.append(deck.pop())
    #   デッキからディーラーの手札へ
            dealer_hand.append(deck.pop())
        print(player_hand)
        print(get_point(player_hand))
        print(dealer_hand)
        print(get_point(dealer_hand))

        turn += 1
        input("次のターンへ")
    print("ゲームオーバー")

if __name__ == "__main__":
    main()