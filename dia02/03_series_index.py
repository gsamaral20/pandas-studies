# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%
# Obter 1º elemento da lista
idades[0]

# Obter o último elemento da lista
idades[-1]

# Obter 1º elemento da serie
series_idades[0]

# O índices das series funcionam da mesma maneira que as chaves dos dicionários
# series_idades[-1] não existe chave -1

# Ordenar a series
series_idades = series_idades.sort_values()
series_idades

# Note que não irá retornar o 23
series_idades[0]

# O iloc utiliza o índice como posição
series_idades.iloc[0]
series_idades.iloc[-1]

# %%

# Obter os 3 primeiros elementos da series
series_idades.iloc[:3]

# %%


idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

indexs = [
    "Lucas", "Mariana", "Pedro", "Ana", "Rafael",
    "Juliana", "Bruno", "Camila", "Thiago", "Fernanda",
    "Gustavo", "Larissa", "Felipe", "Beatriz", "André"
]

series_idades = pd.Series(idades, index=indexs)
series_idades