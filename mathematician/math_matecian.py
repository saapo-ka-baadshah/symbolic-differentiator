# from .Algebraic.algerbaic_classes import *
# from .Expression.expressions import *
# from .Logarithmic.logarithm_classes import *
from RegexTools.reg_tools import *

import re


class Mathematician():
    def __init__(self):
        pass

    def Symbolize(self, inString):
        """
        >>> mathem = Mathematician()
        >>> mathem.Symbolize("funca = f(y) * ( sin(x) - e^(x+y) )")
        ['(', ')', '*', '(', '(', ')', '-', '(', '+', ')', ')']

        :param inString:
        :return:
        """
        return (convertToExpression(inString))





