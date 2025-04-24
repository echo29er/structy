import time

### TEST RUNNER
def test_runner(test_function, expected_result):
    """
    Runs a test function with timing and verification

    Args:
        test_name: Name of the test for identification
        test_func: Function to execute (should take no arguments)
        expected_result: The expected result

    Returns:
        String with test result and timing information
    """
    test_name = test_function.__name__  # Get the function name automatically
    start_time = time.perf_counter()
    actual = test_function()
    execution_time = time.perf_counter() - start_time

    # Convert to microseconds for better precision with fast tests
    execution_time_us = execution_time * 1_000_000

    try:
        assert actual == expected_result, f"Expected {expected_result}, got {actual}"
        return f"✓ {test_name}: PASS - Result: {actual} (executed in {execution_time_us:.2f} microseconds)"
    except AssertionError as e:
        return f"✗ {test_name}: FAIL - {e} (executed in {execution_time_us:.2f} microseconds)"