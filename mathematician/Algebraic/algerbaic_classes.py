import re
"""
This is a Set of classes defining Algebraic Methods:
Add(  array    ):            defines addition of arrayed entities
Multiply(    array   ):      defines multiplication of arrayed entities
Subtract(   array   ):       defines subtraction of arrayed entities
Divide(   array   ):         defines division of arrayed entities
Xn(     var = x,    n):      defines variable to the power n entity

"""


def findIntInAString(string_in):
    """
    Self-explanatory

    >>> findIntInAString("n + 15")
    ['15']

    >>> findIntInAString("n")

    :param string_in:
    :return list_of_integers_in_the_string:
    """
    return re.findall(r'\d+', string_in)


class Add():
    """
    Addition Object which adds arrayed entities
    >>> obj = Add(["sin(x)", "f(y)", "e^(x+y)"])
    >>> str(obj)
    'sin(x) + f(y) + e^(x+y)'

    >>> obj = Add(["sin(x)", "f(y)", "e^("+str(Add(["x", "y"]))+")"])
    >>> str(obj)
    'sin(x) + f(y) + e^(x + y)'
    """

    def __init__(self, array):
        self.array = array

    def __str__(self):
        string_out = ""
        for i in self.array:
            if i == self.array[-1]:
                string_out += str(i)
            else:
                string_out += str(i) + " + "

        return (string_out)


class Multiply():
    """
    Multiplication Object which multiplies the arrayed entities
    >>> obj = Multiply(["sin(x)", "f(y)", "e^(x+y)"])
    >>> str(obj)
    'sin(x) * f(y) * e^(x+y)'
    """

    def __init__(self, array):
        self.array = array

    def __str__(self):
        string_out = ""
        for i in self.array:
            if i == self.array[-1]:
                string_out += str(i)
            else:
                string_out += str(i) + " * "

        return (string_out)


class Subtraction():
    """
    Subtraction Object which subtracts the arrayed entities
    >>> obj = Subtraction(["sin(x)", "f(y)", "e^(x+y)"])
    >>> str(obj)
    'sin(x) - f(y) - e^(x+y)'
    """

    def __init__(self, array):
        self.array = array

    def __str__(self):
        string_out = ""
        for i in self.array:
            if i == self.array[-1]:
                string_out += str(i)
            else:
                string_out += str(i) + " - "

        return (string_out)


class Division():
    """
    Division Object which divides the arrayed entities
    >>> obj = Division(["sin(x)", "f(y)", "e^(x+y)"])
    >>> str(obj)
    'sin(x) / f(y) / e^(x+y)'
    """

    def __init__(self, array):
        self.array = array

    def __str__(self):
        string_out = ""
        for i in self.array:
            if i == self.array[-1]:
                string_out += str(i)
            else:
                string_out += str(i) + " / "

        return (string_out)


class Xn():
    """
    Defines a power function with radix = variable (default x) and power = power
    >>> power_obj = Xn(var= "x", power="n")
    >>> str(power_obj)
    'x^{n}'

    >>> power_obj.derivative()
    '(n) * x^{n-1}'
    """

    def __init__(self, power, var="x"):
        self.power, self.var = power, var

    def __str__(self):
        out = "%s^{%s}" % (str(self.var), str(self.power))
        return(out)

    def derivative(self):
        """
        Returns an object with first order derivative
        >>> power_obj = Xn(var= "x", power=15)
        >>> str(power_obj.derivative())
        '15 * x^{14}'

        :return: Multiply()
        """
        if isinstance(self.power, int) or isinstance(self.power, float):
            coeff = self.power
            diff_power = self.power - 1
            return Multiply([coeff, Xn(var=self.var, power=diff_power)])
        elif isinstance(self.power, str):
            # coeff = "({})".format(self.power)
            # offset_list = findIntInAString(self.power)
            # if len(offset_list) == 1:
            #     offset
            #     diff_power =
            pass

        raise Exception("Math Error: Can't differentiate the funtion")
