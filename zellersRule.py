#zellers rule day calculation

class Zeller_s_Rule:
    def __init__(self):
        self.day = None
        self.month = None
        self.year = None
        self.month_zeller = None
        self.year_zeller = None

    def set_date(self, day_:int , month_:int, year_:int):
        self.day = day_
        self.month = month_
        self.year = year_
        self.month_zeller = self.month
        self.year_zeller = self.year

    def get_date(self):
        return self.day, self.month, self.year

    def calculate_Day(self):
        if self.month < 3:
            self.year_zeller -= 1
        
        self.month_zeller = (self.month - 2) % 12

        if self.month_zeller == 0:
            self.month_zeller = 12

        C = int (self.year_zeller / 100)
        Y = int (self.year_zeller % 100)
        M = int (self.month_zeller)
        D = int (self.day)

        F = (D + int (((13* M)-1)/5) + Y + int (C / 4) + int (Y / 4) - 2 * C) % 7

        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        return week_days[F]


zeller = Zeller_s_Rule()
zeller.set_date(1,1,2000)
print(zeller.calculate_Day())