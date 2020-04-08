name = "Africa"
avg_age = 19.7
avg_daily_income_in_USD = 5
avg_daily_income_population = 0.71
period_type = "days"
Time_to_Elapse =  58
reported_cases = 674
population = 66622705
total_hospital_beds = 1380614

data = []		#input data
impact = []		#mild case scenario
severe_impact = []		#severe case scenario

def infections_by_requested_time():
	currently_infected = reported_cases * 10
	daily_impact_cases = currently_infected * 30
	impact.append(daily_impact_cases)
	print(impact)

	severe_case = reported_cases * 50 
	daily_severe_case = severe_case * (2**10)
	severe_impact.append(daily_severe_case)
	print(severe_impact)
infections_by_requested_time()




