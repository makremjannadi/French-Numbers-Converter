
def string_cleaner(string_num) -> str:

    # add 's' at the end if 'mille', 'cent' or 'quatre-vingt' are at the tail of the string
    suffix = ('mille', 'cent', 'quatre-vingt')
    if string_num.endswith(suffix):
        string_num += 's'

    # remove 'un-' in 'un-mille' and 'un-cent'
    string_num = string_num.replace('un-cent', 'cent')
    string_num = string_num.replace('un-mille', 'mille')

    return(string_num)