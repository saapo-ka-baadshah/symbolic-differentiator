"""
sin_inv     ( val )   :         Defines the regular expressions for inverse trigonometric functions namely asin(),acos(),atan(),acosec(),asec(),acot()
cos_inv     ( val )   :
tan_inv     ( val )   :
secIinv     ( val )   :
cosec_inv   ( val )   :
cot_inv     ( val )   :
"""


class sin_inv():
    r"""
    >>> sin_obj=sin_inv(val='x')
    >>> str(sin_obj)
    'sin^{-1}(x)'

    >>> sin_obj.derivative()
    '\\frac{1}{\\sqrt{1-x^{2}}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "sin^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = r'\frac{1}{\sqrt{1-%s^{2}}}' % (str(self.val))
        return out


class cos_inv():
    r"""
    >>> cos_obj=cos_inv(val='x')
    >>> str(cos_obj)
    'cos^{-1}(x)'

    >>> cos_obj.derivative()
    '\\frac{1}{\\sqrt{x^{2}-1}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "cos^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = r'\frac{1}{\sqrt{%s^{2}-1}}' % (str(self.val))
        return out


class tan_inv():
    r"""
    >>> tan_obj=tan_inv(val='x')
    >>> str(tan_obj)
    'tan^{-1}(x)'

    >>> tan_obj.derivative()
    '\\frac{1}{1+x^{2}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "tan^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = r'\frac{1}{1+%s^{2}}' % (str(self.val))
        return out


class cot_inv():
    r"""
    >>> cot_obj=cot_inv(val='x')
    >>> str(cot_obj)
    'cot^{-1}(x)'

    >>> cot_obj.derivative()
    '\\frac{-1}{1+x^{2}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "cot^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = r'\frac{-1}{1+%s^{2}}' % (str(self.val))
        return out


class sec_inv():
    r"""
    >>> sec_obj=sec_inv(val='x')
    >>> str(sec_obj)
    'sec^{-1}(x)'

    >>> sec_obj.derivative()
    '\\frac{1}{|x|*\\sqrt{x^{2}-1}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "sec^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = r'\frac{1}{|x|*\sqrt{%s^{2}-1}}' % (str(self.val))
        return out


class cosec_inv():
    r"""
    >>> cosec_obj=cosec_inv(val='x')
    >>> str(cosec_obj)
    'cosec^{-1}(x)'

    >>> cosec_obj.derivative()
    '\\frac{-1}{|x|*\\sqrt{x^{2}-1}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "cosec^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = r'\frac{-1}{|x|*\sqrt{%s^{2}-1}}' % (str(self.val))
        return out
