import pandas as pd
from random import randint, shuffle

samples = pd.read_csv('files/sample_texts.csv')

languages = pd.read_csv('files/language-codes.csv')

n_languages = len(languages)

bloco = languages.iloc[randint(0, n_languages)]
print(samples[samples['cod'] == bloco['cod']]['sample_text'].iloc[0])
bloco_correto = {'idioma': languages[languages['cod'] == bloco['cod']]['language'].iloc[0],
                 'texto': samples[samples['cod'] == bloco['cod']]['sample_text'].iloc[0],
                 'correto': True}

idioma_erradas = [languages[languages['cod'] == languages.iloc[randint(
    0, n_languages)]['cod']]['language'].iloc[0] for i in range(4)]
bloco_errado = {'idioma': idioma_erradas,
                'correto': [False, False, False, False]}


# print(f"\nIdioma: {bloco_correto['idioma']}")
# print(f"\nAmostra de texto: {bloco_correto['texto']}")
# print(f"\nCorreto: {bloco_correto['correto']}\n")

print(f"\nIdioma: {bloco_errado['idioma']}")
# print(f"\nCorreto: {bloco_errado['correto']}\n")

pos = randint(1, 5)
err_print = bloco_errado.copy()
print(f'{pos=}')
for i in range(5):
    print(i, end=": ")
    if i == pos:
        print(f"--> Idioma: {bloco_correto['idioma']}")
        # print(f"Amostra de texto: {bloco_correto['texto']}")
        # print(f"Correto: {bloco_correto['correto']}")
    else:
        try:
            print(f"Idioma: {err_print['idioma'][i]}")
            err_print['idioma'] = [k for j, k in enumerate(err_print['idioma']) if j != i]
            err_print['correto'] = [k for j, k in enumerate(err_print['idioma']) if j != i]
            # print(f"Correto: {bloco_errado['correto'][i]}")
        except:
            try:
                print(f"Idioma: {bloco_errado['idioma'][i+1]}")
                err_print['idioma'] = [k for j, k in enumerate(err_print['idioma']) if j != i]
                err_print['correto'] = [k for j, k in enumerate(err_print['idioma']) if j != i]
            # print(f"\nCorreto: {bloco_errado['correto'][i-1]}")
            except:
                print(f"Idioma: {bloco_errado['idioma'][i-1]}")
                err_print['idioma'] = [k for j, k in enumerate(err_print['idioma']) if j != i]
                err_print['correto'] = [k for j, k in enumerate(err_print['idioma']) if j != i]
            