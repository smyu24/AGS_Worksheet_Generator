import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from loader import LinFunc, getInt, x, QuadFunc, ExpFunc, PWFunc, graphPW, ArithSeq, GeoSeq
from sympy import *
from random import randint

# AGS1.4.1.1 - Solve Each Equation And Check Steps.
# Option : Simple
# instruction : For each of the equations provided below, identify the first operation performed on the variable and also identify the last operation performed on the variable. Then, determine the first step that would take place when solving and the last step that would take place when solving. If needed, solve and check your solution.

# NOT FINISHED; MIGHT NOT NEED THIS TOPIC/LESSSON