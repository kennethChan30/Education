import re

def collect_term(question):
    #define expression of index form
    index = re.compile(r'[a-z]\^?-?\d*')
    #seperate each index
    nominator = sorted(index.findall(question))
    #collec the same term of expression using dictonary
    ans = {}
    #the ouput text
    ans_string = ""
    #loop all index
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
    #produce print answers
    for k, v in ans.items():
        if v == 1:
            ans_string = ans_string + k
        else:
            ans_string = ans_string + k + '^' + str(v)
    return ans_string

def simplify_index(question):
    return collect_term(question)