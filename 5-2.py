class Rectangle:
    def __init__(self,li):
        self.__x = li[0]
        self.__y = li[1]
        self.__length = li[2]
        self.__width = li[3]
    def changePos(self,x,y):
        self.__x = x
        self.__y = y
        print('移动后位置为：({},{})'.format(self.__x,self.__y))
    def enlarge(self,num):
        self.__length *= num
        self.__width *= num
        print('放大两倍后长宽分别为：'+'('+str(self.__length)+','+str(self.__width)+')')
    def show(self):
        print('位置：('+str(self.__x)+','+str(self.__y)+')')
        print('长宽分别为：'+str(self.__length)+' '+str(self.__width))
if __name__ =='__main__':
    a = Rectangle(list(eval(input())))
    a.show()
    a.changePos(50,70)
    a.enlarge(2)
    
