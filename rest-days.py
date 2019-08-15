from datetime import date, datetime, timedelta
birth_date = date(1999, 7, 2, 10, 0 ,0)
for days in range(0, 5000):
	print(birth_date - timedelta(days=days+3))
