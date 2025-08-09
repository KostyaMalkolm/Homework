from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_operations, filter_result_operations):
    assert filter_by_state(filter_operations) == filter_result_operations

# def test_sort_by_date()
#