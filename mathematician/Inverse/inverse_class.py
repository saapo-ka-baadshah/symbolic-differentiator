"""
sin     ( val )   :         Defines the regular expressions for trigonometric functions namely sin(),cos(),tan(),cosec(),sec(),cot()
cos     ( val )   :
tan     ( val )   :
sec     ( val )   :
cosec   ( val )   :
cot     ( val )   :
"""


class sin_inv():
    """
    >>> sin_obj=sin_inv(val='x')
    >>> str(sin_obj)
    'sin^{-1}(x)'

    >>> sin_obj.derivative()
    '1/\\\sqrt{1-x^{2}}'

    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        out = "sin^{-1}(%s)" % (str(self.val))
        return out

    def derivative(self):
        out = '1/\\' + 'sqrt{1-%s^{2}}' % (str(self.val))
        return out
