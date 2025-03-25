import pandas as pd

# Carregar a planilha
file_path = "Copia_de_Employees.xlsx"  # Ajuste o caminho se necessário
df = pd.read_excel(file_path, sheet_name="Employees")

# Exibir as primeiras linhas
print(df.head())

# Calcular IQR
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

# Definir limites aceitáveis
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrar dados removendo outliers
df_no_outliers = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]

# Comparar médias
print("Média salarial antes:", df["Salary"].mean())
print("Média salarial depois:", df_no_outliers["Salary"].mean())

df_no_outliers["Start Date"] = pd.to_datetime(df_no_outliers["Start Date"], errors="coerce")

# Verificar se há valores inválidos (NaT)
print(df_no_outliers["Start Date"].isna().sum())

df_no_outliers["Start Date"] = pd.to_datetime(df_no_outliers["Start Date"], errors="coerce")

# Verificar se há valores inválidos (NaT)
print(df_no_outliers["Start Date"].isna().sum())

# Remover linhas com salários vazios
df_no_outliers = df_no_outliers.dropna(subset=["Salary"])

#Remover linhas duplicadas
df_no_outliers = df_no_outliers.drop_duplicates()

#Salvar os dados limpos
df_no_outliers.to_excel("Employees_Cleaned.xlsx", index=False)
df_no_outliers.to_csv("Employees_Cleaned.csv", index=False)
