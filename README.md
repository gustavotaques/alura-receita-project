# Projeto sobre Django

Esse é um projeto de um site de receitas do curso da Alura que utiliza alguns dos mais importantes conceitos sobre o framework Django

---

## Getting Started

Para rodar este projeto você precisa realizar alguns passos:

### Passo A: Ambiente Virtual

1. Crie um ambiente virtual (geralmente uso o `virtualenv`) e ative-o

### Passo B: Instalando as dependências

1. No terminal com o caminho do projeto digite `pip install -r requirements.txt` para instalar as dependências do projeto

### Passo C: Instale e configure o PostgreSQL (se caso já houver o PostgreSQL no sistema, ignorar este passo)

#### Tutorial de como instalar e configurar no Windows:

1. Acompanhe o vídeo até aos 3:05  `https://www.youtube.com/watch?v=FoqXi0wpX4c`

#### Para instalar no ambiente WSL e Linux:

1. Vá para `https://docs.microsoft.com/pt-br/windows/wsl/tutorials/wsl-database` e siga o passo a passo referente à instalação do PostgreSQL

### Passo D: Criando arquivo para variáveis de ambiente

1. Crie um arquivo `.env` na raiz do projeto
2. Copie todas as variáveis que consta em `.template.env` para o arquivo criado

### Passo E: Configurando o Banco de Dados no projeto

#### No Windows:

1. Execute o `SQL Shell`
2. Crie um database com o comando `CREATE DATABASE <nome_do_database>;`
3. Atribua o `<nome_do_database>` na variável `DB_NAME` no arquivo `.env`
4. Atribua o `nome_do_usuario` (por padrão é `postgres`) na variável `DB_USER` no arquivo `.env`
5. Atribua o `password` (criado quando configurado o PostgreSQL) na variável `DB_PWD` no arquivo `.env`
6. Ainda no `SQL Shell` execute o comando `GRANT ALL PRIVILEGES ON DATABASE <nome_do_database> TO nome_do_usuario;`. Se confirmado ele aparecerá `GRANT`

#### No WSL e Linux

1. 
