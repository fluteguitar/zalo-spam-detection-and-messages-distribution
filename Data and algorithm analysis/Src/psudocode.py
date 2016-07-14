#intialize values for each pair (OA, user)
def generation():
	for each_oa in OA_list():
		for each_user in users_follow_OA_list():
			calculate score(each_oa, each_user)

#For each OA, sort followed users according to his score
def arrangement():
	for each_oa in OA_list():
		sort_followed_user_by_score()

#For each OA, distribute messges according to sorted list of users
def distribution_messages_for_each_OA(no_mess):
"""
no_mess: int
	The number of messages shot for this OA
"""

def distribution_messages()
	for each_oa in OA_list():
		distribution_messages_for_each_OA()
		