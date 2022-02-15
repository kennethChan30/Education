import random

def bracket():
	no_of_index = random.randrange(1,3)
	

def index_formation():
	base = random.choice(['b','k', 'x', 'y', 'z'])
	index = random.randrange(-10, 10)
	if index == 1:
		return base
	elif index == 0:
		return None
	else:
		return  '^'.join((base, str(index))) + ' '
def string_of_index(diff):
	running_no = random.randrange(0, diff)
	q = ''
	check = 0
	if running_no == 0:
		q = '1'
	for i in range(running_no):
		single_index = index_formation()
		if single_index == None:
			check = check + 1
			if check == running_no:
				q = '1'
			continue
		else:
			q = q + single_index
	return q	

def index_question(ndiff = 3, ddiff = 3):
	nominator = string_of_index(ndiff)
	denominator = string_of_index(ddiff)
	if len(denominator) == 1:
		prob = nominator
	else:
		prob = nominator + '/' + denominator

	if prob.count('a') < 2 and prob.count('b') < 2 and prob.count('x') < 2 and prob.count('y') < 2 and prob.count('z') < 2:
		return index_question()
	else:
		return prob


