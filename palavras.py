import pandas as pd
from random import randint, shuffle

samples = pd.read_csv('files/sample_texts.csv')
languages = pd.read_csv('files/language-codes.csv')

n_languages = len(languages)

alternativas = ['a', 'b', 'c', 'd', 'e']

bloco = languages.iloc[randint(0, n_languages-1)]
bloco_correto = {'idioma': languages[languages['cod'] == bloco['cod']]['language'].iloc[0],
                 'texto': samples[samples['cod'] == bloco['cod']]['sample_text'].iloc[0],
                 'correto': True}

idioma_erradas = [languages[languages['cod'] == languages.iloc[randint(
    0, n_languages)]['cod']]['language'].iloc[0] for i in range(4)]
bloco_errado = {'idioma': idioma_erradas,
                'texto': ['-', '-', '-', '-'],
                'correto': [False, False, False, False]}

geral = {'idioma': [],
         'texto': [],
         'correto': []}
for k in bloco_errado.keys():
    geral[k] += bloco_errado[k]
    geral[k].append(bloco_correto[k])

df_geral = pd.DataFrame(geral).sample(frac=1).reset_index(drop=True)

correta = alternativas[df_geral[df_geral['correto'] == True].index[0]]
print(f"\n\t\t\t\t\tAmostra do texto:\n\n{df_geral[df_geral['correto'] == True]['texto'].values[0]}\n")

for alt, i in enumerate(df_geral['idioma']):
    print(f">> ({alternativas[alt]}) {i}")

resposta = input('\n\t\t\t\t\tO trecho acima pertence a qual idioma? ').lower()

if resposta == correta:
    print("\n\t\t\t\t\tVocê acertou!\n")
else:
    print("\n\t\t\t\t\tVocê errou ):")
    print(f"\n\t\t\t\t\tA alternativa correta era: {df_geral[df_geral['correto'] == True]['idioma'].values[0]}\n")

