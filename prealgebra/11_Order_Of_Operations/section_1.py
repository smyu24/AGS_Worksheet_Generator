# NOT REAL

# First Section (ANSWER GENERATION NEED WORK)
import math
import random

from sympy import sympify
import sympy as sp

def division_cleaner(var, primer):
    var = abs(int(var))
    for i in range(1, int(int(var) / 2) + 2):
        if int(var) % i == 0:
            if i not in primer:
                primer.append(i)
            if int(int(var)/i) not in primer:
                primer.append(int(int(var) / i))
    print(var)
    print(primer)
    holder = random.choice(primer[:1])
    print(holder, primer)
    return holder

def Order_Of_Operations_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    calculation = ''
    temp = 0
    all_expressions = ['+', '-', '*', '/', '**']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2, 3]
    negative = ['-', '']
    temp = random.choice(case)
    primer = []
    sym_1 = ''
    sym_2 = ''
    sym_3 = ''
    hold = ''

    print('temp',temp)
    if option_difficulty == "easy":
        if temp == 1:
            a,b,c = str(random.randint(2, 10)), str(random.randint(1, 10)), str(random.randint(1, 10))
            sym_1 = str(random.choice(addition_expression))

            answerset.append(sympify(a + "*" + "(" + b + sym_1 + c + ")"))
            problemsets.append(a + "*" + "(" + b + sym_1 + c + ")")
        
        elif temp == 2:
            a,b,c = str(random.randint(1, 10)), str(random.randint(2, 10)), str(random.randint(1, 10))
            sym_1 = str(random.choice(mult_expression))
            sym_2 = str(random.choice(addition_expression))
        
            if sym_1 == '/':
                a = division_cleaner(b, primer) * random.randint(3, 6)
            
            answerset.append(sympify(str(a) + sym_1 + b + sym_2 + c))
            problemsets.append(str(a) + sym_1 + b + sym_2 + c)
        
        elif temp == 3:
            a,b,c = str(random.randint(1, 10)), str(random.randint(2, 10)), str(random.randint(2, 10))
            sym_1 = str(random.choice(mult_expression))
            calculation = int(a) * int(b)
            if sym_1 == '/':
                c = division_cleaner(calculation, primer) * random.randint(2, 6)
            
            answerset.append(sympify(a + "*" + b + sym_1 + str(c)))
            problemsets.append(a + "*" + b + sym_1 + str(c))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif option_difficulty == "medium":
        if temp == 1:
            a,b,c,d = str(random.randint(2, 10)), str(random.randint(1, 10)), str(random.randint(2, 10)), str(random.randint(2, 10))
            sym_1 = str(random.choice(addition_expression))
            sym_2 = str(random.choice(mult_expression))
            
            if sym_2 == '/':
                d = division_cleaner(c, primer) * random.randint(3, 6)
            
            answerset.append(sympify(a + "*" + "(" + b + sym_1 + c + sym_2 + str(d) + ")"))
            problemsets.append(a + "*" + "(" + b + sym_1 + c + sym_2 + str(d) + ")")

        elif temp == 2:
            a,b,c,d = str(str(random.choice(negative)) + str(random.randint(2, 5))), str(random.randint(1, 10)), str(random.randint(1, 10)), str(random.randint(1, 5))
            sym_1 = str(random.choice(addition_expression))

            answerset.append(sympify(a + "*" + "(" + b + sym_1 + c + ")" + "**" + d))
            problemsets.append(a + "*" + "(" + b + sym_1 + c + ")" + "**" + d)
        
        elif temp == 3:
            a,b,c = str(str(random.choice(negative)) + str(random.randint(1, 10))), str(random.randint(1, 10)), str(random.randint(1, 5))
            sym_1 = str(random.choice(addition_expression)) #division_cleaner(calculation, primer) * random.randint(2, 6)

            answerset.append(sympify(a + sym_1 + b + "**" + c))
            problemsets.append(a + sym_1 + b + "**" + c)

    elif option_difficulty == "hard":
        if temp == 1:
            a,b,c,d = str(random.randint(9, 27)), str(random.randint(7, 25)), str(random.randint(2, 5)), str(random.randint(2, 10))
            sym_1 = str(random.choice(addition_expression)) #division_cleaner(calculation, primer) * random.randint(2, 6)
            sym_2 = str(random.choice(mult_expression))
            sym_3 = str(random.choice(addition_expression))

            if sym_2 == '/':
                c = division_cleaner(abs(sympify(a + sym_1 + b)), primer) * random.randint(3, 8)
            
            answerset.append(sympify("(" + a + sym_1 + b + ")" + sym_2 + str(c) + sym_3 + d))
            problemsets.append("(" + a + sym_1 + b + ")" + sym_2 + str(c) + sym_3 + d)
        elif temp == 2:
            a,b,c,d = str(random.choice(negative)) + str(random.randint(2, 10)), str(random.randint(7, 25)), str(random.randint(7, 25)), str(random.randint(2, 5))
            sym_1 = str(random.choice(addition_expression)) #division_cleaner(calculation, primer) * random.randint(2, 6)
            sym_2 = str(random.choice(mult_expression))

            problemsets.append(a + "*" + "(" + b + sym_1 + c + ")" + sym_2 + d)
            answerset.append(sympify(a + "*" + "(" + b + sym_1 + c + ")" + sym_2 + d))
        elif temp == 3:
            a,b,c,d = str(random.randint(7, 25)), str(random.randint(7, 25)), str(random.randint(7, 25)), str(random.randint(2, 5))
            sym_1 = str(random.choice(addition_expression)) #division_cleaner(calculation, primer) * random.randint(2, 6)
            sym_2 = str(random.choice(addition_expression))
            sym_3 = str(random.choice(mult_expression))
            hold = str(random.choice(negative))
            problemsets.append(hold + "(" + a + sym_1 + "(" + b + sym_2 + c + ")" + ")" + sym_3 + d)
            answerset.append(sympify(hold + "(" + a + sym_1 + "(" + b + sym_2 + c + ")" + ")" + sym_3 + d))

    return(problemsets, answerset)

print("EASY!!!\n\n")
for i in range(20):
    a, b = Order_Of_Operations_1("easy", False)
    print(a, b)
print("MEDIUM!!!\n\n")
for i in range(20):
    a, b = Order_Of_Operations_1("medium", False)
    print(a, b)
print("HARD!!!\n\n")
for i in range(20):
    a, b = Order_Of_Operations_1("hard", False)
    print(a, b)