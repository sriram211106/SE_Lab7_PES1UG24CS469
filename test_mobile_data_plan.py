from hypothesis import given, strategies as st
from mobile_data_plan import parse_plan, usage_average, payable_bill
import math

@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        parse_plan(s)
    except Exception as e:
        assert False, f"parse_plan crashed with: {e!r}"

@given(st.text() | st.none())
def test_usage_average_no_crash(s):
    try:
        usage_average(s)
    except Exception as e:
        assert False, f"usage_average crashed with: {e!r}"

@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception as e:
        assert False, f"payable_bill crashed with: {e!r}"

@given(st.lists(st.integers(min_value=0, max_value=10**6), min_size=1))
def test_usage_average_valid_input(nums):
    result = usage_average(",".join(map(str, nums)))
    assert result == sum(nums) // len(nums)

@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=10**6))
def test_payable_bill_never_negative(b, d):
    result = payable_bill(f"{b}|{d}")
    assert result is not None and result >= 0 and math.isfinite(result)