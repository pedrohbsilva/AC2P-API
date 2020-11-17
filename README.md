# AC2P API

Este projeto utiliza python, utilizando o micro framework Flask, com o objetivo de criar uma
API de dados de solicitação de corridas, como o UBER ou o 99.

## Configuração

Utilizar o python3, criar uma virtualenv usando o comando virtualenv NOME_DA_PASTA.

Para instalar as dependências, utilize pip3 install -r requirements.txt

Para utilizar o migrate, use os comandos:
- python3 main.py db init: Para criar a pasta de migration
- python3 main.py db migrate: Para enviar as tabelas para a pasta migration
- python3 main.py db upgrade: Para criar dentro do seu database os migrations atualizados

