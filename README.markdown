# Database Project

Este projeto implementa um sistema de banco de dados com SQLite, incluindo tabelas, triggers, views e testes automatizados com pytest. O projeto segue as especificações de um trabalho acadêmico.

## Pré-requisitos

- Python 3.x
- Git
- LaTeX (para compilar o relatório)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Natanael-SSilva/database_project.git
   cd database_project
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv bd_env
   bd_env\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Executando os Testes

1. Navegue até a pasta do projeto:

   ```bash
   cd database_project
   ```

2. Execute os testes com pytest:

   ```bash
   pytest tests/
   ```

## Compilando o Relatório

1. Instale um compilador LaTeX (ex.: MiKTeX).

2. Navegue até a pasta `docs`:

   ```bash
   cd docs
   ```

3. Compile o relatório:

   ```bash
   latexmk -pdf report.tex
   ```

## Enviando Alterações para o GitHub

1. Adicione os arquivos:

   ```bash
   git add .
   ```

2. Faça um commit:

   ```bash
   git commit -m "Implementação do projeto de banco de dados"
   ```

3. Envie para o GitHub:

   ```bash
   git push origin main
   ```

## Contato

Para dúvidas, entre em contato com [natanaelsantos.tech@gmail.com].