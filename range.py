age = int(input("enter your age"))

if(age >= 1 and age <= 110):
    if(age>=18):
        print("you are eligible to vote")
    else:
        print("not eligible")
else:
    print("enter valid number")
