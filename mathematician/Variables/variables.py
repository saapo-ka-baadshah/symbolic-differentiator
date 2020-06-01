"""
Define a Variable Class with requirement of a symbol.
Consider the support of Latin symbols.

"""


class Variable():
    """
    Variable definition
    >>> var = Variable("x")
    >>> str(var)
    'x'
    """

    def __init__(self, symbol):
        if not symbol:
            raise(Exception("Variable should have a symbol. Expected an argument, got none.s"))
        if(symbol in ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
                      "varepsilon", "theta", "iota", "kappa", "vartheta", "rho", "sigma",
                      "tau", "upsilon", "phi", "chi", "psi", "omega"]):
            self.symbol = r"\%s"%(symbol)
        else:
            self.symbol = symbol

    def __str__(self):
        return self.symbol
