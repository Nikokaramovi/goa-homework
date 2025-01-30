#1
x=int(input("enter your number: "))
if x %2 == 0:
    print("even")
else:
    print("odd")

#2
for i in range(1, 50,):
    if i % 2 == 0:
        print(i)

#3
listn = [3, 7, 5, 12, 18, 25, 9, 30, 2, 15]
for i in listn:
    if i > 10:
        print(i)



#4
numbers = [15, 7, 5, 12, 18, 25, 9, 30, 2, 3]
print(numbers[0] + numbers[9])
print(numbers[0] * numbers[9])
print(numbers[0] / numbers[9])

#5
x = int(input("შეიყვანეთ რიცხვი (0-4): "))
names = ["ანა", "გიორგი", "ნიკა", "მარიამი", "დავითი"]
print(names[x])
    
