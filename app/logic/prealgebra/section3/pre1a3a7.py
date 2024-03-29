# First Section

import math
import random

def Dividing_Integers_1(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = []
    to_be_prime = 0
    holder = []
    negative = [1, -1]
    temp = []
    list_holder = []

    if(localmin == localmax):
        if option_difficulty == 1: # Pure positive integers
            to_be_prime = random.randint(2, 10)

        elif option_difficulty == 2: # Mix of positive and negetives
            to_be_prime = random.randint(10, 20)

        elif option_difficulty == 3: # All previous options + higher number threshold
            to_be_prime = random.randint(15, 30)
    else:
        to_be_prime = random.randint(localmin, localmax)

    # answer generation...
    for i in range(1, int(to_be_prime / 2) + 1):
        if to_be_prime % i == 0:
            if i not in temp:
                temp.append(i)
            if int(to_be_prime/i) not in temp:
                temp.append(int(to_be_prime / i))

    holder = random.choice(temp[1:])
    if option_difficulty == 1:
        list_holder.append(random.choice(negative) * (holder * random.randint(2, 10)))
        list_holder.append(random.choice(negative) * holder)

    elif option_difficulty == 2:
        list_holder.append(random.choice(negative) * (holder * random.randint(5, 15)))
        list_holder.append(random.choice(negative) * holder)

    elif option_difficulty == 3:
        list_holder.append(random.choice(negative) * (holder * random.randint(10, 15)))
        list_holder.append(random.choice(negative) * holder)
    
    problemsets = str(list_holder[0]) + r" \div " + str(list_holder[1]) # "latexified"

    answerset.append(int(list_holder[0]/list_holder[1]))

    return(str(problemsets), str(answerset)) # $6 \div 3 = 2$

def Dividing_Integers_2(option_difficulty, option_random, localmin, localmax):
    problemsets = ""
    answerset = []
    to_be_prime = 0
    holder = []
    negative = [1, -1]
    temp = []
    list_holder = []
    
    if(localmin == localmax):
        if option_difficulty == 1: # Pure positive integers
            to_be_prime = random.randint(2, 10)

        elif option_difficulty == 2: # Mix of positive and negetives
            to_be_prime = random.randint(10, 20)

        elif option_difficulty == 3: # All previous options + higher number threshold
            to_be_prime = random.randint(15, 30)
    else:
        to_be_prime = random.randint(localmin, localmax)

    # answer generation...
    for i in range(1, int(to_be_prime / 2) + 1):
        if to_be_prime % i == 0:
            if i not in temp:
                temp.append(i)
            if int(to_be_prime/i) not in temp:
                temp.append(int(to_be_prime / i))

    holder = random.choice(temp[1:])

    if option_difficulty == 1:
        list_holder.append(random.choice(negative) * (holder * random.randint(2, 10)))
        list_holder.append(random.choice(negative) * holder)

    elif option_difficulty == 2:
        list_holder.append(random.choice(negative) * (holder * random.randint(5, 15)))
        list_holder.append(random.choice(negative) * holder)

    elif option_difficulty == 3:
        list_holder.append(random.choice(negative) * (holder * random.randint(10, 15)))
        list_holder.append(random.choice(negative) * holder)
    
    problemsets=r"\frac{" + str(list_holder[0]) + "}{" + str(list_holder[1]) + "}" # "latexified"
    answerset.append(int(list_holder[0]/list_holder[1]))

    return(problemsets, answerset) 