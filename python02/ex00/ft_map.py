
def ft_map(function_to_apply, list_of_inputs):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if list_of_inputs is None:
        raise TypeError
    else:
        for x in list_of_inputs:
            yield function_to_apply(x)
