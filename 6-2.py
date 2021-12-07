import time,sys
class Clock:
    def __init__(self, time: list = None):
        if time is None:
            time = [0, 0, 0]
        self.__time = time

    def getData(self):
        return self.__time

    def __repr__(self):
        return 'It is {0[0]:^2d}:{0[1]:^2d}:{0[2]:^2d} now'.format(self.__time)

    def setTime(self, time: list = None):
        if time is None:
            time = [0, 0, 0]
        self.__time = [0, 0, 0]
        self.passTimeT(time)

    def passTimeT(self, time: list = None):
        if time is None:
            time = [0, 0, 0]
        hour, minute, second = time[0], time[1], time[2]
        self.__time[2] += second
        self.__time[1] += self.__time[2] // 60 + minute
        self.__time[0] += self.__time[1] // 60 + hour
        tmp = self.__time[0] // 24
        self.__time[0] %= 24
        self.__time[1:] = list(map(lambda x: x % 60, self.__time[1:]))
        return tmp


# 未考虑大小月，是否闰年，统一按一月30天，一年十二月计算，因此存在误差
class Calendar:
    def __init__(self, date: list = None):
        if date is None:
            date = [1970, 1, 1]
        self.__date = date

    def getData(self):
        return self.__date

    def setDate(self, date: list = None):
        if date is None:
            date = [0, 0, 0]
        self.__date = [0, 0, 0]
        self.passTimeD(date)

    def __repr__(self):
        return "It is {0[0]:^4d}.{0[1]:^2d}.{0[2]:^2d}" \
            .format(self.__date)

    def passTimeD(self, date: list = None):
        if date is None:
            date = [0, 0, 0]
        year, month, day = date[0], date[1], date[2]
        self.__date[2] += day
        self.__date[1] += self.__date[2] // 30 + month
        self.__date[0] += self.__date[1] // 12 + year
        self.__date[2] %= 30
        self.__date[1] %= 12


class CalendarClock(Clock, Calendar):
    def __init__(self, time: list = None, date: list = None):
        super().__init__()
        if time is None:
            time = [0, 0, 0]
        if date is None:
            date = [1970, 1, 1]
        self.__time = time
        self.__date = date

    def __repr__(self):
        return "It is {0[0]:^4d}.{0[1]:^2d}.{0[2]:^2d} {1[0]:^2d}:{1[1]:^2d}:{1[2]:^2d} now" \
            .format(self.__date, self.__time)

    def getData(self):
        return self.__date, self.__time

    def setCalender(self, time: list = None, date: list = None):
        if time is None:
            time = [0, 0, 0]
        if date is None:
            date = [0, 0, 0]
        self.__time = [0, 0, 0]
        self.__date = [0, 0, 0]
        self.passTimeC(date, time)

    def passTimeC(self, date: list = None, time: list = None):
        if date is None:
            date = [0, 0, 0]
        if time is None:
            time = [0, 0, 0]
        clo = Clock(self.__time)
        da = Calendar(self.__date)
        date[2] += clo.passTimeT(time)
        da.passTimeD(date)
        self.__time = clo.getData()
        self.__date = da.getData()


if __name__ == '__main__':
    aClock = Clock()
    aCalen = Calendar()
    aCaClo = CalendarClock()
    # while (True):
    #     sys.stdout.write('\r'+str(aClock))
    #     time.sleep(1)
    #     aClock.passTimeT([0, 0, 1])
    # print("{}\n{}\n{}\n".format(aClock, aCalen, aCaClo))
    # aClock.passTimeT(list(map(int, input("Input time to pass(h,minute,s) separated by space:").split(' '))))
    # aCalen.passTimeD(list(map(int, input("Input time to pass(y,month,d) separated by space:").split(' '))))
    # aCaClo.passTimeC(list(map(int, input("Input time to pass(y,month,d) separated by space:").split(' '))),
    #                  list(map(int, input("Input time to pass(h,minute,s) separated by space:").split(' '))))
    # print("{}\n{}\n{}\n".format(aClock, aCalen, aCaClo))
    # aClock.setTime(list(map(int, input("Input time to set(h,minute,s) separated by space:").split(' '))))
    # aCalen.setDate(list(map(int, input("Input time to set(y,month,d) separated by space:").split(' '))))
    # aCaClo.setCalender(list(map(int, input("Input time to set(h,minute,s) separated by space:").split(' '))),
    #                    list(map(int, input("Input time to pass(h,minute,s) separated by space:").split(' '))))
    # print("{}\n{}\n{}\n".format(aClock, aCalen, aCaClo))
