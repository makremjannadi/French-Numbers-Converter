from Utils.StringMapper import number_string_mapper
from Utils.ConversionCleaner import string_cleaner

def tens_divisor(num) -> str:
    if num <= 16:
        res = number_string_mapper(num, 'units')
        return(res)

    if num > 16:
        quotient, remainder = divmod(num, 10)

        if quotient in [1, 2, 3, 4, 5, 6]:
            if remainder == 0:
                res = number_string_mapper(quotient, 'tens')

            elif remainder == 1:
                res = number_string_mapper(quotient, 'tens') + "-et-un"

            else:
                res = number_string_mapper(quotient, 'tens') + '-' + number_string_mapper(remainder, 'units')

        elif quotient == 8:
            if remainder == 0:
                res = number_string_mapper(quotient, 'tens')

            elif remainder == 1:
                res = number_string_mapper(quotient, 'tens') + "-un"

            else:
                res = number_string_mapper(quotient, 'tens') + '-' + number_string_mapper(remainder, 'units')

        elif quotient == 7:
            res = number_string_mapper(quotient - 1, 'tens')

            if remainder == 1:
                res += "-et-onze"
            else:
                remainder += 10
                res += '-' + tens_divisor(remainder)

        else:
            res = number_string_mapper(quotient - 1, 'tens')

            if remainder == 1:
                res += "-onze"
            else:
                remainder += 10
                res += '-' + tens_divisor(remainder)

    return(res)


def hundreds_divisor(num) -> str:
    quotient, remainder = divmod(num, 100)

    if quotient == 0:
        res = tens_divisor(num)
        return (res)

    else:
        res = tens_divisor(quotient)
        res += "-cent"

        if remainder != 0:
            t_res = tens_divisor(remainder)
            res += '-' + t_res

        return(res)


def thousands_divisor(num) -> str:
    quotient, remainder = divmod(num, 1000)

    if quotient == 0:
        res = hundreds_divisor(num)
        return(res)

    else:
        q_res = hundreds_divisor(quotient)
        res = q_res + "-mille"

        if remainder != 0:
            r_res = hundreds_divisor(remainder)
            res = q_res + "-mille-" + r_res

        return(res)


def number_to_string_converter(num) -> str:
    num = int(num)
    if num < 0 or num > 999999:
        print('Please insert a number between 0 and 999999')
        return

    elif num <= 16:
        res = number_string_mapper(num, 'units')

    else:
        res = thousands_divisor(num)

    # clean conversion result
    res = string_cleaner(res)

    return(res)
