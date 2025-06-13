def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for:
    - Non-numeric input
    - Division by zero

    Args:
        numerator: The numerator (expected to be a number or numeric string)
        denominator: The denominator (expected to be a number or numeric string)

    Returns:
        A string with the result or an error message
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt the division
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
