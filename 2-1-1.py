x,y = eval(input("Please enter the x and y coordinates:"))
if x > 0 and y >0:
    print("({:1},{:2}) 坐标位于第一象限".format(x,y))
elif x < 0 and y > 0:
    print("({:1},{:2}) 坐标位于第二象限".format(x,y))
elif x < 0 and y < 0:
    print("({:1},{:2}) 坐标位于第三象限".format(x,y))
elif x>0 and y > 0:
    print("({:1},{:2}) 坐标位于第四象限".format(x,y))
else:
    print("在坐标轴上")
