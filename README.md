# Analisador Magnojet

Aplicação de visão computacional para identificação e contagem de bicos de pulverização Magnojet da linha PB-IA em fotografias. O projeto foi desenvolvido como trabalho acadêmico pela equipe Pupilos.

## Instalação

O projeto utiliza Python 3.12. No Windows, execute os comandos abaixo na pasta do projeto:

```cmd
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No macOS ou Linux:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Execução

No Windows, abra `Abrir Analisador Magnojet.bat` ou execute:

```cmd
.\.venv\Scripts\python.exe -m analisador_magnojet --interface
```

A interface permite selecionar fotografias, executar a identificação, consultar análises anteriores e registrar informações de estoque. Também é possível analisar uma imagem ou pasta pelo terminal:

```cmd
.\.venv\Scripts\python.exe -m analisador_magnojet caminho\da\foto.jpg
.\.venv\Scripts\python.exe -m analisador_magnojet caminho\das\fotos --confianca 0.25
```

## Base de imagens

A base contém 84 fotografias originais, separadas em 59 imagens de treino, 19 de validação e 6 de teste. Foram produzidas 332 variações controladas de rotação, iluminação, desfoque, saturação, recorte e fundo. Destas, 201 são utilizadas em conjunto com as imagens originais durante os ajustes do modelo.

As classes identificadas são PBIA-01, PBIA-015, PBIA-02, PBIA-025, PBIA-03, PBIA-04, PBIA-05 e PBIA-06. As divisões foram organizadas por grupos visuais para reduzir a semelhança entre as imagens de treino, validação e teste.

## Modelo oficial

Durante o desenvolvimento foram avaliadas diferentes configurações da base, resolução de entrada, taxa de aprendizado, otimizador e ajustes dos pesos. O modelo escolhido para a aplicação foi o **Oficial-v1**, utilizado com confiança de 50% e resolução de 960 px.

| Conjunto | Imagens completamente identificadas | Total de imagens | F1 por objeto |
| --- | ---: | ---: | ---: |
| Validação original | 15 | 19 | 0,897 |
| Teste original | 0 | 6 | 0,455 |
| Teste ampliado | 0 | 12 | 0,419 |
| Amostra online | 1 | 5 | 0,250 |

O F1 médio de validação foi 0,923 quando as imagens originais e as variações de validação foram consideradas nos grupos previstos pelo experimento. Uma detecção é considerada correta quando a classe coincide com a anotação e a interseção sobre união é igual ou superior a 0,50.

Os resultados completos dos modelos avaliados estão em [`docs/RESULTADOS.md`](docs/RESULTADOS.md).

## Organização do projeto

- `analisador_magnojet`: módulos de análise e persistência;
- `dataset`: imagens, anotações e divisões da base;
- `modelos`: pesos utilizados pelo programa;
- `scripts`: conferência, avaliação e ajuste do modelo;
- `docs`: resultados dos experimentos;
- `fontes`: documentos utilizados na elaboração do projeto.
