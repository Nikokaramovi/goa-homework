"""1)მომხმარებელს შემოატანინე თავისი სახელი, შემდეგ შემატანინეთ მეგობრის გვარი და დაბეჭდეთ ისინი კონკატინაციის მეშვეობით."""

user_name = input("please enter your name :")
friend_surname = input("please enter friend surname :")
full_name = user_name + " " + friend_surname
print(full_name)




"""2)მომხმარებელს შემოატანინეთ მისი ასაკი და დაუბეჭდეთ რამდენი წლის იქნება 10 წელში."""

age = 13
print(age+10)


"""3)მომხმარებელს შემოატანინეთ 5 რიცხვი და დაითვალეთ ამ რიცხვების საშუალო არითმეტიკული."""


num1 = input("choose a number:")
num2 = input("choose a number:")
num3 = input("choose a number:")
num4 = input("choose a number:")
num5 = input("choose a number:")
nums = (int(num1) + int(num2) + int(num3) + int(num4) + int(num5))/5
print(nums)


"""4)კომენტარის სახით ახსენით რა არის Case Sensitive + რა არის Snake Case."""
#case sensitive- არის მაგალითად: თუ სისტემაში არის "book" მაშინ ვერ იქნება "BOOK" ან "Book" იმიტომ რომ case sensitive-ია
#Snake Case- ანუ Snake_case  არის წინადადების ქვეშ გასმული ხაზი  Snake_case ვერ იქნება Snake\case 
 

"""5)დაუშვით 5 შეცდომა და გვერდით კომენტარის სახით მიუწერეთ სწორი ვერსია (ახსენით რა არის Debugging)"""
1#print = (name)  #სწორი პასუხი: print(name)
2#color = orange #სწორი პასუხი: сolor = "orange"
3#name = giorgi #სწორი პასუხი: name = "giorgi"
4#print("book') #სწორი პასუხი: print("book")
5#age13 #სწორი პასუხი: age = 13
