#author CJP 10/12/2021


p = int(input("Enter investment amount. "))
r = int(input("Enter the annual interest rate. ")) 
t = int(input("Enter the number of years the money is in account. "))

value_of_account = p * ((1 + (r / 12)) ** (12 * t))
print(value_of_account)