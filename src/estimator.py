from src.my_funcs import *



def estimator(data):

	impact = dict()
	severeImpact = dict()

	days = daily_impact(data["period_type"], data["time_to_elapse"])

	impact["currently_infected"] = currently_infected_cases(data["reported_cases"], data["multiplier"])

	impact["infectionsByRequestedTime"] = infections_by_requested_time(data["currently_infected"], days)

	severeImpact["currentlyInfected"] = severe_infected_cases(data["currently_infected"], data																										["multiplier_factor"])

	severeImpact["infectionsByRequestedTime"] = severe_infected_cases(data["currently_infected"], data																										["multiplier_factor"])


	response =  { 
			data: data,          # the input data you got
			impact: impact,        // your best case estimation
			severeImpact: severeImpact   // your severe case estimation
		}


	return response
