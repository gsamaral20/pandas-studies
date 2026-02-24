# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

# Média de idades
media = sum(idades) / len(idades)
print("Média:", media)

# Variância
diffs = 0
for i in idades:
        diffs += (i - media)**2
variancia = diffs / (len(idades)-1)
print("Variância: ", variancia)

# %%

import pandas as pd

# Series só permite um "tipo" de dado
series_idades = pd.Series(idades)
series_idades

# %%

# Métodos das Series
# Média no Pandas
media_idades = series_idades.mean()
print("Média: ", media_idades)

# Variância Pandas
variancia_idades = series_idades.var()
print("Variância: ", variancia_idades)

# Descritivo Estatístico
summary_idades = series_idades.describe()
summary_idades
# %%
