def is_correct_number(n):
    if str(n).replace('.', '', 1).isdigit() and 0 <= float(n) <= 999999999999:
        return True
    else:
        raise ValueError("Number validate error")
