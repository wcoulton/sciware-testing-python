# -*- coding: utf-8 -*-
"""Main module template with example functions."""


def sum_numbers(number_list):
    """Example function. Sums a list of numbers using a for loop.

    Parameters
    ----------
    number_list : list
        List of ints or floats

    Returns
    -------
    int or float
        Sum of list

    Notes
    -----
    This is NOT good Python, just an example function for tests.

    Examples
    --------
    >>> number_list = [2, 3, 4]
    >>> sum_numbers(number_list)
    9

    Empty lists are returned as zero
    >>> zero_number_list = []
    >>> sum_numbers(zero_number_list)
    0

    Does not sum strings. Will return value error
    >>> not_number_list = [2, 3, 'stuff']
    >>> sum_numbers(not_number_list) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        raise ValueError(
    ValueError: sum_numbers sums a list containing only ints and floats

    Nor will it sum list of lists, dicts, sets, or tuples.
    # doctest: +IGNORE_EXCEPTION_DETAIL
    >>> another_not_number_list = [[4], 5]
    >>> sum_numbers(another_not_number_list)
    Traceback (most recent call last):
        raise ValueError(
    ValueError: ...

    Bools are alright though.
    >>> bool_list = [True, False, False, True, True]
    >>> sum_numbers(bool_list)
    3

    Will sum tuples
    >>> number_tuple = (4, 9, 16)
    >>> sum_numbers(number_tuple)
    29

    """

    sum_val = 0
    for n in number_list:
        if not isinstance(n, (float, int)):
            raise ValueError(
                'sum_numbers sums a list containing only ints and floats.')
        sum_val += n

    return sum_val


def add_vectors(vector_1, vector_2):
    """Example function. Sums the same index elements of two list of numbers.

    Parameters
    ----------
    v1 : list
        List of ints or floats

    v2 : list
        List of ints or floats

    Returns
    -------
    list
        Sum of lists

    Notes
    -----
    This is NOT good Python, just an example function for tests.

    Examples
    --------
    >>> v1 = [2, 3, 4]
    >>> v2 = [4, 9, 16]
    >>> add_vectors(v1, v2)
    [6, 12, 20]

    Will not sum vectors of different lengths
    >>> v3 = [2, 3, 4]
    >>> v4 = [4, 9, 16, 25]
    >>> add_vectors(v3, v4) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        raise RuntimeError(
    RuntimeError: add_vectors can only add vectors of the same length.

    Adding two empty vectors will also return an empty vector
    Will not sum vectors of different lengths
    >>> v0 = []
    >>> add_vectors(v0, v0) # doctest: +IGNORE_EXCEPTION_DETAIL
    []

    Will only take lists
    >>> t1 = (2, 4, 8)
    >>> t2 = (3, 9, 27)
    >>> add_vectors(t1, t2) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        raise ValueError(
    ValueError: add_vectors can only sum vectors that are lists.

    """
    sum_vec = []
    if len(vector_1) != len(vector_2):
        raise RuntimeError(
            'add_vectors can only add vectors of the same length.')

    if not isinstance(vector_1, list) or not isinstance(vector_2, list):
        raise ValueError(
            'add_vectors can only sum vectors that are lists.')

    for a, b in zip(vector_1, vector_2):
        sum_vec += [a + b]

    return sum_vec


# std::vector<double> add_vectors(std::vector<double> &v1, std::vector<double> &v2)
# {
#     // Check inputs
#     if (v1.size() != v2.size())
#     {
#         throw std::invalid_argument("There's a mismatch in vector size" + std::to_string(v1.size()) + "!=" + std::to_string(v2.size()));
#     }

#     //
#     // Solution 1
#     //

#     // Add the vectors
#     std::vector<double> new_vector(v1.size());

#     for (size_t i = 0; i < v1.size(); i++)
#     {
#         new_vector[i] = v1[i] + v2[i];
#     }

#     //
#     // Solution 2
#     //

#     // std::vector<double> new_vector = v1;
#     // std::transform(new_vector.begin(), new_vector.end(), v2.begin(), new_vector.begin(), std::plus<double>());

#     return new_vector;
# }
