user_id = input("please enter valid id: ")

while len(user_id) != 9 or not user_id.isdigit():
	
	user_id = input("please try again - enter valid value: ")
	
user_id = list(user_id)

	
types = [type(x) for x in user_id]



for i in range(0, len(user_id)):
	user_id[i] = int(user_id[i])



