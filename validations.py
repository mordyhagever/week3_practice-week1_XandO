
def check_str(letter):
    pass

def is_int(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False

def check_square(square):
    if not is_int(square):
        return False
    square = int(square)
    if square < 1 or square > 9:
        return False
    return True

