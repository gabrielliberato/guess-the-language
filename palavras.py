import pandas as pd
from random import randint

samples = pd.read_csv('files/sample_texts.csv')

languages = pd.read_csv('files/language-codes.csv')

n_languages = len(languages)

bloco = languages.iloc[randint(0, n_languages)]
texto_bloco = {'idioma': languages[languages['cod'] == bloco['cod']]['language'].iloc[0], 'texto': samples[samples['cod'] == bloco['cod']]['sample_text'].iloc[0]}

print(texto_bloco['idioma'])
print(texto_bloco['texto'])
