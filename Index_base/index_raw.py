import re
from wordInput import openWord, addEquation, addLine, nextpage
from ramdonQuestion import index_question


def bracket_handle(step2):
	bracket = re.compile(r'\(.+?\)\^-?\d+')
	index = re.compile(r'[a-z]\^?-?\d*')
	bracket_collect = []
	start_remain = 0
	breaking_bracket  = ''
	if bracket.match(step2):
		for b in bracket.finditer(step2):
			new_string = ''
			intermediate = b.group(0)
			outside_power = int(intermediate[intermediate.rindex('^')+1:])
			index_in_bracket = index.findall(intermediate)
			for i in index_in_bracket:
				if len(i) == 1:
					new_string = new_string + i + '^' + str(outside_power)
				else:
					new_string = new_string + i[0:2] + str(int(i[2:]) * outside_power)
			bracket_collect.append([start_remain, b.start(), new_string])
			start_remain = b.end()

		for v in bracket_collect:
			breaking_bracket = breaking_bracket + step2[v[0]:v[1]] + v[2]
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
	ans = {}
	if nominator:
		for n in nominator:
			if n[0] not in ans.keys():
				if len(n) == 1:
					ans[n] = 1
				else:
					ans[n[0]] = int(n[2:])
			else:
				mutiple_rule = 1
				if len(n) == 1:
					ans[n] = ans[n] + 1
				else:
					ans[n[0]] = ans[n[0]] + int(n[2:])

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
							ans[n[0]] = -int(n[2:])
				else:
					if len(n) == 1:
						ans[n] = -int(denominator_keep[n]) - 1
						del denominator_keep[n]
					else:
						if n[2] != '-':
							ans[n[0]] = -int(denominator_keep[n[0]]) - int(n[2:])
							del denominator_keep[n[0]] 
						else:
							ans[n[0]] = int(denominator_keep[n[0]]) -int(n[2:])
							del denominator_keep[n[0]]

			else:
				if len(n) == 1:
					ans[n] = ans[n] - 1
				else:
					ans[n[0]] = ans[n[0]] - int(n[2:])

	denominator_keep_string = '(' + ' '.join('^'.join((key,val)) if val != '1' else key for (key,val) in denominator_keep.items()) + ')'

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
		else:
			ans_string = nominator_string + '/(' + denominator_string + denominator_keep[1:]


	else:
		if nominator_string == None and denominator_string == None:
			ans_string = '1'
		elif denominator_string == None:
			ans_string = nominator_string
		elif nominator_string == None:
			ans_string = '1/' + denominator_string
		else:
			ans_string = nominator_string + '/' + denominator_string
		
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

question = '(ab)^2/(a^2b^-3)^-3'
ans, denominator_keep = collect_term(bracket_handle(question))
print(positive_index(ans, denominator_keep))
# bracket_handle(question)
# print(question[0:0])
