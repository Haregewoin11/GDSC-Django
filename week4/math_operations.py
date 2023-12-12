def operations(a, b):
    result = {}
    try:
        result["Addition"] = a + b
        result["Substraction"] = a - b
        result["Multiplication"] = a * b
        if b != 0:
            result["Division"] = a / b
        else:
            raise ZeroDivisionError("Error: Cannot divide by Zero.")
    except TypeError:
        print("Error: Invalid input type. Both inputs should be numbers.")
    finally:
        return result
    pass


def power_operation(base, ex, **kwargs):
    try:
        power = base ** ex

        if 'modulo' in kwargs:
            power %= kwargs['modulo']

        return power
    except TypeError:
        print("Error: Invalid input type. Both inputs should be numbers.")
    except ValueError:
        print("Error: Invalid values. Both inputs must not be negative numbers.")
    pass


def apply_operations(operation_list):
    return list(map(lambda op: op0, operation_list))


def basic_operations(n1, n2):
    result = {}
    try:
        result["Addition"] = n1 + n2
        result["Substraction"] = n1 - n2
        result["Multiplication"] = n1 * n2
        if n2 != 0:
            result["Division"] = n1 / n2
        else:
            raise ZeroDivisionError("Error: Cannot divide by Zero.")
    except TypeError:
        print("Error: Invalid input type. Both inputs should be numbers.")
    finally:
        return result
    pass


def power_operation(base, ex, **kwargs):
    try:
        power = base ** ex

        if 'modulo' in kwargs:
            power %= kwargs['modulo']

        return power
    except TypeError:
        print("Error: Invalid input type. Both inputs should be numbers.")
    except ValueError:
        print("Error: Invalid values. Both inputs must not be negative numbers.")
    pass


def apply_operations(operation_list):
    return list(map(lambda op: op0, operation_list))



