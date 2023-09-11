
def list_divide(numbers, divide=2):
    count = 0
    for num in numbers:
         if num % divide == 0:
            count += 1
    return count

class ListDivideException(Exception):
    pass

def test_list_divide():
    # Test a
    if list_divide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException

    # Test b
    if list_divide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException

    # Test c
    if list_divide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException

    # Test d
    if list_divide([]) != 0:
        raise ListDivideException

    # Test e
    if list_divide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

def test_List_Divide():
    pass

if __name__ == "__main__":
    try:
        test_List_Divide()
        print("All tests passed.")
    except ListDivideException:
        print("At least one test failed.")