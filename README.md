![junho-vermelho](https://github.com/user-attachments/assets/568f363f-a7d4-4f77-95e7-3d8d6e76fd4d)

-----

# Projeto Junho Vermelho 🩸

Este projeto é uma aplicação web completa e interativa, desenvolvida em apoio à campanha **Junho Vermelho**, o mês de conscientização sobre a importância da doação de sangue. A plataforma serve como um canal informativo e, ao mesmo tempo, um espaço para a comunidade se engajar, visualizar dados em tempo real e compartilhar experiências.

### 📜 Sobre a Campanha

O "Junho Vermelho" foi criado para reforçar a importância da doação de sangue, um gesto simples que pode salvar até quatro vidas. A campanha é intensificada em junho para celebrar o **Dia Mundial do Doador de Sangue** (14 de junho) e para ajudar a manter os estoques dos hemocentros em níveis seguros, especialmente durante o inverno, quando as doações tendem a diminuir.

### ✨ Funcionalidades

O projeto final conta com as seguintes funcionalidades:

  * **Página Informativa:** Uma página principal rica em conteúdo, com seções sobre a campanha, quem pode ou não doar, o passo a passo da doação e dados estatísticos sobre o tema no Brasil.
  * **Visualização Dinâmica de Estoque:** Um painel que se conecta em tempo real ao banco de dados para mostrar os níveis de estoque de cada tipo sanguíneo, com ícones de bolsas de sangue que se preenchem de forma animada.
  * **Sistema de Autenticação de Usuários:** Uma página dedicada para cadastro e login, permitindo que os usuários tenham uma identidade no site. As senhas são armazenadas de forma segura usando criptografia (hashing).
  * **Mural Interativo de Experiências:** Uma seção de comentários onde todos podem ler as mensagens de apoio, mas apenas usuários logados podem publicar suas próprias experiências, que são exibidas com nome e data.
  * **Design Responsivo:** O layout da aplicação se adapta para uma visualização otimizada em desktops, tablets e celulares.

### 💻 Tecnologias Utilizadas

A aplicação foi construída com uma arquitetura moderna, separando as responsabilidades entre o front-end (navegador), o back-end (servidor) e o banco de dados.

  * **Front-end (Interface do Usuário):**

      * **HTML5:** Para a estruturação semântica do conteúdo.
      * **CSS3:** Para toda a estilização, animações e o design responsivo.
      * **JavaScript (Vanilla):** Para a interatividade da página, manipulação do DOM e consumo da API do back-end em tempo real via `fetch`.

  * **Back-end (Lógica do Servidor):**

      * **Python 3:** Linguagem principal para toda a lógica da aplicação.
      * **Flask:** Um micro-framework leve e poderoso para criar o servidor web e a API REST que gerencia usuários, comentários e o acesso ao banco de dados.
      * **Werkzeug:** Para gerar e verificar hashes de senhas, garantindo a segurança das contas dos usuários.

  * **Banco de Dados:**

      * **MySQL:** Um robusto sistema de gerenciamento de banco de dados relacional para armazenar os dados dos usuários, comentários e estoque de sangue.
      * **MySQL Workbench:** Ferramenta utilizada para modelar e administrar o banco de dados.

### 🚀 Como Executar o Projeto Localmente

Para rodar esta aplicação em seu ambiente de desenvolvimento, siga os passos detalhados abaixo.

#### Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes softwares instalados:

  * **Python 3.8+** (Durante a instalação no Windows, marque a caixa **"Add Python to PATH"**).
  * **Git** (para clonar o repositório).
  * **MySQL Server** (Anote a senha do usuário `root` que você criar durante a instalação).
  * Um editor de código como o **Visual Studio Code** com a extensão **Live Server**.

#### Passo a Passo para a Instalação

1.  **Clone o repositório:** Abra seu terminal e execute o comando abaixo para criar uma cópia local do projeto.

    ```bash
    git clone https://github.com/Oliver4i2/nome-do-seu-repositorio.git
    ```

    *(Substitua a URL pela do seu repositório no GitHub)*

2.  **Acesse a pasta do projeto:**

    ```bash
    cd nome-do-seu-repositorio
    ```

3.  **Configure o Banco de Dados:**

      * Abra o MySQL Workbench e crie um novo "Schema" com o nome exato: `hemocentro_db`.
      * Dentro desse schema, abra o arquivo `schema.sql` (que está na pasta do projeto) e execute o script para criar e popular as tabelas.

4.  **Configure as Credenciais do Backend:**

      * Abra o arquivo `app.py` em seu editor.
      * Localize o dicionário `db_config` e preencha o campo `password` com a senha do seu usuário `root` do MySQL.

    <!-- end list -->

    ```python
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'SUA_SENHA_AQUI', # <--- IMPORTANTE!
        'database': 'hemocentro_db'
    }
    ```

      * **Atenção:** Nunca envie este arquivo com senhas reais para um repositório público.

5.  **Instale as Dependências Python:**

      * Crie um arquivo chamado `requirements.txt` na pasta do projeto com o seguinte conteúdo:
        ```
        Flask
        Flask-Cors
        mysql-connector-python
        Werkzeug
        ```
      * No terminal, dentro da pasta do projeto, execute o comando:
        ```bash
        # No Windows
        py -m pip install -r requirements.txt

        # No macOS/Linux
        pip3 install -r requirements.txt
        ```

6.  **Execute a Aplicação (2 Terminais):**

      * **a) Inicie o servidor Back-end:** No seu primeiro terminal, execute:

        ```bash
        python app.py
        ```

        *Deixe este terminal rodando.*

      * **b) Inicie o Front-end:** No Visual Studio Code, clique com o botão direito no arquivo `index.html` e selecione **"Open with Live Server"**.

7.  **Acesse a aplicação:** Seu navegador abrirá o site. A partir daí, você pode navegar, se cadastrar na página `login.html` e testar todas as funcionalidades.

### 📂 Estrutura de Pastas

```
junho-vermelho/
|-- imagens/
|   |-- prosangue.png
|   `-- (outras imagens dos hemocentros e borda)
|-- app.py             # Arquivo principal do Flask (Back-end)
|-- index.html         # Página principal da campanha
|-- login.html         # Página de login e cadastro de usuários
|-- style.css          # Folha de estilos principal
|-- schema.sql         # Script para criar as tabelas do banco de dados
|-- requirements.txt   # Dependências do Python
`-- README.md          # Este arquivo de documentação
```

-----

Feito com ❤️ para conscientizar sobre um gesto que salva vidas.

   Autor: Pedro Oliveira
   GitHub: [https://github.com/Oliver4i2](https://github.com/Oliver4i2)



