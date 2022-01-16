from flask import Flask
from flask import request
import re

app = Flask(__name__)

@app.route("/")
def index():
    question = request.args.get("celsius", "")
    ans = run(question)
    return (
        """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
            </form>"""
        + "the simplyfied form of " + question + " is "
        + ans
    )


def indexWithFraction(question):
    fraction = question.split('/')
    nominator = sorted(index.findall(fraction[0]))
    denominator = sorted(index.findall(fraction[1]))
    nominator_left = nominator.copy()
    denominator_left = denominator.copy()
    for n in nominator:
        for d in denominator:
            if n[0] == d[0]:
                if len(n) == 1:
                    upper = 1
                else:
                    upper = int(n[2:])
                if len(d) == 1:
                    lower = 1
                else:
                    lower = int(d[2:])

                index_rule = upper - lower
                ans.append(n[0] + '^' + str(index_rule))
                nominator_left.remove(n)
                denominator_left.remove(d)
    for n in nominator_left:
        ans.append(n)
    for d in denominator_left:
        if len(d) == 1:
            reverse = -1
        else:
            reverse  = -int(d[2:])
        ans.append(d[0] + '^' + str(reverse))

def indexWithoutFraction(question):
    nominator = sorted(index.findall(question))
    for n in nominator:
        ans.append(n)

def expressPositiveIndex():
    ans_nominator = []
    ans_denominator = []
    for m in ans:
        if len(m) == 1:
            continue
        if m[2] == '-':
            if m[3:] == '1':
                ans_denominator.append(m[0])
            else:
                ans_denominator.append(m[0:2] + m[3:])
        else:
            if m[2:] == '1':
                ans_nominator.append(m[0])
            else:
                ans_nominator.append(m)
    if len(ans_nominator) != 0 and len(ans_denominator) != 0:
        finalAns = ('').join(ans_nominator) + '/' + ('').join(ans_denominator)
    elif len(ans_nominator) == 0:
        finalAns =  '1/' + ('').join(ans_denominator)
    else:
        finalAns =  ('').join(ans_nominator)
    return finalAns

def run(question):
    global ans, index
    ans = []
    index = re.compile(r'[a-z]\^?-?\d*')
    if '/' in question:
        indexWithFraction(question)
    else:
        indexWithoutFraction(question)
    return expressPositiveIndex()
    
if __name__ == '__main__':
    app.run()