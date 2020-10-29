from collections import Counter
from hypothesis import given, strategies

from algorithms.quicksort import quicksort
from algorithms.sorting import mergesort
from algorithms.sorting import new_insertion_sort, insertion_sort

def _test_sorting_list_by_property(input_list, sorted_list):
    assert isinstance(sorted_list, list)
    assert Counter(sorted_list) == Counter(input_list)
    assert all(x <= y for x, y in zip(sorted_list, sorted_list[1:]))


@given(strategies.lists(strategies.integers()))
def test_quicksort_list_of_integers(numbers):
    result = numbers[:]
    quicksort(result)
    _test_sorting_list_by_property(numbers, result)


@given(strategies.lists(strategies.integers()))
def test_mergesort_list_of_integers(numbers):
    result = numbers[:]
    mergesort(result)
    _test_sorting_list_by_property(numbers, result)


@given(strategies.lists(strategies.integers()))
def test_insertion_list_of_integers(numbers):
    result = numbers[:]
    new_insertion_sort(result)
    _test_sorting_list_by_property(numbers, result)


@given(strategies.lists(strategies.integers()))
def test_another__list_of_integers(numbers):
    result = numbers[:]
    insertion_sort(result)
    _test_sorting_list_by_property(numbers, result)