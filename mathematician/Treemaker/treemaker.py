from mathematician.Treemaker.RegexTools.reg_tools import *
from mathematician.Expression.expressions import *


def getFunctionTrees(inString):

    function_locations = getFunctions(inString)
    for fun_location in function_locations:
        local_function = inString[fun_location[0]: fun_location[1]]

