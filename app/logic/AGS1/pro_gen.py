from .Unit1.S1_1_1 import Evaluate_Equation_1, Evaluate_Equation_2, Evaluate_Equation_3
from .Unit1.S1_1_2 import Graph_The_Ordered_Pairs
from .Unit1.S1_2_1 import Fill_In_The_Sequence_1, Fill_In_The_Sequence_2, Fill_In_The_Sequence_3
from .Unit1.S1_2_2 import The_Meaning_Of_An_Exponent_1, The_Meaning_Of_An_Exponent_2
from .Unit1.S1_2_3 import Finding_Patterns_In_Geometric_Shapes
from .Unit1.S1_3_1 import Reading_The_Table
from .Unit1.S1_3_2 import Arithmetic_Sequences_1, Arithmetic_Sequences_2, Arithmetic_Sequences_3
from .Unit1.S1_3_3 import Geometric_Sequence_Problem
from .Unit1.S1_3_4 import So_Should_We_Use_Recursive_Or_Explicit
#-----
from .Unit1.S1_4_1 import Arithmetic_Explicit_Recursive
from .Unit1.S1_4_2 import AGS_Find_The_Slope_Section_1, AGS_Find_The_Slope_Section_2, AGS_Find_The_Slope_Section_3, AGS_Find_The_Slope_Section_4
from .Unit1.S1_5_1 import Information_To_Geometric_Sequence
from .Unit1.S1_5_2 import Slope_Intercept_Form_1, Slope_Intercept_Form_2
#from .Unit1.S1_5_3 import Geometric_Sequence_To_Explicit_Recursive
#not done, but close (done somewhere else)
from .Unit1.S1_6_1 import AGS_Percent_Change
from .Unit1.S1_6_2 import Is_It_Arithmetic_Or_Geometric_Sequence
from .Unit1.S1_8_1 import Fill_The_Gap
from .Unit1.S1_9_1 import Which_Grows_Faster
#from .Unit1.S1_10_1 import _ (not done, will do later)

# from .Unit2.S2_1_1 import _
from .Unit2.S2_2_1 import Find_The_Slope
# from .Unit2.S2_2_2 import Indicate_The_Relationship
from .Unit2.S2_2_3 import Solve_The_Following_Equations
from .Unit2.S2_2_4 import Find_The_Recursive_And_Explicit_Equations
from .Unit2.S2_3_1 import Rules_Of_Exponents
from .Unit2.S2_3_2 import Details_Of_Linear_And_Geometric_Sequences_1, Details_Of_Linear_And_Geometric_Sequences_2, Details_Of_Linear_And_Geometric_Sequences_3
from .Unit2.S2_3_3 import Fill_In_The_Blanks
from .Unit2.S2_3_4 import Find_The_Slope_Table
from .Unit2.S2_4_1 import Square_Roots
from .Unit2.S2_4_2 import Fill_In_The_Table
from .Unit2.S2_5_1 import Higher_Order_Roots
from .Unit2.S2_5_2 import Evaluate_The_Function
from .Unit2.S2_6_1 import Percent_Increase_Decrease
from .Unit2.S2_6_2 import Monthly_Exponential
"""
from .Unit2.S2_7_1 import _
from .Unit2.S2_7_2 import _
from .Unit2.S2_7_3 import _
from .Unit2.S2_8_1 import _
from .Unit2.S2_10_1 import _
from .Unit2.S2_10_2 import _
from .Unit2.S2_11_1 import _

from .Unit3.S3_1_1 import _
"""

from random import randint, choice

'''
AGS 1 Section 1-1-1
'''
def M_Evaluate_Equation(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""


  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-1-1-1'):
        problem, answer = Evaluate_Equation_1(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "$ {\\color{red}" + str(answer) + "} $"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + "\\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-1-1-2'):
        problem, answer = Evaluate_Equation_2(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      elif(twoDarr[total][0] == '1-1-1-3'):
        problem, answer = Evaluate_Equation_3(twoDarr[total][1], "latex")

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-1-2
'''
def M_Graph_The_Ordered_Pairs(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-1-2-1'):
        problem, answer = Graph_The_Ordered_Pairs(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{1cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{1cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{1cm}"

      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-2-1
'''
def M_Fill_In_The_Seq(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-1-1'):
        problem, answer = Fill_In_The_Sequence_1(twoDarr[total][1]) # error

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-2-1-2'):
        problem, answer = Fill_In_The_Sequence_2( choice(["lin", "exp", "neither"]) ) #["lin", "exp", "neither"]

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-2-1-3'):
        problem, answer = Fill_In_The_Sequence_3(twoDarr[total][1]) # error

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)
  

'''
AGS 1 Section 1-2-2
'''
def M_The_Meaning_Of_An_Exp(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-2-1'):
        problem, answer = The_Meaning_Of_An_Exponent_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-2-2-2'):
        problem, answer = The_Meaning_Of_An_Exponent_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-2-3
'''
def M_Finding_Patterns_In_Geo_Seq(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-2-3-1'):
        problem, answer = Finding_Patterns_In_Geometric_Shapes( choice(["lin", "exp"]) )

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 1-3-1
'''
def M_Reading_The_Table(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-1-1'):
        problem, answer = Reading_The_Table(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-3-2
'''
def M_Arithmetic_Seq(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-2-1'):
        problem, answer = Arithmetic_Sequences_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-3-2-2'):
        problem, answer = Arithmetic_Sequences_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-3-2-3'):
        problem, answer = Arithmetic_Sequences_3(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-3-3
'''
def M_Geo_Seq_Problem(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-3-1'):
        problem, answer = Geometric_Sequence_Problem(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-3-4
'''
def M_So_Should_We_Use(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-3-4-1'):
        problem, answer = So_Should_We_Use_Recursive_Or_Explicit(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

#--------------------
'''
AGS 1 Section 1-4-1
'''
def M_Arithmetic_Explicit_Recursive(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-4-1-1'):
        problem, answer = Arithmetic_Explicit_Recursive(twoDarr[total][1], 'all', blanks=True)

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-4-2
'''
def M_AGS_Find_The_Slope(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-4-2-1'):
        problem, answer = AGS_Find_The_Slope_Section_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-4-2-2'):
        problem, answer = AGS_Find_The_Slope_Section_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-4-2-3'):
        problem, answer = AGS_Find_The_Slope_Section_3(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-4-2-4'):
        problem, answer = AGS_Find_The_Slope_Section_4(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-5-1
'''
def M_Information_To_Geometric_Sequence(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-1-1'):
        problem, answer = Information_To_Geometric_Sequence(randint(1,4), kind='exp')

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-5-2
'''
def M_Slope_Intercept(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-5-2-1'):
        problem, answer = Slope_Intercept_Form_1(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      elif(twoDarr[total][0] == '1-5-2-2'):
        problem, answer = Slope_Intercept_Form_2(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-5-3
'''
def M_Geometric_Seq_To_Explicit_Recursive(twoDarr):  
  #Geometric_Sequence_To_Explicit_Recursive (Not DONE)
  return

'''
AGS 1 Section 1-6-1
'''
def M_AGS_Percentage_Change(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-1-1'):
        problem, answer = AGS_Percent_Change(twoDarr[total][1])

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-6-2
'''
def M_Is_It_Arith_Or_Geo_Seq(twoDarr):  
  #Is_It_Arithmetic_Or_Geometric_Sequence
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-2-1'):
        problem, answer = Is_It_Arithmetic_Or_Geometric_Sequence(randint(1,3))

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-8-1
'''
def M_Fill_The_Gap(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-8-1-1'):
        problem, answer = Fill_The_Gap() # only one setting

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-9-1
'''
def M_Which_Grows_Faster(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-9-1-1'):
        problem, answer = Which_Grows_Faster() # only one setting

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 1-10-1
'''
#1.10.1 Information to Arithmetic(?) Sequence.

#instruction: write the explicit equation for each geometric sequence.
# random.randint(1,4), no easy, medium, hard, and "lin"
def M_Information_To_Arith_Seq(twoDarr):  
  return



"""
'''
AGS 1 Section 2-1-1
'''
def _(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-9-1-1'):
        problem, answer = Which_Grows_Faster() # only one setting

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)
"""

'''
AGS 1 Section 2-2-1
'''
def M_Find_The_Slope(twoDarr):  
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '2-2-1-1'):
        problem, answer = Find_The_Slope( randint(1,3) ) 

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)


'''
AGS 1 Section 2-2-2
'''
# NO CODE

'''
AGS 1 Section 2-2-3
'''
def M_Solve_The_Following_Equations(twoDarr):
  masterSeed = []
  ANSmasterSeed = []
  newpageanswer = []
  tmasterSeed = ""
  tANSmasterSeed = ""

  for total in range(len(twoDarr)):
    midMasterSeed = ""
    midANSmasterSeed = ""
    midnewanswer = ""

    for i in range(twoDarr[total][2]):
      if(twoDarr[total][0] == '1-6-2-1'):
        problem, answer = Is_It_Arithmetic_Or_Geometric_Sequence(randint(1,3))

        tmasterSeed = "\\task " + str(problem) + " \\vspace{2cm}"
        temp_answer = "{\\color{red}" + str(answer) + "}"
        tANSmasterSeed = r"\task " + str(problem) + r"\\" + temp_answer + " \\vspace{2cm}"
        tnewpageanswer = "\\task " + temp_answer + " \\vspace{2cm}"
      
      midMasterSeed += tmasterSeed
      midANSmasterSeed += tANSmasterSeed
      midnewanswer += tnewpageanswer

    ANSmasterSeed.append(midANSmasterSeed)
    masterSeed.append(midMasterSeed)
    newpageanswer.append(midnewanswer)

  return (masterSeed, ANSmasterSeed, newpageanswer)

'''
AGS 1 Section 2-2-4
'''


'''
AGS 1 Section 2-3-1
'''


'''
AGS 1 Section 2-3-2
'''


'''
AGS 1 Section 2-3-3
'''


'''
AGS 1 Section 2-3-4
'''


'''
AGS 1 Section 2-4-1
'''


'''
AGS 1 Section 2-4-2
'''


'''
AGS 1 Section 2-5-1
'''


'''
AGS 1 Section 2-5-2
'''


'''
AGS 1 Section 2-6-1
'''


'''
AGS 1 Section 2-6-2
'''


'''
AGS 1 Section 2-7-1
'''


'''
AGS 1 Section 2-7-2
'''


'''
AGS 1 Section 2-7-3
'''


'''
AGS 1 Section 2-8-1
'''


'''
AGS 1 Section 2-10-1
'''


'''
AGS 1 Section 2-10-2
'''


'''
AGS 1 Section 2-11-1
'''
