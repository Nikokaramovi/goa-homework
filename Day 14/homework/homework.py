#1
#1


x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(x[0])
print(x[-1])
x[2] =  "Midweek"
print(x)


#2
animals = input("enter 5 animal names:")
res = animals.split(" ")
print(res[0], res[-1])
res[1] = input("enter second animal name:")
print(res)


#3
listn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(listn[::3])
print(listn[::-1])
new_numbers = listn[3:9]
print(new_numbers)


#4
number = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500]
first_five = number[:5]
every_third = number[::3]
final_list = first_five + every_third 
print(first_five)
print(every_third)
print(final_list)


#5

number1 = input("enter 10 numbers").split(" ")
print(number1[:3])

print(number1[3:7])
if number1[-1] == 10:
    print("the last number is 10")
else:
    print("the last number is not 10")