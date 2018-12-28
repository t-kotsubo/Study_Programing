apple_price = 200
input_num = input('購入する個数を入力してください。：')
qty = int(input_num)
price = apple_price * qty
money = 1000
balance = money - price

if price < money:
    print('リンゴを', qty , '個購入しました。', '\n値段は', price, '円です。', '\n残りは', balance, '円です')

elif price == money:
    print('リンゴを', qty ,'個購入しました。', '\n値段は', price, '円です。', '\nお金がなくなりました。')

elif price > money:
    print('リンゴを', qty ,'個購入しようしとしました。', '\n値段は', price, '円です。', '\nお金が足りません。')

else :
    print('不正なデータです。')

print('現在の所持金は', balance, '円です。')