import re
from wordInput import openWord, addEquation, addLine, nextpage
from ramdonQuestion import index_question
def bracket_rule(question):
	bracket = re.compile(r'\(.+?\)\^-?\d+|[a-z]\^?-?\d*')
	index = re.compile(r'[a-z]\^?-?\d*')
	question = ("(b^-3c^2)^2e/a^3^3")
	bracket_index = bracket.findall(question)
	if '/' in bracket_index[0]:
		inside = question[question.index('(')+1:question.index(')')]
		seperate = inside.split('/')
		fraction_rule = '({0})^{2}/({1})^{2}'.format(seperate[0], seperate[1], question[question.rindex('^')+1:])

		print(fraction_rule)
def bracket_handle(step2):
	bracket = re.compile(r'\(.+?\)\^-?\d+')
	index = re.compile(r'[a-z]\^?-?\d*')
	bracket_collect = []
	start_remain = 0
	breaking_bracket  = ''
	present = ''
	if bracket.match(step2):
		for b in bracket.finditer(step2):
			new_string = ''
			ans_present = ''
			intermediate = b.group(0)
	#for present in word
			outside_power_string = intermediate[intermediate.rindex('^')+1:]
			if outside_power_string[0] == '-':
				outside_power_string = '(' + outside_power_string + ')'
			outside_power = int(intermediate[intermediate.rindex('^')+1:])
			index_in_bracket = index.findall(intermediate)
			for i in index_in_bracket:
				if len(i) == 1:
					new_string = new_string + i + '^' + str(outside_power) + ' '
					ans_present = ans_present + i + '^' + outside_power_string  + ' '
				else:
					new_string = new_string + i[0:2] + str(int(i[2:]) * outside_power) + ' '
					if i[2] == '-':
						ans_present = ans_present + i[0:2] + '((' + i[2:] + ')x' + outside_power_string +') ' 
					else:
						ans_present = ans_present + i[0:2] + '(' + i[2:] + 'x' + outside_power_string +') ' 
			
			bracket_collect.append([start_remain, b.start(), new_string, ans_present])
			start_remain = b.end()

		for v in bracket_collect:
			breaking_bracket = breaking_bracket + step2[v[0]:v[1]] + v[2]
			present = present + step2[v[0]:v[1]] + v[3]
		print(present)
		addEquation('=' + present, 0.6)
		print(breaking_bracket)
		addEquation('=' + breaking_bracket, 0.6)
	else:
 		breaking_bracket = step2
	return breaking_bracket

def collect_term(question):
	#define expression of index form
	index = re.compile(r'[a-z]\^?-?\d*')
	denominator = []
#for denominator that dont need to caculate
	denominator_keep = {}
	if '/' in question:
		fraction = question.split('/')
		denominator = index.findall(fraction[1])
	else:
		fraction = [question]
	nominator = index.findall(fraction[0])
	#check 0 power
	check0 = 0
	division_rule = 0
	drule_string = '  (a^m /a^n   = a^(m-n) )'
	mutiple_rule = 0
	mrule_string = '  (a^m a^n  =  a^(m+n) )'
	ans = {}
	ans_present = {}

	if nominator:
		for n in nominator:
			if n[0] not in ans.keys():
				if len(n) == 1:
					ans[n] = 1
					ans_present[n] = '(1)'
				else:
					ans[n[0]] = int(n[2:])
					ans_present[n[0]] = '(' + n[2:] + ')'
			else:
				mutiple_rule = 1
				if len(n) == 1:
					ans[n] = ans[n] + 1
					ans_present[n] = ans_present[n][0:-1] + '+1' + ')'
				else:
					ans[n[0]] = ans[n[0]] + int(n[2:])
					if n[2] == '-':
						ans_present[n[0]] = ans_present[n[0]][0:-1] + '+(' + n[2:] +')' + ')'
					else:
						ans_present[n[0]] = ans_present[n[0]][0:-1] + '+' + n[2:] + ')'

	if denominator:
		for n in denominator:
			if n[0] not in ans.keys():
				if n[0] not in denominator_keep.keys():
					if len(n) == 1:
						denominator_keep[n] = '1'
					else:
						if n[2] != '-':
							denominator_keep[n[0]] = n[2:]
						else:
							division_rule = 1
							ans[n[0]] = -int(n[2:])
							ans_present[n[0]] = '(0-(' + n[2:] + '))'
				else:
					division_rule = 1
					if len(n) == 1:
						ans[n] = -int(denominator_keep[n]) - 1
						ans_present[n] = '(0-' + denominator_keep[n]  + '-1)'
						del denominator_keep[n]
					else:
						if n[2] != '-':
							ans[n[0]] = -int(denominator_keep[n[0]]) - int(n[2:])
							ans_present[n[0]] = '(0-' + denominator_keep[n[0]]  + '-' +n[2:] + ')'
							del denominator_keep[n[0]] 
						else:
							ans[n[0]] = int(denominator_keep[n[0]]) -int(n[2:])
							ans_present[n[0]] = '(0-' + denominator_keep[n[0]] + '-(' + n[2:] + '))'
							del denominator_keep[n[0]]

			else:
				division_rule = 1
				if len(n) == 1:
					ans[n] = ans[n] - 1
					ans_present[n] = ans_present[n][0:-1] + '-1' + ')'
				else:
					ans[n[0]] = ans[n[0]] - int(n[2:])
					if n[2] == '-':
						ans_present[n[0]] = ans_present[n[0]][0:-1] + '-(' + n[2:] +')' + ')'
					else:
						ans_present[n[0]] = ans_present[n[0]][0:-1] + '-' + n[2:] + ')'

	denominator_keep_string = '(' + ' '.join('^'.join((key,val)) if val != '1' else key for (key,val) in denominator_keep.items()) + ')'
	if division_rule == 1 and mutiple_rule ==1:
		rule_string = mrule_string + drule_string
	elif division_rule == 1:
		rule_string = drule_string
	elif mutiple_rule == 1:
		rule_string = mrule_string
	else:
		rule_string = ''
	if len(denominator_keep_string) != 2:
		present = '(' + ' '.join('^'.join((key,val)) for (key,val) in ans_present.items()) + ')/' + denominator_keep_string + rule_string
	else:
		present = ' '.join('^'.join((key,val)) for (key,val) in ans_present.items()) + rule_string

	print(present)
	addEquation('=' + present, 0.6)
	for k, v in ans.items():
		if v == 0:
			check0 = 1
			del ans_present[k]
			continue
		if v == 1:
			ans_present[k] = k
		else:
			ans_present[k] = k + '^' + str(v)
	if  len(denominator_keep_string) != 2:
		if check0 == 1 and len(ans_present) == 0:
			present = '1' + '/' + denominator_keep_string + '  (a^0 = 1)'
		elif check0 == 1:
			present = '(' + ' '.join(val for val in ans_present.values()) + ')/' + denominator_keep_string + '  (a^0 = 1)'
		else:
			present = '(' + ' '.join(val for val in ans_present.values()) + ')/' + denominator_keep_string
	else:
		if check0 == 1 and len(ans_present) == 0:
			present = '1' + '  (a^0 = 1)'
		elif check0 == 1:
			present = ' '.join(val for val in ans_present.values()) +  '  (a^0 = 1)'
		else:
			present = ' '.join(val for val in ans_present.values())
	print(present)
	addEquation('=' + present, 0.6)
	return ans, denominator_keep_string

def positive_index(step, denominator_keep):
	ans_string = ''
	ans_nominator = {}
	ans_denominator = {}
#classify nominaort and denominator by the negative sign of power
	for k, v in step.items():
		if v < 0:
			ans_denominator[k] = -v
		else:
			ans_nominator[k] = v
#transform dictionaries to strings
	nominator_string = collect_strings(ans_nominator)
	denominator_string = collect_strings(ans_denominator)
	if len(denominator_keep) != 2:
		if nominator_string == None and denominator_string == None:
			ans_string = '1/' + denominator_keep
		elif denominator_string == None:
			ans_string = nominator_string +'/'+ denominator_keep
		elif nominator_string == None:
			ans_string = '1/(' + denominator_string + denominator_keep[1:]
			present = ans_string  + '  (a^-n = 1/a^n )'
			print(present)
			addEquation('=' + present, 0.6)
		else:
			ans_string = nominator_string + '/(' + denominator_string + denominator_keep[1:]
			present = ans_string + '  (a^-n = 1/a^n )'
			print(present)
			addEquation('=' + present, 0.6)

	else:
		if nominator_string == None and denominator_string == None:
			ans_string = '1'
		elif denominator_string == None:
			ans_string = nominator_string
		elif nominator_string == None:
			ans_string = '1/' + denominator_string
			present = ans_string + '  (a^-n = 1/a^n )'
			print(present)
			addEquation('=' + present, 0.6)
		else:
			ans_string = nominator_string + '/' + denominator_string
			present = ans_string + '  (a^-n = 1/a^n )'
			print(present)
			addEquation('=' + present, 0.6)
	return ans_string

def collect_strings(step):
	collect_string = ""
	for k, v in step.items():
		if v == 0:
			continue
		elif v == 1:
			collect_string = collect_string + k
		else:
			collect_string = collect_string + k + '^' + str(v) + ' '
	if len(collect_string) == 0:
		return None
	return collect_string


openWord()
question_bank = {}
for i in range(1, 3):
	question = index_question()
	# question = '(ab)^2/c(a^2 b^-3)^-3'
	addEquation(str(i) + '..' + question, 0.6)
	ans, denominator_keep = collect_term(bracket_handle(question))
	answer = positive_index(ans, denominator_keep)
	addLine()
	question_bank[str(i) + '..' + question] = str(i) + '..' + answer

nextpage()
for q in question_bank.keys():
	addEquation(q, 0.2)
nextpage()
for a in question_bank.values():
	addEquation(a, 0.2)
