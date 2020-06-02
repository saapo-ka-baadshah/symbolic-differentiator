import re


def getSymbolList(inString):
    return re.findall(r"[(\+|\-)(.*?)(\+|\-)]+", inString)


def getFunctions(inString):
    """
    >>> random_string = "g(x) = x + x**2 + f(x + x**2)"
    >>> res = getFunctions(random_string)
    >>> print(res)

    :param inString:
    :return list:
    """
    pat = re.compile(r"\w+\(.*?\)")
    pat_function_name = re.compile(r"\w+\(")
    pat_function_value = re.compile(r"\(.*?\)")
    function_locations = list()
    function_details = list()
    for match in pat.finditer(inString):
        subString = str(match.group())
        function_name = pat_function_name.findall(subString)[0][:-1]
        function_value = pat_function_value.findall(subString)[0][1:-1]
        function_locations.append([match.start(), match.end()])
        function_details.append([function_name, function_value])

    return(function_locations, function_details)

def getExponents(inString):
    """
    >>> random_string = "g(x) = x + x**2 + f(x + x**2) + a^(x + x**2) + e^(x)"
    >>> getExponents(random_string)

    :param inString:
    :return:
    """


    pat = re.compile(r"\w+\^\(.*?\)")
    pat_exponent_base = re.compile(r"\w+\^")
    pat_exponent_value = re.compile(r"\(.*?\)")
    exponential_locations = list()
    exponent_details = list()
    for match in pat.finditer(inString):
        subString = str(match.group())
        exponent_base = pat_exponent_base.findall(subString)[0][:-1]
        exponent_value = pat_exponent_value.findall(subString)[0][1:-1]
        exponent_details.append([exponent_base, exponent_value])
        exponential_locations.append([match.start(), match.end()])

    return (exponential_locations, exponent_details)

def getLogarithms(inString):
    """
    >>> random_string = "g(x) = x + x**2 + f(x + x**2) + a^(x + x**2) + e^(x) + log(base1)(value1) + log(base)(value) + ln(value) + log(15)"
    >>> getLogarithms(random_string)

    :param inString:
    :return:
    """

    pat = re.compile(r"(log\(.*?\)\(.*?\))|(ln\(.*?\))|(log\(.*?\))")
    logarithms_locations = list()
    logarithms_details = list()
    for match in pat.finditer(inString):
        subString = match.group()
        type = match.groups().index(subString) + 1
        if type == 1:
            log_type = re.findall(r"\w+\(", subString)[0][:-1]
            log_base = re.findall(r"\(.*?\)", subString)[0][1:-1]
            log_val = re.findall(r"\(.*?\)", subString)[1][1:-1]
            logarithms_details.append([log_type, log_base, log_val])
        elif (type == 2) or (type == 3):
            log_type = re.findall(r"\w+\(", subString)[0][:-1]
            log_val = re.findall(r"\(.*?\)", subString)[0][1:-1]
            logarithms_details.append([log_type, log_val])
        logarithms_locations.append([match.start(), match.end()])

    return (logarithms_locations, logarithms_details)



def getBracketIndices(inString):
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



