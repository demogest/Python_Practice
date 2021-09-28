bmi,age = eval(input("pleas input the bmi and age(divided by commas):"))
if bmi >= 22.0 and age < 45:
    print("medium")
elif bmi < 22.0 and age >= 45:
    print("medium")
elif bmi >= 22.0 and age >= 45:
    print("high")
elif bmi < 22.0 and age < 45:
    print("low")
