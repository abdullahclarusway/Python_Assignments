x = input("Please enter a number:")
my_list = list(x)
sum = 0
if x.isdigit() == True:
    for i in my_list:
        first_sum = int(i) ** len(my_list)
        sum += first_sum
    if int(x) == sum:
        print("{} is an Armstrong number".format(x))
    else:
        print("{} is not an Armstrong number".format(x))
else:
    print("It is an invalid entry. Don't use  non-numeric, float or negative values!")