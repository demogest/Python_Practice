class Circle:
    def __init__(self, radius: int, center: list):
        self.__radius, self.__center = radius, center

    def getRadius(self) -> int:
        return self.__radius

    def getCenter(self) -> list:
        return self.__center


class Rectangle:
    def __init__(self, pos: list):
        self.__pos = pos

    def getPos(self) -> list:
        return self.__pos


def rect_in_circle(a: Circle, b: Rectangle) -> bool:
    # 计算矩形中心点
    bPos = b.getPos()
    # [(bPos[0][0] + bPos[1][0])/2,(bPos[0][1] + bPos[1][1])/2]
    b_c = list(map(lambda x: (x[0] + x[1]) / 2, zip(bPos[0], bPos[1])))
    # 平移矩形到坐标系原点, 记录矩形中心与右上顶点构成的向量OA
    OA = list(map(lambda x: x[0] - x[1], zip(bPos[1], b_c)))
    # 平移矩形的时候, 平移圆
    # 通过对称, 将圆心放到第一象限
    # 记录坐标原点到圆心的向量 OB
    OB = list(map(abs, list(map(lambda x: x[0] - x[1], zip(a.getCenter(), b_c)))))
    # 计算向量AB:
    AB = list(map(lambda x: x[0] - x[1], zip(OB, OA)))  # AB = [OB[0] - OA[0], OB[1] - OA[1]]
    # 计算向量AC, C是将AB中的负值置0
    AC = [max(0, i) for i in AB]  # AC = [max(0, AB[0]), max(0, AB[1])]
    return AC[0] ** 2 + AC[1] ** 2 <= a.getRadius() ** 2


if __name__ == '__main__':
    cirRadi = int(input('Please enter the radius:'))
    cirCen = list(map(int, list(input('Please enter the Center coordinates').split(' '))))
    cir = Circle(cirRadi, cirCen)
    recCoord = list(map(int, list(input('Please input the coordinate(LD,RU):').split(' '))))
    recCoord = [recCoord[i:i + 2] for i in range(0, len(recCoord), 2)]
    rec = Rectangle(recCoord)
    if rect_in_circle(cir, rec):
        print('Overlap')
        exit(0)
    print('Non-Overlap')
    exit(0)
