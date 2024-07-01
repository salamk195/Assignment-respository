rice = int(input("enter the selling price of your rice"))
beans = int(input("enter the selling price of your beans"))
yam = int(input("enter the selling price of your yam"))
corn = int(input("enter the selling price of your corn"))
garri = int(input("enter the selling price of your garri"))
#if cost_price of every one of them = 22000
profit_of_rice =  rice - 22000
profit_of_beans = beans - 22000
profit_of_yam = yam - 22000
profit_of_corn =  corn - 22000
profit_of_garri = garri - 22000

if profit_of_rice > 1:
    print("profit on rice")
elif profit_of_rice < 1:
    print("loss on rice")


if profit_of_beans > 1:
    print("profit on beans")
elif profit_of_beans < 1:
    print("loss on beans")


if profit_of_yam > 1:
    print("profit on yam")
elif profit_of_yam < 1:
    print("loss on yam")


if profit_of_corn > 1:
    print("profit on corn")
elif profit_of_corn < 1:
    print("loss on corn")


if profit_of_garri > 1:
    print("profit on garri")
elif profit_of_garri < 1:
    print("loss on garri")





