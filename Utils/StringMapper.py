
units_mapping = {
    0 : "zéro",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze",
    16: "seize"
}

tens_mapping = {
     1: "dix",
     2: "vingt",
     3: "trente",
     4: "quarante",
     5: "cinquante",
     6: "soixante",
     8: "quatre-vingt"
}

def number_string_mapper(num, mapping_type) -> str:

    if mapping_type == 'tens':
        result = tens_mapping[num]

    elif mapping_type == 'units':
        result = units_mapping[num]

    return(result)