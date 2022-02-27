import pandas as pd
#from matplotlib import pyplot
#import numpy as np

# countries = pd.read_csv('files/countries_data.csv')
# print(countries)

# samples = pd.read_csv('files/samples_texts.csv')
# print(samples)

valids = pd.read_csv('files/valids.csv')
# print(valids[valids['valid'] == 1])

# world = pd.read_csv('files/world.csv')
# print(world)

dominios_validos = valids[valids['valid'] == 1]['code'].values