"""
Defines all Exponential Classes

Ax(		radix, exponent 	):				defines a radic^(exponent) object (for common log)

Ex(		exponent 		):		            defines exp^(exponent) object

"""


class Ex():
    """
    >>> exp_obj = Ex(exponent='x')
    >>> str(exp_obj)
    'e^{x}'

    >>> exp_obj.derivative()
    'e^{x}'



    """

    def __init__(self, exponent):
        self.exponent = exponent

    def __str__(self):
        out = "e^{%s}" % (str(self.exponent))
        return out

    def derivative(self):
        out = "e^{%s}" % (str(self.exponent))
        return out


class Ax():
    r"""
    >>> exp_obj = Ax(exponent='x',radix='a')
    >>> str(exp_obj)
    'a^{x}'

    >>> exp_obj.derivative()
    'a^{x}*\\log(a)'



    """

    def __init__(self, exponent, radix):
        self.exponent = exponent
        self.radix = radix

    def __str__(self):
        out = "%s^{%s}" % (str(self.radix), str(self.exponent))
        return out

    def derivative(self):
        out = r"%s^{%s}*\log(%s)" % (str(self.radix),
                                     str(self.exponent), str(self.radix))
        return out
