"""
This is a Set of classes defining Logarithmic Methods:
Log(    base = 10,   val     ):                  defines a log funtion of value = val with the base = base (default
                                                        value of base is 10)(By Default it is a natural log function)
Ln(     val     ):                               defines a log funtion of value = val with the base = e (By default
                                                        it is a mathematical log function)
ALog(   base = 10,  val     ):                   defines an antilog funtion of value = val with base = base (default
                                                        value of base is 10)(By Default it is anti-log of natural log)

Anti-log of Ln is not defined since it is supposed to be covered in the exponential package
"""


class Log():
    """
    Defines a log function with base = base and value = val
    >>> log_obj = Log(val="x", base="y")
    >>> str(log_obj)
    'log_{y}(x)'
    """

    def __init__(self, val, base=10):
        self.base, self.val = base, val

    def __str__(self):
        out = "log_{%s}(%s)" % (str(self.base), str(self.val))
        # out_inverse_trigo = "tan^{-1}(%s)"%(str(self.val))
        return(out)


class Ln():
    """
    Defines a mathematical log function with base = e and value = val
    >>> ln_obj = Ln(val="x")
    >>> str(ln_obj)
    'log_{e}(x)'
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "log_{%s}(%s)" % (str("e"), str(self.val))
        return(out)
