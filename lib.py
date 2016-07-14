# This file contains important formulas
from data_processing import *
import yaml

with open("param.yaml", 'r') as f:
	doc = yaml.load(f)

def get_param():
	return doc["param"]


def score_formula(var):
	"""
	Return the value of the function for var, which is a list of variables
	The parameter and the degree of each variable is get from param.yaml
	var (variable orders): 
		percentage_seen_mess(OA, user)
		percentage_clicked_mess(OA, user) 
		no_seen_mess(OA, user)
		get_no_clicked_mess(OA, user):
		other variables
	"""
	score = 0
	it = 0

	for (pwr, par) in get_param():
		score += par * var[it]^pwr 
		it += 1

	return score

print score_formula([1,2,3,4,5])