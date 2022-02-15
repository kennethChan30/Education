import re

def collect_term(question):
    #define expression of index form
    index = re.compile(r'[a-z]\^?-?\d*')
    nominator = index.findall(question)
    ans = {}
    for n in nominator:
        if n[0] not in ans.keys():
            if len(n) == 1:
                ans[n] = 1
            else:
                ans[n[0]] = int(n[2:])
        else:
            if len(n) == 1:
                ans[n] = ans[n] + 1
            else:
                ans[n[0]] = ans[n[0]] + int(n[2:])
    return ans

def positive_index(step):
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
            collect_string = collect_string + k + ' '
        else:
            collect_string = collect_string + k + '^' + str(v) + ' '
    if len(collect_string) == 0:
        return None
    return collect_string
def simplify_index(question):
    return positive_index(collect_term(question))