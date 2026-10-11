age=int(input("Enter your age: "))
day=input("Enter the day of the week: ")

if age<5:
    print("You get in for free!")
else:
    if age>=5 and age<=12:
        print("The price is 50,000 Toman.")
    elif age>=60:
        print("The price is 60,000 Toman.")
    else:
        print("The price is 100,000 Toman.")
if day.lower()=="tuesday":
    print("You get a 20% discount on Tuesdays!")
