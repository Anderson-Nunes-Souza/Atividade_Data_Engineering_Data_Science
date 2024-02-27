# Atividade Data Engineering & Data Science

 O objetivo deste projeto é complementar o conhecimento técnico obtido ao longo desta disciplina em um projeto de engenharia e análise de dados que envolve ingestão, armazenamento e análise de dados. A seguir uma breve descrição dos tópicos que serão abordados:

Ingestão de dados: Construir uma aplicação que ingere dados do CoinMarketCap, os transforma e os carrega em um armazenamento de dados.
Modelagem de dados e design de banco de dados: Construa um modelo de dados e projete um esquema de banco de dados para o armazenamento.
Análise de dados: Crie gráficos que apresentem:
O preço do Bitcoin nos últimos 5 anos. Utilize a figura 1 como exemplo.
Gráfico do tipo candlestick nos últimos 30 dias do Bitcoin. Utilize a figura 2 como exemplo. 

# Executando o Projeto

   #  1 - Mongo Db
   Para instalar e configurar o MongoDB em seu sistema, siga estas etapas gerais. As instruções específicas podem variar dependendo do sistema operacional que você está usando.
      1.1 Baixe o MongoDB:
      Ubuntu:
      bash

      sudo apt update
      sudo apt install mongodb

      CentOS:
      bash

      sudo yum update
      sudo yum install mongodb

      macOS (com Homebrew):

      bash

      brew tap mongodb/brew
      brew install mongodb-community

      Windows:

      Baixe o instalador do MongoDB do site oficial: MongoDB Download Center

      1.2 Inicie o MongoDB:
      Ubuntu / CentOS:

      O serviço deve ser iniciado automaticamente após a instalação. Você pode verificar o status com:

      bash

      sudo systemctl status mongodb

      macOS:

      Você pode iniciar o MongoDB com o comando:

      bash

      brew services start mongodb-community

      Windows:

      Depois de instalar o MongoDB, ele deve estar em C:\Program Files\MongoDB\Server\{version}\bin. Abra o prompt de comando como administrador e navegue até este diretório. Em seguida, execute:

      bash
      mongod

      Após executar o mongod, abrir o MongoDb Compass e conectar ao Localhost

   # 2 executar o ambiente
      Esse projeto contém as bibliotecas utilizadas já disponíveis na pasta myenv portanto deve funcionar sem a necessidade de realizar instalação dos módulos.
      na raiz do projeto, executar:
      
      bash
      .\myenv\Scripts\activate

   # 3 Executando o Projeto.
      3.1 Acessar a raiz do projeto e executar o Script "coinMarketCall.py".
      Ao ser executado, ele guardará as informações dentro do MongoDB.

      3.2 Gerando os gráficos
      Na pasta raiz do projeto, executar o comando "jupyter notebook" e acessar o arquivo "readMongodb.ipynb" que aparecerá na lista.
      No servidor do Jupyter, selecionar a opção "Run" e em seguida, "Run All Cells"



# Bibliotecas Python utilizadas
   Instalação myenv para python
   rodar o comando .\myenv\Scripts\activate
   import requests
   import datetime
   import json
   from pymongo import MongoClient
   import pandas as pd
   from pymongo import MongoClient