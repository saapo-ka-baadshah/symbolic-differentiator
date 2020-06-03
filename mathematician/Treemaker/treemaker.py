from mathematician.Treemaker.RegexTools.reg_tools import *
from mathematician.Expression.expressions import *
from mathematician.Algebraic.algerbaic_classes import *
from mathematician.Expression.expressions import *
from mathematician.Logarithmic.logarithm_classes import *
from mathematician.Variables.variables import *

NON_FUNCTION_LIST = ["log", "ln", "sin", "cos", "tan", "cosec", "cot", "sec", "sinh", "cosh", "tanh", "cosech",
                     "sech", "coth"]


def getFunctionTrees(inString):
    """
    >>> _, func = getFunctionTrees("f(x, y) = g(x) + x**2 + 13")
    >>> str(func[1])

    :param inString:
    :return:
    """


    function_locations, function_details = getFunctions(inString)
    function_list = list()
    for funct in function_details:
        print(funct)
        function_list.append(Function(name= funct["name"], variables= funct["variables"].replace(" ", "").split(",")))

    return(function_locations, function_list)



