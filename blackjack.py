#
##########################################################################
# ブラックジャック
##########################################################################
##########################################################################
# インポート
##########################################################################
import random
##########################################################################
# 変数
##########################################################################
#(RANK)=数字
#(SUIT)=スート
RANK,SUIT = 0,1
##########################################################################
# サブルーチン
##########################################################################
##########################################################################
# プレイヤーターン
##########################################################################
def player_op(deck,player_hand,op):
    #戻り値初期化
    doubled,ending = False,False
    if op == "1":
        print("[プレイヤー：スタンド ]")
#       スタンドの処理
        doubled,ending = False,True
    elif op == "2":
        print("[プレイヤー：ヒット　 ]")
#       ヒットの処理
        player_hand.append(deck.pop())
        print_player_hand(player_hand)
        doubled,ending = False,True
    elif op == "3":
#       ダブルの処理
        if len(player_hand) == 2:
            print("[プレイヤー：ダブル　 ]")
            player_hand.append(deck.pop())
            print_player_hand(player_hand)
            doubled,ending = True,True
        else:
            print("[ダブルはできません。]")
#
    if get_point(player_hand) > 21:
        print("[プレイヤーはバストした]")
        ending = True
#
    if get_point(player_hand) == 21:
        print("[２１です！]")
        ending = True
#
    return doubled,ending
#
##########################################################################
# ポイント計算
##########################################################################
def get_point(hand):
    result = 0
    ace_flag = False
    for card in hand:

        #Aが含まれているか
        if card[RANK] == 1:
            ace_flag = True

        #ＪＱＫが含まれているか
        if card[RANK] > 10:
            num = 10
        else:
            num = card[RANK]
        result = result + num
#	Aが含まれていて合計が11以下の場合、Aを11とみなして加算
    if ace_flag == True and result <= 11:
        result +=10
    return result
#
##########################################################################
# プレイヤーの手札表示
##########################################################################
def print_player_hand(player_hand):
    print("プレイヤー（",get_point(player_hand),"）：　　　")
    for card in player_hand:
        print("[",card[SUIT],card[RANK],"]")
    print()
#
##########################################################################
# ディーラーの手札表示
##########################################################################
def print_dealer_hand(dealer_hand,uncoverd):
    if uncoverd:
        print("ディーラー（",get_point(dealer_hand),"）：　　　")
    else:
        print("ディーラー（??）：　　　")
#
#uncoverd=TRUE、flagの設定で1枚目は見れる
#uncoverdがFALSEで最初から見れない
    #
    flag = True
    for card in dealer_hand:
        if flag or uncoverd:
            print("[",card[SUIT],card[RANK],"]")
            flag = False
        else:
            print("[ ** ]")
    print()
#
##########################################################################
# デッキ作成
##########################################################################
def make_deck():
    suits = ["S","H","D","C"]
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)
    return deck
#
##########################################################################
# メインルーチン
##########################################################################
def main():
    turn = 1
    player_money = 100

#  デッキを作る
    while(player_money > 0):
        print("ターン：",turn)
        print("所持金",player_money)
#
#   プレイヤーの手札格納用リスト初期化
        player_hand = []
#   ディーラーの手札格納用リスト初期化
        dealer_hand = []
#   デッキ作成
        deck = make_deck()
        #print(deck)
        bet = 10
        player_money -= bet

        for i in range(2):
    #   デッキからプレイヤーの手札へ
            player_hand.append(deck.pop())
    #   デッキからディーラーの手札へ
            dealer_hand.append(deck.pop())

#        print(player_hand)
        print_player_hand(player_hand)
        print(get_point(player_hand))
#        print(dealer_hand)
        print_dealer_hand(dealer_hand,False)
        print(get_point(dealer_hand))
#
#		プレイヤーターン
        while True:
            op = input("スタンド：1　ヒット：2　ダブル：3>>")
            doubled,ending = player_op(deck,player_hand,op)
            if doubled:
                player_money += bet
                bet += bet
            if ending:
                break
#
        turn += 1
        input("次のターンへ")
    print("ゲームオーバー")

if __name__ == "__main__":
    main()
