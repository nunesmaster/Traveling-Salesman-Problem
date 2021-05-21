# Traveling-Salesman-Problem

## Installation

São usadas as bibliotecas matplotlib, numpy, math e random

as bibliotecas math e random são instaladas ao mesmo tempo que é instalado o python

o seguinte comando instala a biblioteca matplotlib e numpy
    sudo apt-get install python3-matplotlib

É usada a versao 3.8.5 do python

## Usage

1. O programa gera aleatoriamente n pontos com coordenadas inteiras
2 a) Determina um candidato a solução gerando uma permutação qualquer dos pontos
2 b) Aplica a heurística nearest-neighbour-first 
3 Determina a vizinhança aplicando o "2-exchange"
4 a) Utiliza a heuristica "best-improvement-first"
4 b) Utiliza a heuristica "first-improvement"
4 c) Escolhe o candidato com menos cruzamentos de arestas
4 d) Escolhe um candidato qualquer na vizinhança

```python


python3 Points.py

1. Primeiro indicar o número de pontos que quer gerar
2. Indicar o valor da coordenada mais baixa
3. Indicar o valor da coordenada mais alta
4. É gerado o primeiro candidato e é imprimido na consola
5. Indicar a opção que pretende de modo a gerar um plot para vizualizar o candidato
6. Para sair escolher a opção 7

