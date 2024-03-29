# absolute path of the parent directory to the sys.path

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import signify, GeoSeq, ArithSeq, latexify
from sympy import Rational
from random import randint

def getSeqAnswer(seq, prob='common', blanks=False, expr="latex", numTerms=6):
    if expr=="latex":
        answer = ''
        if prob in ['common','all'] :
            answer += '$d = ' if type(seq)==ArithSeq else '$r = '
            answer += latexify(seq.common, seq.precision) + '$'
        if prob in ['explicit','all']:
            if len(answer)>0:
                answer += r' \newline '
            answer += '$' + seq.getExplicit() + r' \quad\text{or}\quad ' + seq.getExplicit(0) + '$'
        if prob in ['recursive','all']:
            if len(answer)>0:
                answer += r' \newline '
            answer += '$' + seq.getRecursive() + r' \quad\text{or}\quad ' + seq.getRecursive(0) + '$'
        
        if blanks:
            if len(answer)>0:
                answer += r' \newline '
            answer += signify(seq.getSeqStr(range(1,numTerms+1))) 
    else:
        seq.getTerms(numTerms)
        answer = seq

    return answer

#section 1
def Geometric_Sequence_Problem(difficulty=1, prob='common', blanks=False, expr="latex"):
    if difficulty == 1: # easy
        if randint(0,1):
            geo = GeoSeq(randint(1,10), [1,randint(1,10)])
        else:
            geo = GeoSeq(randint(-10,-1), [1,randint(-10,-1)])
    
    elif difficulty == 2: # medium
        ratio = Rational(randint(1,7),randint(2,7))
        power = randint(2,9 - ratio.q)
        start = ratio.p*ratio.q**power
        if randint(0,1):
            geo = GeoSeq(ratio, [1,start])
        else:
            geo = GeoSeq(-ratio, [1,start])

    elif difficulty == 3: # hard
        if randint(0,1):
            geo = GeoSeq(Rational(randint(1,5),randint(2,5)), [1,Rational(randint(1,7),randint(2,7))])
        else:
            geo = GeoSeq(Rational(randint(-5,-1),randint(2,5)), [1,Rational(randint(1,7),randint(2,7))])
    
    nums = [1,2,'','','',''] if blanks else [1,2,3,4,5]
    problem = signify(geo.getSeqStr(nums))
    answer = getSeqAnswer(geo, prob, blanks, expr)
            
    return problem, answer

# for i in range(10):
#     problem, answer = Geometric_Sequence_Problem(2, 'common')
#     print(problem, r'\\')
#     print(answer, r'\\ \\')

# #section 2
# for i in range(10):
#     problem, answer = Geometric_Sequence_Problem(2, 'recursive')
#     print(problem, r'\\')
#     print(answer, r'\\ \\')

# #section 3
# for i in range(10):
#     problem, answer = Geometric_Sequence_Problem(2, 'explicit', blanks=True)
#     print(problem, r'\\')
#     print(answer, r'\\ \\')