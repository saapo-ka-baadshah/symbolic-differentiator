import re


def getSymbolList(inString):
    return re.findall(r"[(\+|\-)(.*?)(\+|\-)]+", inString)

def convertToExpression(inString):
    """
    >>> convertToExpression("((f(x)) + (f(x) + g(y)))")
    :param inString:
    :return:
    """
    openning_bracket = list()
    function_indices = list()
    for i in range(len(inString)):
        char = inString[i]
        if char == "(":
            openning_bracket.append(i)

        try:
            if char == ")":
                start = openning_bracket.pop(-1)
                end = i
                function_indices.append([start, end])
        except Exception as e:
            print(e)
            raise Exception("Check the brackets please.")

        if (i == len(inString) and (len(openning_bracket) != 0)):
            raise Exception("You have an unbalanced number of brackets.")

    print(function_indices)



