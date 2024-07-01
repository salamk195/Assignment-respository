home expenses

rent = 1200
groceries = 300
t_fare = 150
entertainment = 100
misselenious = 50
M = (rent+groceries+t_fare+entertainment+misselenious)
#M representinmg total monthly expense
print(M)
d = M/30
#d is daily expenses
print(d)


#converting form degree to celcius

temperature_in_celcius = input("Enter temperature degree in celcius")
#to get farenhit temperature
temperature_in_farenhit = (float(temperature_in_celcius)*9/5)+32
print(float(temperature_in_farenhit))



#tell me the year you were born and ill give you your age

year_given = input("enter the year you were born")
your_age = 2024-(float(year_given))
print(float(your_age))



#age calculator

first_number = input("put first number")
second_number = input("put second number")
third_number = input("put third number")
fourth_number = input("put fourth number")
fifth_number = input("put fifth number")
numerator = first_number + second_number + third_number +fourth_number + fifth_number
mean = (float(numerator)/5)
print(float(mean) )










#fiday 28th today





#conerting pounds to dollar
#formula = amount in pounds  * 1.26

amount_given = int(input('write amount in pounds'))
price_in_dollar = (amount_given) * 1.26
print(price_in_dollar)




#circumfrence of a circle
#foormula is C = 2pir

pi = 22/7

radius = int(input('radius'))
circumfrence = 2 * (pi) *(radius)
print(circumfrence)


#reverse inputed name
name_to_reverse = input('write your name')
reverse = name_to_reverse[::-1]
print(reverse)


#accpet input from user and print out the first and last name
given_name = input("Write your name")
first_letter = (given_name[0])
last_letter = (given_name[-1])
print("The first letter of your beautiful name is " + first_letter + " and the last letter is " + last_letter)
print(first_letter + last_letter)


#calculate the circumfrence of a circle




#formula for compound interest 
#    A = P(1+r/100)t

#where A = final amount P = initaial principal balance r = interest n = number of times interest applied per time period t = number of times elapsed


principal = int(input("principal_amount"))
inputed_rate = int(input("interest rate"))
rate = float(inputed_rate/100)
time = float(input("time"))

amount = principal * (1 + rate)**time
print(amount)



assigmnet for the weekend

#a super store makes sales of five goods

#phones, freezer, television, Air conditioner, batteries

cost_price_of_phone = 72000
cost_price_of_freezer = 150000
cost_price_of_television = 120000
cost_price_of_Air_conditioner = 500000
cost_price_of_battery = 200000

selling_price_of_phone = int(input('Cost price of phone = 72000 What is your selling price'))
selling_price_of_frezzer=int(input('Cost Cost price of freezer = 150000 What is your selling price '))
selling_price_of_television = int(input('Cost price of television = 120000 What is your selling price'))
selling_price_of_Air_conditioner = int(input('Cost price of Air conditioner = 500000 What is your selling price'))
selling_price_of_battery = int(input('Cost price of battery = 200000 What is your selling price'))


total_selling_price = selling_price_of_phone + selling_price_of_frezzer + selling_price_of_television + selling_price_of_Air_conditioner + selling_price_of_battery

total_cost_price = cost_price_of_phone + cost_price_of_freezer + cost_price_of_television + cost_price_of_Air_conditioner + cost_price_of_battery





if total_selling_price > total_cost_price:
	print('You have made profit of ', total_selling_price - total_cost_price)
elif total_selling_price < total_cost_price:
	print('You have made a loss of ', total_cost_price - total_selling_price)



assignment 2


#Folade is a student that offers 10 courses, at the end of the semster are scores are below
#input scores  wrtie a program to calculate her standing in the class 70 above A,60-69 B, 50-59 C, 40-49 D, 30-39 E, 29-0 F

score_for_maths = int(input('Please input the score for maths'))
score_for_english = int(input('Please input the score for english'))
score_for_chemistry = int(input('Please input the score for chemistry'))
score_for_biology = int(input('Please input the score for biology'))
score_for_agric = int(input('Please input the score for agric'))
score_for_physics = int(input('Please input the score for physics'))
score_for_economics = int(input('Please input the score for economics'))
score_for_civic = int(input('Please input the score for civic'))
score_for_crk = int(input('Please input the score for crk'))
score_for_history = int(input('Please input the score for history'))
score_for_bookkeeping = int(input('Please input the score for bookkeeping'))

each_scores = (score_for_agric + score_for_biology + score_for_bookkeeping + score_for_chemistry + score_for_civic + score_for_crk + score_for_economics + score_for_english + score_for_history + score_for_maths + score_for_physics)/10

if each_scores >= 70:
    print('You are among the best, You have A')
elif each_scores >60 < 69:
    print('You have done well, you have B')
elif each_scores >50 <69:
    print('Do better next time, You have C')
elif each_scores > 40 <49:
    print('Your performance was bad, you have D')
elif each_scores >30 <39:
    print('Very bad from you, you have E')
elif each_scores >0 <20:
    print('Worst performance, you have F you are repeating this class')











