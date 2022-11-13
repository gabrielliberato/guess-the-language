import pandas as pd
from random import randint, shuffle

pontuacao = 0


def main():

    global pontuacao

    print(f"\nVOCÊ TEM {pontuacao} PONTOS\n")

    qtd = 10

    samples = pd.read_csv('files/sample_texts.csv')
    languages = pd.read_csv('files/language-codes-2.csv')

    alternativas = [k for k in "abcdefghijklmnopqrstuvwxyz"][0:qtd]
    # print(f"{alternativas=}")

    dict_idioma_escolhido = languages.sample(n=1).to_dict('records')[0]

    # print(dict_idioma_escolhido)

    nome_idioma_correto = dict_idioma_escolhido['language']
    # nome_idioma_correto = 'Herero'
    # print(f"{nome_idioma_correto=}")
    cod_idioma_correto = dict_idioma_escolhido['cod']
    # cod_idioma_correto = 'hz'
    # print(f"{cod_idioma_correto=}")
    amostra_idioma_correto = samples[samples['cod'] == cod_idioma_correto].to_dict(
        'records')[0]['sample_text']
    # amostra_idioma_correto = 'blablabla'
    bloco_correto = {'idioma': [nome_idioma_correto],
                     'texto': [amostra_idioma_correto],
                     'correto': [True]}

    # drop the correct language from the dataframe

    languages_restantes = languages[languages['cod']
                                    != dict_idioma_escolhido['cod']]

    # select 4 random languages from the remaining ones

    df_erradas = languages_restantes.sample(n=(qtd-1))

    idioma_erradas = df_erradas['language'].tolist()

    bloco_errado = {'idioma': idioma_erradas,
                    'texto': ['-'] * (qtd-1),
                    'correto': [False] * (qtd-1)}

    geral = {k: bloco_correto[k] + bloco_errado[k] for k in bloco_correto}

    # print(geral)

    df_geral = pd.DataFrame(geral).sample(frac=1).reset_index(drop=True)

    # print(df_geral[df_geral['correto'] == True].index[0])
    alternativa_correta = alternativas[df_geral[df_geral['correto'] == True].index[0]]

    print(
        f"\nAmostra do texto:\n\n{df_geral[df_geral['correto'] == True]['texto'].values[0]}\n")

    for alt, i in enumerate(df_geral['idioma']):
        if alt < qtd:
            print(f">> ({alternativas[alt]}) {i}")

    resposta = input('O trecho acima pertence a qual idioma? ').lower()
    # resposta = 'a'

    if resposta == alternativa_correta:
        pontuacao += 30
        print("\nVocê acertou!\n")
    else:
        if pontuacao > 5:
            pontuacao -= 5
        else:
            pontuacao = 0
        print("\nVocê errou ):")
        print(
            f"\nA alternativa correta era: {df_geral[df_geral['correto'] == True]['idioma'].values[0]}\n")


if __name__ == '__main__':
    while input('\nDeseja jogar? (S/N) ').lower() == 's':
        # while True:
        main()
