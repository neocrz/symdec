# Análise Semantica de Sintomas e Frequência de Termos para Diagnóstico Médico

O presente projeto propõe um código para análise de sintomas especificados pelo paciente, a fim de verificar a probabilidade de relações com certas doenças através da realização de análise de term frequency com base em um dataset de doenças disponível no [Kaggle](https://www.kaggle.com/datasets/niyarrbarman/symptom2disease/data). 

## Funcionamento
A ferramenta funcionará da seguinte forma:

- O usuário fornecerá uma frase que descreve os sintomas.
- O algoritmo de análise irá classificar as doenças mais prováveis, com base em vetores e frequência de termos.
- O algoritmo irá retornar uma sequência ordenada de doenças e a probabilidade delas.
- O usuário irá tomar os resultados para ajudá-lo na tomada de decisão.


## Instalação
Para utilizar o programa: 
1. clone o repositório:
```console
git clone https://github.com/neocrz/
```

2. Obtenha o arquivo `Symptom2Disease.csv` no site do [Kaggle](https://www.kaggle.com/datasets/niyarrbarman/symptom2disease/data) e coloque na pasta `data`

3. Crie um ambiente python e ative o ambiente
```console
python -m venv venv

# windows 
.\venv\Scripts\activate
```

4. Instale as dependências python

```console
pip install -r requirements.txt
```

5. Execute e entre com a string que descreve os sintomas (em inglês):
```
python main.py
```
