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

