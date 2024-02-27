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
      sudo apt update
      sudo apt install mongodb

   CentOS:
      sudo yum update
      sudo yum install mongodb

   macOS (com Homebrew):
      brew tap mongodb/brew
      brew install mongodb-community

   Windows:

   Baixe o instalador do MongoDB do site oficial: MongoDB Download Center

      1.2 Inicie o MongoDB:
      Ubuntu / CentOS:

   O serviço deve ser iniciado automaticamente após a instalação. Você pode verificar o status com:
      sudo systemctl status mongodb

   macOS:
   Você pode iniciar o MongoDB com o comando:

      brew services start mongodb-community

   Windows:

   Depois de instalar o MongoDB, ele deve estar em C:\Program Files\MongoDB\Server\{version}\bin. Abra o prompt de comando como administrador e navegue até este diretório. Em seguida, execute:

      mongod

   Após executar o mongod, abrir o MongoDb Compass e conectar ao Localhost clicando em 'Save & Connect'

   # 2 executar o ambiente
   Esse projeto contém as bibliotecas utilizadas já disponíveis na pasta myenv portanto deve funcionar sem a necessidade de realizar instalação dos módulos.
   Na raiz do projeto, executar:
      .\myenv\Scripts\activate

   # 3 Executando o Projeto.
   3.1 Acessar a raiz do projeto e executar o Script "coinMarketCall.py".
   Ao ser executado, ele guardará as informações dentro do MongoDB.

   3.2 Gerando os gráficos
   Na pasta raiz do projeto, executar o comando: 
      "jupyter notebook" 
   
   Depois acessar o arquivo "readMongodb.ipynb" que aparecerá na lista.
   No servidor do Jupyter, selecionar a opção "Run" e em seguida, "Run All Cells"



# Bibliotecas Python (caso alguma não funcione!)
Todas as bibliotecas citadas abaixo já estão instaladas no diretório "myenv", caso alguma informe problema, é só realizar a instalação
após executar o ambiente myenv

1 - Instalação myenv para python
   rodar o comando .\myenv\Scripts\activate

2 - realizar a instalação das bibliotecas: 
Requests
   pip install requests
import datetime
   pip install datetime
import json
   pip install json
from pymongo import MongoClient
   pip install MongoClient
import pandas as pd
   pip install pandas
import pprint
   pip install pprint
import matplotlib.pyplot as plt
   pip install matplotlib
import mplfinance as mpf
   pip install mplfinance
import mplcursors
   pip install mplcursors
