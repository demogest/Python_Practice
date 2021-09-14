from math import *
if __name__ == '__main__':
    height = float(input("Please input the height:"))
    weight = float(input("Please input the weight:"))
    bmi = weight/(height**2)
    print("Your BMI is:"+str(format(bmi,'.2f')))
    if bmi >= 28:
        print("肥胖")
    elif bmi >=24:
        print("偏胖")
    elif bmi >= 18.5:
        print("正常")
    elif bmi <18.5:
        print("偏瘦")
