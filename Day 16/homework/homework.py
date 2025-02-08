# .insert(index, value) - ამატებს list'ში ელემენტს რომელ ინდექსზეც გვინდა
# .pop(index) - აგდებს ელემენტს კონკრეტული ინდექსიდან
# len() - თვლის string'ში სიმბოლოების და list'ში ელემენტების რაოდენობას
# .append() - list'ის ბოლოში ამატებს იმ ელემენეტს რასაც ფრჩხილებში ჩავუწერთ
# .lower() - lower'ი დიდ ასოებს გადააქცევს პატარა ასოებად და პატარა ასოებს ტოვებს ისე პატარას
# .upper() - upper'ი ადიდებს ასოებს და დიდ ასოს ტოვებს ისევ დიდად
# .capitalize - capitalize  ადიდებს პირველ ასოს ხოლო დანარჩენს აპატარავებს
# .find - find'ი ეძებს მითითებულ ელემენტს როგორც ლისტში ასევე სტრინგებშიც


surname = ["tavadze","karamovi","abuladze","gvelesiani","motiashvili"]
name = input("enter your name: ")
if len(name) > 7:
    surname.append(name)

print(surname)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::2])


res1 = "niko"
print(len(res1))



name1 = input("enter your name in uppercase: ")
print(name1.lower())


surname1 = "karamovi"
print(surname1.upper())


res2 = "niko"
print(res2.capitalize())