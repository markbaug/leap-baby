def is_leap_baby(day,month,year):
	if year%400==0:
		if day==29:
			if month==2:
				return True
		else:
			return False
	if year%100==0:
		return False
	if year%4==0:
		if day==29:
			if month==2:
				return True
		else:
			return False
	else:
		return False