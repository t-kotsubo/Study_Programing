import datetime

# d = datetime.date.today()
# print(d)
# dt_n = datetime.date.today()
# print(dt_n)
# dt_today = datetime.datetime.today()
# print(dt_today)

# now = datetime.datetime.now()
# dt_d = datetime.datetime.strptime(now, "%Y-%m-%d-%H-%M-%S")
# print(dt_d)
# dt_s = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
# print(dt_s)
# dt_d = datetime.datetime.strptime(dt_s, "%Y-%m-%d %H:%M:%S")
# print(dt_d)

birthday = datetime.date(2019, 7, 21)
# birthday = datetime.date(2019, 7, 21)
# new_year_day = datetime.date(2020, 1, 1)
# print(new_year_day - birthday)

print(birthday + datetime.timedelta(5))

# print(birthday)

# today = datetime.datetime.today()

# print(today-birthday)