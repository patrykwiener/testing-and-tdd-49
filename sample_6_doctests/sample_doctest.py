def sample_addition(x, y):
    """
    Sample function adding two variables.

    :param x: x param
    :param y: y param
    :return: parameter sum
    >>> sample_addition(1, 22)
    23
    >>> sample_addition(0, 0)
    0
    >>> sample_addition('Ala ma ', 'kota')
    'Ala ma kota'
    """
    return x + y


def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
