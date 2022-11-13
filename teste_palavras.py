import random


def mistura(dici: dict, alternativas: list) -> dict:
    for i in alternativas:
        alt = random.choice(alternativas)
        dici['alternativa'] = alt
        alternativas.remove(alt)

    return dici


a = {'idioma': ['Basque', 'Norwegian Bokmål', 'Abkhazian', 'Aragonese', 'Bulgarian', 'Nepali', 'Hebrew', 'Panjabi', 'Sango', 'Kazakh', 'Lithuanian'],
     'texto': ['Wikipedia eduki askeko entziklopedia bat da, lankidetzaz editatua, eleanitza, Interneten argitaratua...', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
     'correto': [True, False, False, False, False, False, False, False, False, False, False]}

k = mistura(a, 'abcdefghijk'.split())
print(k)


# create a function that receives a dict and return a dict with values that are not none


