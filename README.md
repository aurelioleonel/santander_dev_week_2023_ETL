#### Explorando ETL com Python

Este projeto exemplifica um processo de extração, transformação e carregamento (ETL) de dados utilizando Python. O objetivo é realizar a leitura de um arquivo CSV contendo informações de clientes, aplicar transformações nestes dados e convertê-los para o formato JSON.

Inicialmente o arquivo CSV é lido utilizando a biblioteca Pandas, armazenando os dados em um DataFrame. Esta etapa representa a extração dos dados da fonte CSV.

Em seguida, algumas transformações são aplicadas nos dados como conversão do tipo de dados de algumas colunas e renomeação de cabeçalhos. Estas transformações limpam e preparam os dados para analise.

Os dados do DataFrame são então convertidos para o formato JSON, primeiro criando um dicionário Python a partir dos dados, para então serializar este dicionário em uma string JSON formatada e indentada. Esta etapa de conversão para JSON representa o carregamento dos dados estruturados em um novo formato.

Foram utilizadas as bibliotecas Pandas para extração e transformação dos dados tabulares, e o módulo nativo JSON da linguagem Python para serialização dos dicionários em JSON.

O processo realizado demonstra as principais etapas de um pipeline ETL utilizando Python, desde a extração dos dados brutos até o carregamento dos dados tratados em um formato desejado. As técnicas apresentadas podem ser expandidas para casos mais complexos de ETL.
