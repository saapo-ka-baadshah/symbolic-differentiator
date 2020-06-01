"""
Define a class of Expressions and Functions
Expr(   lhs,    rhs     ):                      defines an expression as LHS = RHS
Function(       name,   []variable    ):          defines a function with a function name and array of variables
"""


class Expr():
    """
    Define an Expression as LHS = RHS

    >>> expr = Expr(lhs= "y", rhs= Function(name= "f", variables= ["x"]))
    >>> str(expr)
    'y = f(x)'
    """
    def __init__(self, lhs, rhs):
        self.lhs, self.rhs = lhs, rhs

    def __str__(self):
        return(str(self.lhs) + " = " + str(self.rhs))

class Function():
    """
    Define a Function with a function name and its variables
    >>> func = Function(name="f", variables=["x", "y", "z"])
    >>> str(func)
    'f(x, y, z)'

    >>> str(func.differentiate())
    "f'(x, y, z)"

    >>> str(func.differentiate().differentiate())
    "f''(x, y, z)"

    >>> var_func = Function(name="y")
    >>> str(var_func.differentiate())
    "y'"

    """
    def __init__(self, name, variables= None):
        self.name, self.variables = name, variables

    def __str__(self):
        if (self.variables != None):
            function_name = str(self.name)
            list_of_variables = ", ".join(self.variables)
            out_string = "{}({})".format(function_name, list_of_variables)
            return out_string
        function_sym = str(self.name)
        return(function_sym)

    def differentiate(self):
        """
        Gets a function e.g. f(x)
        and returns it as f'(x)
        :return Function():
        """

        if (self.variables == None):
            return Function(name= self.name+"'", variables=None)
        return Function(name= self.name+"'", variables= self.variables)

