
# 📊 Análise e Limpeza de Dados de Funcionários

Este projeto Python realiza uma análise exploratória e limpeza de dados de uma planilha de funcionários. É ideal para processos de pré-processamento em pipelines de análise de dados, ciência de dados e BI (Business Intelligence).

---

## 🧩 Funcionalidades

- ✅ Leitura de planilha Excel com `pandas`.
- 📉 Identificação e remoção de **outliers salariais** utilizando o intervalo interquartílico (IQR).
- 📆 Conversão e validação de datas de início (`Start Date`).
- ❌ Remoção de valores nulos e duplicados.
- 💾 Exportação dos dados limpos em formatos Excel e CSV.

---

## ⚙️ Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - `pandas`
  - `openpyxl` (para salvar em Excel)

### Instalação rápida:

```bash
pip install pandas openpyxl
```

---

## 🚀 Como utilizar

1. Coloque o arquivo `Copia_de_Employees.xlsx` no mesmo diretório que o script `analise_employees.py`.
2. Execute o script via terminal:

```bash
python analise_employees.py
```

3. Serão gerados os seguintes arquivos com os dados limpos:
   - `Employees_Cleaned.xlsx`
   - `Employees_Cleaned.csv`

---

## 🗂 Estrutura do Projeto

```
├── analise_employees.py         # Script principal de análise
├── Copia_de_Employees.xlsx      # Planilha original de entrada
├── Employees_Cleaned.xlsx       # Dados limpos em Excel
├── Employees_Cleaned.csv        # Dados limpos em CSV
└── README.md                    # Este arquivo
```

---

## 🧠 Lógica do Script

- **Outliers**: São removidos com base no cálculo de Q1, Q3 e IQR da coluna `Salary`.
- **Datas**: As datas da coluna `Start Date` são convertidas para o formato `datetime` e valores inválidos são tratados.
- **Qualidade dos Dados**: O script remove valores nulos em `Salary` e linhas duplicadas para garantir a integridade dos dados.

---

## 📞 Contato

Desenvolvido por **[Digital Quanta](https://digitalquanta.com.br)** 🚀

👉 Para soluções em **análise de dados**, **inteligência artificial**, **automação de processos** e **desenvolvimento de sistemas personalizados**, fale com a gente!

---

&copy; 2025 Digital Quanta - Todos os direitos reservados.

