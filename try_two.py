from dataclasses import replace
import itertools
from math import comb
import re
import string
from tkinter import W
from pprint import pprint 
import re
import string
import traceback

def get_number_of_propositions(expression):
    indexes = [expression[match.start()] for match in re.finditer(r'(?i)\b[a-z]\b', expression)]
    return indexes

def truthTable1(input, expression):
  expression = expression.lower()
  expression = expression.replace("and","&")
  expression = expression.replace("xor","^")
  expression = expression.replace("or","|")
  expression = expression.replace("not","~")

  temp = [[1, 0]] * len(input)
  indexes = [match.start() for match in re.finditer(r'(?i)\b[a-z]\b', expression)]
 
  print("Expression: ", expression)
  for combination in itertools.product(*temp):
    s = list(expression)
    for count ,index in enumerate(indexes):
        s[index] = combination[count]
    expression = "".join(str(x) for x in s)
    evaluation = eval(expression)
    print(expression + " |" , evaluation ,'\n')


expression_ = "NOT (NOT a AND b) AND (a AND b)"
propositions = get_number_of_propositions(expression_)
truthTable1(propositions,expression_)