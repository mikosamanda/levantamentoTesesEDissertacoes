# Levantamento bibliográfico
## Pesquisa inciada no dia 02/11 
## Banco de dados: Banco de teses e dissertaçoes da CAPES
##Tipos de documntos: Teses e Dissertações
## Intervalo de tempo: 1987 - 2024

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carrega o arquivo xlsx
df = pd.read_excel('/home/hub-ia/Documentos/Inteligencia_Atificial/TeseseDissertações Capes_ IA.xlsx')


# Mostra as primeiras linhas
print(df.head())

##Gráfico de Barras: Ideal para comparar a quantidade de publicações por ano. Esse gráfico pode ser útil se você quiser ver variações entre anos específicos.


# Configurar o estilo dos gráficos
plt.style.use('ggplot')

######## GRÁFICOS DE LINHAS ########
##Gráfico de Linha: Útil para ver a tendência ao longo do tempo. Mostra como a quantidade de publicações de teses e dissertações evoluiu ano a ano.


##### Gráfico com duas linhas "TESES" e "DISSERTAÇÕES" #####

# Configuração do tamanho do gráfico
plt.figure(figsize=(10, 6))

# Linha para teses
plt.plot(df['ANO'], df['TESES'], marker='o', color='r', label='Teses')

# Linha para dissertações
plt.plot(df['ANO'], df['DISSERTAÇÕES'], marker='o', color='g', label='Dissertações')

# Rótulo do eixo X
plt.xlabel('Ano')

# Rótulo do eixo Y
plt.ylabel('Quantidade de Publicações')

# Título do gráfico
plt.title('Evolução das Teses e Dissertações Publicadas por Ano')

# Exibir a legenda para identificar cada linha
plt.legend()

# Mostrar o gráfico
plt.show()

##### Gráfico de linhas para o TOTAL #####

plt.figure(figsize=(10, 6))
plt.plot(df['ANO'], df['TOTAL'], marker='o', color='b', label='Quantidade de Publicações')
plt.xlabel('ANO')
plt.ylabel('Quantidade de Publicações')
plt.title('Evolução das Teses e Dissertações Publicadas por ano')
plt.legend()
plt.show()

######## HISTOGRAMA ########
##Histograma: Pode ser usado para visualizar a distribuição de publicações em um período, ajudando a identificar anos com muitas ou poucas publicações.

# Histograma
##plt.figure(figsize=(10, 6))
##plt.hist(df['ANO'],bins=50, color='skyblue', edgecolor='black')
##plt.xlabel('Quantidade de Publicações')
##plt.ylabel('Frequência')
##plt.title('Distribuição da Quantidade de Publicações por Ano')
## plt.show() ## NÃO TA DANDO CERTO

## 2. Gráfico de Barras: Comparação da quantidade por ano
plt.figure(figsize=(12, 7))
plt.bar(df['ANO'], df['TOTAL'], color='#800080', edgecolor='black')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Publicações')
plt.title('Quantidade de Teses e Dissertações Publicadas por Ano')
plt.show()

## 2. Gráfico de Barras: Comparação da quantidade por ano

# Definindo o número de barras
n = len(df['ANO'])

# Configurando o tamanho do gráfico
plt.figure(figsize=(12, 7))

# Criando um eixo para os valores
bar_width = 0.35  # Largura das barras
x = np.arange(n)  # Posicionamento das barras no eixo x

plt.bar(x - bar_width/2, df['TESES'], width=bar_width, color='#800080', edgecolor='black', label='Teses')
plt.bar(x + bar_width/2, df['DISSERTAÇÕES'], width=bar_width, color='r', edgecolor='black', label='Dissertações')

#Rótulos e título
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Quantidade de Publicações', fontsize=14)
plt.title('Quantidade de Teses e Dissertações Publicadas por Ano', fontsize=16)

# Rótulos nos eixos
plt.xticks(x, df['ANO'], rotation=45, fontsize=9)
plt.yticks(fontsize=12)

# Adicionando uma grade
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando legenda
plt.legend()

# Exibindo o gráfico
plt.tight_layout()  # Ajusta os elementos do gráfico
plt.title('Quantidade de Teses e Dissertações Publicadas por Ano')
plt.show()