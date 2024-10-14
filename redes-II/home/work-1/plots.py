import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
labels = [
    'Sem intervalo', 'Intervalo 0.1s', 'Intervalo 0.01s'
]
enviadas = [727445, 2951, 26733]
recebidas = [727444, 2951, 26733]
perdidas = [1, 0, 0]
porcentagem_perda = [0.0001374674374007657, 0.0, 0.0]
mensagens_por_minuto = [145489.0, 590.0, 5347.0]
mensagens_por_segundo = [2425.0, 10.0, 89.0]
taxa_max = [4219.62, 9.93, 95.97]
taxa_min = [3.44, 7.50, 16.05]
taxa_media = [2567.27, 9.83, 89.25]
desvio_padrao = [394.63, 0.07, 3.01]

# 1. Gráfico de Barras: Enviadas, Recebidas e Perdidas
fig, ax = plt.subplots()
width = 0.2
indices = np.arange(len(labels))

ax.bar(indices - width, enviadas, width=width, label='Enviadas')
ax.bar(indices, recebidas, width=width, label='Recebidas')
ax.bar(indices + width, perdidas, width=width, label='Perdidas')

ax.set_xlabel('Condições de Envio')
ax.set_ylabel('Número de Mensagens')
ax.set_title('Mensagens Enviadas, Recebidas e Perdidas')
ax.set_xticks(indices)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.savefig('mensagens_enviadas_recebidas_perdidas.png')

# 2. Gráfico de Linhas: Taxa de Recebimento (Mínima, Média, Máxima)
plt.figure()
plt.plot(labels, taxa_max, label='Taxa Máxima', marker='o')
plt.plot(labels, taxa_min, label='Taxa Mínima', marker='o')
plt.plot(labels, taxa_media, label='Taxa Média', marker='o')

plt.xlabel('Condições de Envio')
plt.ylabel('Taxa de Recebimento')
plt.title('Taxa de Recebimento (Máxima, Mínima, Média)')
plt.legend()

plt.tight_layout()
plt.savefig('taxa_recebimento.png')

# 3. Gráfico de Barras: Média de Mensagens por Minuto e Porcentagem de Perda
fig, ax = plt.subplots()
ax.bar(labels, mensagens_por_minuto, label='Mensagens por Minuto')
ax.bar(labels, porcentagem_perda, bottom=mensagens_por_minuto, label='Porcentagem de Perda')

ax.set_xlabel('Condições de Envio')
ax.set_ylabel('Métricas')
ax.set_title('Mensagens por Minuto e Porcentagem de Perda')
ax.legend()

plt.tight_layout()
plt.savefig('mensagens_por_minuto_perda.png')

# 4. Gráfico de Dispersão: Mensagens Recebidas vs. Taxa de Recebimento Média
plt.figure()
plt.scatter(recebidas, taxa_media)

plt.xlabel('Mensagens Recebidas')
plt.ylabel('Taxa de Recebimento Média')
plt.title('Mensagens Recebidas vs. Taxa de Recebimento Média')

plt.tight_layout()
plt.savefig('scatter_mensagens_taxa.png')

plt.show()
