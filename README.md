# Classificador de predisposição ao AVC #


Para instalar as versões utilizadas no desenvolvimento, basta executar o seguinte comando no terminal:

`pip install -r requirements.txt`

A organização do repositório está feita de seguinte forma:

`main.py`: Arquivo contendo o backend em Python, desenvolvido com auxílio do framework Flask. Esse arquivo pode funcionar tanto com base no registro de dados em `db.py` - que faz o registro de dados no banco de dados ElephantSQL, que exige conexão com banco de dados externos,  e em `txt.py`- que fazo registro de dados de forma local, em arquivos de texto para facilitar o procedimento de teste, e remover custos. 

`ml_model.py`: Arquivo contendo a interface que implementa o modelo de Machine Learning, sendo utilizada pelo backend para obter o resultado da classificação do usuário.

`stroke_model.ipynb`: Arquivo contendo o desenvolvimento do modelo, bem como as análises estatísticas utilizadas.

`templates/`: Diretório contendo os arquivos .html que implementam a interface gráfica da aplicação.

`imagens/`: Diretório contendo arquivos de imagens utilizados na implementação da interface gráfica.
