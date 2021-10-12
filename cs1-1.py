#author CJP 10/12/2021
first_x_value = int(input("Enter first value of x. "))
first_y_value = int(input("Enter first value of y. "))
second_x_value = int(input("Enter second value of x. "))
second_y_value = int(input("Enter second value of y. "))

distance = (((second_x_value - first_x_value) ** 2) + ((second_y_value - first_y_value) ** 2) ** (1/2))
print(distance)