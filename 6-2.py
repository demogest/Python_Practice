class Clock:
    def __init__(self, time=None):
        if time is None:
            time = [0, 0, 0]
        self.__time = time

    def getData(self):
        return self.__time

    def __repr__(self):
        return 'It is {0[0]}:{0[1]}:{0[2]} now'.format(self.__time)

    def setTime(self, time: list):
        self.__time = time

    def passTimeT(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.__time[2] += second
        self.__time[1] += self.__time[2] // 60 + minute
        self.__time[0] += self.__time[1] // 60 + hour
        tmp = self.__time[0] // 24
        self.__time[0] %= 24
        self.__time[1:] = list(map(lambda x: x % 60, self.__time[1:]))
        return tmp


# 未考虑大小月
class Calender:
    def __init__(self, date: list = None):
        if date is None:
            date = [1970, 1, 1]
        self.__date = date

    def getData(self):
        return self.__date

    def setDate(self, date: list):
        self.__date = date

    def __repr__(self):
        return "It is {0[0]}.{0[1]}.{0[2]}" \
            .format(self.__date)

    def passTimeD(self, year: int = 0, month: int = 0, day: int = 0):
        self.__date[2] += day
        self.__date[1] += self.__date[2] // 30 + month
        self.__date[0] += self.__date[1] // 12 + year
        self.__date[2] %= 30
        self.__date[1] %= 12


class CalenderClock(Clock, Calender):
    def __init__(self, time: list = None, date: list = None):
        super().__init__()
        if time is None:
            time = [0, 0, 0]
        if date is None:
            date = [1970, 1, 1]
        self.__time = time
        self.__date = date

    def __repr__(self):
        return "It is {0[0]}.{0[1]}.{0[2]} {1[0]}:{1[1]}:{1[2]} now" \
            .format(self.__date, self.__time)

    def getData(self):
        return self.__date, self.__time

    def setCalender(self, time, date):
        self.__time = time
        self.__date = date

    def passTimeC(self, year, month, day, hour: int = 0, minute: int = 0, second: int = 0):
        time = Clock(self.__time)
        date = Calender(self.__date)
        tmp = time.passTimeT(hour, minute, second)
        date.passTimeD(year, month, day + tmp)
        self.setCalender(time.getData(), date.getData())


a = Clock()
print(a)
h, m, s = map(int, input().split(' '))
a.passTimeT(h, m, s)
print(a)
