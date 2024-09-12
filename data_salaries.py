# imports

# %%
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt



# %% 
df = pd.read_excel('data_salaries(avg comparison).xlsx')
print(df)


# %%
# Filtrar os dados por Data Scientist e Data Analyst
df_data_scientist = df[df['job_title'] == 'Data Scientist']
df_data_analyst = df[df['job_title'] == 'Data Analyst']

# Criar subplots para dois gráficos
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Gráfico para Data Scientist
sns.histplot(df_data_scientist['salary_in_usd'], bins=30, kde=True, color='blue', ax=axes[0])
axes[0].set_title('Distribuição de Salários - Data Scientist')
axes[0].set_xlabel('Salário em USD')
axes[0].set_ylabel('Frequência')

# Gráfico para Data Analyst
sns.histplot(df_data_analyst['salary_in_usd'], bins=30, kde=True, color='green', ax=axes[1])
axes[1].set_title('Distribuição de Salários - Data Analyst')
axes[1].set_xlabel('Salário em USD')

# Ajustar layout
plt.tight_layout()
plt.show()
