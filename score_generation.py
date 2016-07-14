# This program inputs users' data and generates interaction score 
# for each pair (user, OA) 
from lib import *
from data_processing import *

def score(user, OA):

	list_of_var = [get_percentage_seen_mess(OA, user), get_percentage_clicked_mess(OA, user) 
	get_no_seen_mess(OA, user), get_no_clicked_mess(OA, user)]
	other variables
	return 