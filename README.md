# 💰 Controle Financeiro com Análise de Dados

Projeto desenvolvido em **Python** para controle de movimentações financeiras e análise dos dados gerados pelo próprio sistema.

A aplicação permite registrar receitas e despesas, controlar saldo e crédito disponível, consultar transações e gerar um resumo financeiro. As informações são armazenadas em arquivos **CSV**, permitindo que novos dados sejam adicionados continuamente pelo próprio programa.

Em um módulo separado, os dados são analisados utilizando **Pandas** e visualizados através de **Matplotlib**, possibilitando transformar as movimentações financeiras em informações e gráficos para análise.

---

## 📌 Sobre o projeto

O projeto foi desenvolvido com o objetivo de aplicar, em uma situação prática, conhecimentos de:

* Python;
* Programação Orientada a Objetos;
* Manipulação de arquivos CSV;
* Estruturação e organização de dados;
* Pandas;
* Matplotlib;
* Análise exploratória de dados;
* Visualização de dados;
* Validação e tratamento de entradas;
* Persistência de dados.

O sistema possui duas etapas principais:

**1. Controle e geração dos dados**

O usuário registra suas movimentações através do programa. As informações são processadas e armazenadas em arquivos CSV.

**2. Análise dos dados**

Os dados armazenados podem ser carregados posteriormente com Pandas para realização de análises e criação de visualizações utilizando Matplotlib.

Dessa forma, o projeto estabelece um fluxo completo:

```text
Entrada de dados
      ↓
Processamento
      ↓
Persistência em CSV
      ↓
Pandas
      ↓
Análise dos dados
      ↓
Matplotlib
      ↓
Visualizações
```

---

# ⚙️ Funcionalidades

## 💳 Controle financeiro

O sistema permite:

* Registrar receitas;
* Registrar despesas;
* Informar descrição da transação;
* Informar valor;
* Informar data;
* Classificar transações por categoria;
* Registrar despesas como **Pix**;
* Registrar despesas como **Débito**;
* Registrar despesas como **Crédito**;
* Atualizar automaticamente o saldo;
* Atualizar o crédito disponível;
* Consultar todas as transações;
* Visualizar um resumo financeiro;
* Alterar o limite de crédito disponível;
* Salvar os dados antes de encerrar o programa.

### Tipos de movimentação

As receitas são identificadas como:

```text
Receita
```

As despesas podem ser classificadas como:

```text
Pix
Débito
Crédito
```

O comportamento financeiro também varia de acordo com o tipo de despesa.

* **Pix:** reduz o saldo;
* **Débito:** reduz o saldo;
* **Crédito:** reduz o crédito disponível.

---

# 📊 Resumo financeiro

O sistema possui uma função de resumo que calcula e apresenta:

* Total de receitas;
* Total de despesas;
* Total gasto via Pix;
* Total gasto via Débito;
* Total gasto via Crédito;
* Saldo atual;
* Crédito disponível.

Exemplo:

```text
Receitas: R$ 5.000,00

Despesas: R$ 2.350,00
Sendo Pix: R$ 700,00 | Débito: R$ 950,00 | Crédito: R$ 700,00

Saldo: R$ 4.050,00
Crédito disponível: R$ 3.300,00
```

---

# 🧱 Programação Orientada a Objetos

A estrutura principal do controle financeiro utiliza **Programação Orientada a Objetos**.

A classe principal do sistema é:

```python
class Conta:
```

Ela concentra informações e comportamentos relacionados à conta financeira.

Entre os principais elementos estão:

### Atributos

```python
self._saldo
self._credito
self.df_t
```

Esses atributos representam:

* Saldo disponível;
* Crédito disponível;
* DataFrame contendo as transações.

### Métodos

A classe possui métodos responsáveis por diferentes operações:

```python
verif_insert()
_receita()
_despesa()
print_all_tran()
resumo()
alterar_credito()
salvar()
```

Essa organização permite concentrar as operações financeiras dentro da própria classe `Conta`.

---

# 🔒 Encapsulamento

O projeto também aplica o conceito de **encapsulamento**, utilizando atributos com `_`:

```python
self._saldo
self._credito
```

As alterações nesses valores são realizadas através dos métodos da classe, como:

```python
_receita()
_despesa()
alterar_credito()
```

Isso ajuda a organizar a responsabilidade sobre os dados da conta.

---

# 💾 Persistência dos dados

Os dados são armazenados em arquivos **CSV**, permitindo que as informações permaneçam disponíveis mesmo após o encerramento do programa.

São utilizados dois arquivos principais:

```text
Dados.csv
Transactions.csv
```

### Dados.csv

Armazena informações relacionadas ao estado atual da conta, como:

```text
Saldo
Credito
```

### Transactions.csv

Armazena as movimentações realizadas.

As transações possuem informações como:

```text
description
value
data
category
type
```

Dessa forma, cada nova transação pode ser adicionada à base existente.

---

# 🔄 Adição contínua de dados

Uma das características do projeto é que a base de dados não precisa permanecer estática.

O usuário pode executar o programa e registrar novas transações.

O sistema adiciona essas informações ao DataFrame:

```python
self.df_t.loc[len(self.df_t)] = [...]
```

e posteriormente salva o DataFrame novamente no arquivo:

```python
self.df_t.to_csv('Transactions.csv', index=False)
```

Isso permite utilizar o projeto continuamente e aumentar a quantidade de dados disponíveis para análise.

---

# 🐼 Análise de dados com Pandas

Além do sistema de controle financeiro, o projeto possui um módulo separado destinado à análise dos dados.

O arquivo `Transactions.csv` pode ser carregado utilizando Pandas:

```python
import pandas as pd

df = pd.read_csv('Transactions.csv')
```

A partir do DataFrame, é possível realizar operações de análise e tratamento dos dados.

Entre as competências aplicadas nessa etapa estão:

* Leitura de arquivos CSV;
* Criação e manipulação de DataFrames;
* Seleção e filtragem de dados;
* Agrupamento de informações;
* Agregação de valores;
* Análise de receitas e despesas;
* Análise por categoria;
* Análise por tipo de transação;
* Análise temporal;
* Cálculo de totais;
* Preparação dos dados para visualização.

---

# 📈 Visualização de dados com Matplotlib

Os dados financeiros também são utilizados para criação de visualizações utilizando **Matplotlib**.

Exemplo de importação:

```python
import matplotlib.pyplot as plt
```

As visualizações permitem observar os dados de maneira gráfica, facilitando a identificação de padrões e comportamentos nas movimentações financeiras.

Dependendo da análise realizada, podem ser visualizados aspectos como:

* Evolução dos gastos;
* Distribuição das despesas;
* Gastos por categoria;
* Comparação entre tipos de transação;
* Receitas e despesas;
* Comportamento financeiro ao longo do tempo.

---

# 🤖 Base de dados para análise

Para realizar análises envolvendo um período maior, o projeto também utiliza uma **base de dados fictícia** contendo movimentações financeiras.

Parte dessa massa de dados foi gerada com auxílio de **Inteligência Artificial**, exclusivamente para fins de teste, desenvolvimento e demonstração.

Os dados não representam informações financeiras reais.

Além da base fictícia inicial, o sistema permite que **novas transações sejam adicionadas pelo usuário**, aumentando progressivamente a quantidade de dados disponíveis para análise.

Isso possibilita testar o fluxo completo:

```text
Base inicial fictícia
        +
Novas transações
        ↓
Transactions.csv
        ↓
Pandas
        ↓
Tratamento e análise
        ↓
Matplotlib
        ↓
Gráficos
```

---

# 🧠 Competências desenvolvidas

## Python

* Sintaxe e estruturas fundamentais;
* Variáveis e tipos de dados;
* Estruturas condicionais;
* Estruturas de repetição;
* Funções;
* Tratamento de exceções com `try/except`;
* Entrada e validação de dados;
* Manipulação de arquivos;
* Organização de código.

## Programação Orientada a Objetos

* Classes;
* Objetos;
* Construtores;
* Atributos;
* Métodos;
* Encapsulamento;
* Separação de responsabilidades;
* Organização de uma aplicação utilizando POO.

## Manipulação de dados

* Leitura de CSV;
* Escrita de CSV;
* Persistência de informações;
* Manipulação de DataFrames;
* Inserção de novos registros;
* Filtragem;
* Agrupamento;
* Agregação;
* Transformação de dados.

## Análise de dados

* Análise exploratória;
* Cálculo de métricas;
* Análise de receitas;
* Análise de despesas;
* Análise por categoria;
* Análise por tipo de pagamento;
* Análise temporal;
* Identificação de padrões nos dados.

## Visualização de dados

* Criação de gráficos com Matplotlib;
* Comparação de categorias;
* Visualização de valores;
* Visualização da evolução dos dados;
* Comunicação visual dos resultados da análise.

---

# 🛠️ Tecnologias

| Tecnologia    | Utilização                            |
| ------------- | ------------------------------------- |
| 🐍 Python     | Desenvolvimento da aplicação          |
| 🧱 POO        | Estruturação do sistema               |
| 🐼 Pandas     | Manipulação e análise dos dados       |
| 📊 Matplotlib | Visualização dos dados                |
| 📄 CSV        | Persistência das informações          |

---

# 📁 Estrutura do projeto

A aplicação é organizada separando o controle financeiro da etapa de análise.

```text
controle_financeiro_com_analise/
│
├── Controle financeiro
│   └── Sistema responsável pelo registro
│       e armazenamento das transações
│
├── Análise
│   └── Módulo responsável pelo tratamento,
│       análise e visualização dos dados
│
├── Dados.csv
│
├── Transactions.csv
│
└── README.md
```

---

# ▶️ Como executar

## 1. Clone o repositório

```bash
git clone https://github.com/G33k02/controle_financeiro_com_analise.git
```

## 2. Acesse a pasta

```bash
cd controle_financeiro_com_analise
```

## 3. Instale as bibliotecas

```bash
pip install pandas matplotlib
```

## 4. Execute o programa

Execute o arquivo principal responsável pelo controle financeiro.

O programa apresentará um menu semelhante a:

```text
========== CONTROLE FINANCEIRO ==========

1 - Nova transação
2 - Mostrar transações
3 - Resumo
4 - Salvar e Sair
5 - Editar crédito
6 - Estatísticas
```

---

# 🔎 Exemplo de utilização

Uma nova despesa pode ser cadastrada informando:

```text
Descrição: Supermercado
Valor: 250
Data: 20/09/2026
Categoria: Alimentação
Tipo: Débito
```

O sistema registra a transação e atualiza o saldo.

Posteriormente, os dados podem ser carregados pelo módulo de análise para gerar informações e visualizações.

---


# 🎯 Objetivo

Este projeto foi desenvolvido como uma aplicação prática para consolidar conhecimentos de **Python, Programação Orientada a Objetos e Análise de Dados**.

A proposta é trabalhar com o ciclo completo dos dados:

**Entrada → Processamento → Armazenamento → Tratamento → Análise → Visualização**

Além de registrar movimentações financeiras, o projeto demonstra como dados gerados por uma aplicação podem posteriormente ser utilizados para produzir análises e informações úteis.

---

# 📚 Aprendizados

Durante o desenvolvimento, foram praticados conceitos de desenvolvimento de software e análise de dados, incluindo:

* Desenvolvimento de uma aplicação utilizando POO;
* Organização de responsabilidades dentro de uma classe;
* Validação de entradas do usuário;
* Tratamento de exceções;
* Persistência de dados em CSV;
* Manipulação de DataFrames;
* Análise de dados financeiros;
* Criação de gráficos;
* Separação entre geração e análise dos dados;
* Versionamento utilizando Git e GitHub.

---

# 👨‍💻 Autor

**Adrian Gonzaga**

Projeto desenvolvido para fins de estudo, prática e construção de portfólio na área de **Python, Análise de Dados e Tecnologia**.
