
def currently_infected_cases(reported_cases, multiplier):
	currently_infected = reported_cases * multiplier
	return currently_infected

def infections_by_requested_time(currently_infected, days):
	infections_per_time = currently_infected * (2 ** int(days/3))
	return infections_per_time

def severe_infected_cases(currently_infected, multiplier_factor):
	severe_case = currently_infected * multiplier_factor
	return severe_case


def daily_impact(period_type, time_to_elapse):
	Days = "Days"
	Weeks = "Weeks"
	Months = "Months"
	days = 0 
	if period_type == Days:
		days = time_to_elapse
	elif period_type == Weeks:
		days = 7 * time_to_elapse
	elif period_type == Months:
		days = 30 * time_to_elapse
	else:
		return days









