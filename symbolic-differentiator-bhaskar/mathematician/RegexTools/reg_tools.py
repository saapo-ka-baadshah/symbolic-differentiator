import re


def findIntInAString(string_in):
    """
    Self-explanatory

    >>> findIntInAString("n + 15")


    :param string_in:
    :return list_of_integers_in_the_string:
    """
    return [re.findall(r'\d+', string_in), re.findall(r'[\w+]\+', string_in)]
