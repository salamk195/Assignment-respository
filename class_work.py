user_inputed_value = int(input("Welcome to Jendol online Superstores, PLease select Card type 1. Regular, 2. Silver, 3. Gold, 4. Platinum" ))
S = "Silver"
G = "Gold"
P = "Platinum"
R = "Regular"
user_card = R
if user_inputed_value ==2:
    user_card = S
elif user_inputed_value ==3:
    user_card = G
else:
    user_card = P



Total_amount_of_goods_bought = ("Enter the total amount of goods you bought")
if Total_amount_of_goods_bought > 1000 :
    print("you have a discount of 5% ")
elif user_inputed_value == R :
   print( Total_amount_of_goods_bought * 5 / 100 )
elif user_inputed_value ==S:
    print( Total_amount_of_goods_bought * 10 / 100)
elif user_inputed_value == G :
    print(Total_amount_of_goods_bought * 15 / 100 )
elif user_inputed_value == P :
    print(Total_amount_of_goods_bought * 20 / 100)



if Total_amount_of_goods_bought > 2000 :
    print("you have a discount of 10%")
elif user_inputed_value == R :
   print( Total_amount_of_goods_bought * 15 / 100 )
elif user_inputed_value == S:
    print( Total_amount_of_goods_bought * 20 / 100)
elif user_inputed_value == G :
    print(Total_amount_of_goods_bought * 25 / 100 )
elif user_inputed_value == P :
    print(Total_amount_of_goods_bought * 30 / 100)
    

