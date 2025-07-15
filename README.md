![junho-vermelho](https://github.com/user-attachments/assets/568f363f-a7d4-4f77-95e7-3d8d6e76fd4d)
Projeto Junho Vermelho 🩸
Este projeto é uma aplicação web completa desenvolvida para a campanha Junho Vermelho, o mês de conscientização sobre a importância da doação de sangue. A plataforma funciona como um portal informativo e interativo, incentivando a doação e permitindo que a comunidade compartilhe suas experiências.

📜 Sobre a Campanha
O "Junho Vermelho" foi criado para destacar a importância da doação de sangue, um gesto que salva milhões de vidas. A campanha ganha força em junho por conta do Dia Mundial do Doador de Sangue, celebrado em 14 de junho. O objetivo é aumentar os estoques dos hemocentros, especialmente durante o inverno, período em que as doações costumam cair. Um único gesto pode salvar até quatro vidas. Seja um herói, doe sangue!

✨ Funcionalidades
O projeto conta com as seguintes funcionalidades:

Página Informativa Completa: Uma página única com diversas seções sobre a campanha, requisitos para doação, o passo a passo do processo e estatísticas nacionais.

Monitor de Estoque em Tempo Real: Uma seção dinâmica que se conecta a um banco de dados para exibir os níveis de estoque de cada tipo sanguíneo, com ícones animados que refletem a quantidade de bolsas.

Sistema de Usuários: Funcionalidade de cadastro e login de usuários em uma página dedicada para garantir a segurança.

Mural de Experiências: Uma seção de comentários onde usuários logados podem compartilhar suas experiências de doação, e todos os visitantes podem ler as mensagens de apoio e incentivo.

Navegação Inteligente: Um menu de navegação fixo que destaca a seção em que o usuário se encontra durante a rolagem da página.

Design Responsivo: O layout se adapta a diferentes tamanhos de tela, como celulares e tablets.

💻 Tecnologias Utilizadas
A aplicação foi construída utilizando um conjunto de tecnologias modernas, separando as responsabilidades entre o front-end, o back-end e o banco de dados.

Front-end (Interface do Usuário):

HTML5: Para a estruturação semântica do conteúdo.

CSS3: Para a estilização, animações e design responsivo.

Back-end (Lógica do Servidor):

Python 3: Linguagem principal para toda a lógica da aplicação.

Flask: Um micro-framework leve para criar o servidor web e a API REST que fornece os dados para o front-end.

Werkzeug: Para gerar e verificar hashes de senhas, garantindo a segurança dos usuários.

Banco de Dados:

MySQL: Um sistema de gerenciamento de banco de dados relacional robusto para armazenar os dados dos usuários, comentários e estoque de sangue.

MySQL Workbench: Ferramenta utilizada para modelar e administrar o banco de dados.

🚀 Como Executar o Projeto Localmente
Para rodar esta aplicação em seu ambiente de desenvolvimento, siga os passos detalhados abaixo.

Pré-requisitos
Antes de começar, certifique-se de que você tem os seguintes softwares instalados:

Python 3.8+ (Durante a instalação no Windows, marque a caixa "Add Python to PATH").

Git (para clonar o repositório).

MySQL Server (Anote a senha do usuário root durante a instalação).

Passo a Passo para a Instalação
Clone o repositório: Abra seu terminal e execute o seguinte comando para criar uma cópia local do projeto.

Bash
git clone https://github.com/Oliver4i2/seu-repositorio-aqui.git

Substitua a URL pela URL real do seu repositório no GitHub.

Acesse a pasta do projeto:

Bash
cd nome-da-pasta-do-projeto

Instale as dependências Python: Este comando usa o pip para ler o arquivo requirements.txt e instalar todas as bibliotecas necessárias (Flask, etc.).

Bash
# No Windows
py -m pip install -r requirements.txt

# No macOS/Linux
pip3 install -r requirements.txt
Configure o Banco de Dados:

Abra o MySQL Workbench e crie um novo "Schema" com o nome exato: hemocentro_db.

Dentro desse schema, abra uma nova janela de query e cole o conteúdo do arquivo schema.sql (que está na pasta do projeto).

Execute o script (clicando no ícone de raio ⚡️) para criar as tabelas usuarios, comentarios e estoque_sanguineo.

Configure as Credenciais do Banco de Dados:

Na pasta do projeto, encontre o arquivo config.py.example.

Faça uma cópia deste arquivo e renomeie a cópia para config.py.

Abra o novo config.py e preencha os campos user (geralmente 'root') e password (a senha que você criou ao instalar o MySQL).

Execute a Aplicação (2 Passos):

a) Inicie o servidor Back-end: Em um terminal, dentro da pasta do projeto, execute:

Bash

python app.py
Deixe este terminal aberto. Ele é o cérebro que se conecta ao banco de dados.

b) Inicie o Front-end: No Visual Studio Code, clique com o botão direito no arquivo index.html e selecione "Open with Live Server". Seu navegador abrirá o site no endereço http://127.0.0.1:5500 (ou uma porta similar).

Pronto! A aplicação estará rodando em sua máquina local.

📂 Estrutura de Pastas
junho-vermelho/
|-- imagens/
|   |-- prosangue.png
|   |-- hemorio.png
|   `-- (outras imagens)
|-- app.py             # Arquivo principal do Flask (Back-end)
|-- config.py          # Arquivo local com senhas (IGNORADO PELO GIT)
|-- config.py.example  # Exemplo de como configurar as senhas
|-- index.html         # Página principal da campanha
|-- login.html         # Página de login e cadastro de usuários
|-- style.css          # Folha de estilos principal
|-- schema.sql         # Script para criar as tabelas do banco de dados
|-- requirements.txt   # Dependências do Python
`-- README.md          # Este arquivo de documentação
Feito com ❤️ para conscientizar sobre um gesto que salva vidas.

Projeto da disciplina Desenvolvimento de Sistemas Web, do curso de Tecnologia em Análise e Desenvolvimento de Sistemas | IFB/Campus Brasília.

Autor: Pedro Oliveira

GitHub: https://github.com/Oliver4i2



