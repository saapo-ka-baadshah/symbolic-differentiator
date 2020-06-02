"""
sin     ( val )   :         Defines the regular expressions for trigonometric functions namely sin(),cos(),tan(),cosec(),sec(),cot()
cos     ( val )   : 
tan     ( val )   : 
sec     ( val )   : 
cosec   ( val )   : 
cot     ( val )   : 
"""


class sin():
    """
    >>> sin_obj=sin(val='x')
    >>> str(sin_obj)
    'sin(x)'

    >>> sin_obj.derivative()
    'cos(x)'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "sin(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = "cos(%s)" % (str(self.val))
        return out


class cos():
    """
    >>> cos_obj=cos(val='x')
    >>> str(cos_obj)
    'cos(x)'

    >> cos_obj.derivative()
    '-cos(x)'


    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "cos(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = "-sin(%s)" % (str(self.val))
        return out


class tan():
    """
    >>> tan_obj=tan(val='x')
    >>> str(tan_obj)
    'tan(x)'
    >>> tan_obj.derivative()
    'sec^{2}(x)'
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "tan(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = "sec^{2}(%s)" % (str(self.val))
        return out


class cot():
    """
    >>> cot_obj=cot(val='x')
    >>> str(cot_obj)
    'cot(x)'

    >>> cosec()
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "cot(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = "-cosec^{2}(%s)" % (str(self.val))
        return out


class cosec():
    """
    >>> cosec_obj=cosec(val='x')
    >>> str(cosec_obj)
    'cosec(x)'

    >>> cosec_obj.derivative()
    '-cosec(x)*cot(x)'
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "cosec(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = "-cosec(%s)*cot(%s)" % (str(self.val), str(self.val))
        return out


class sec():
    """
    >>> sec_obj=sec(val='x')
    >>> str(sec_obj)
    'sec(x)'

    >>> sec_obj.derivative()
    'sec(x)*tan(x)'
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "sec(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = "sec(%s)*tan(%s)" % (str(self.val), str(self.val))
        return out
