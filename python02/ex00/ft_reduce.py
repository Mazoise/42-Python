def ft_reduce(function_to_apply, list_of_inputs):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if len(list_of_inputs) == 0:
        raise TypeError
    it = iter(list_of_inputs)
    result = next(it)
    for i in it:
        result = function_to_apply(result, i)
    return result
