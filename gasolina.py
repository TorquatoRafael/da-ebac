
# Importando as bibliotecas
import matplotlib.pyplot as plt
import pandas as pd

# Carregarando os dados
df = pd.read_csv('gasolina.csv')

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-', color='c', label='Preço')

# Personalizar o gráfico
plt.title('Preço de Gasolina por dia em SP')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.legend()

# Salvando o gráfico
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()
