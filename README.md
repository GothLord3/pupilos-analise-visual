# Analisador Magnojet

Identifica e conta bicos de pulverização Magnojet da linha PB-IA em fotografias. Trabalho acadêmico da equipe Pupilos.

## Abrir o programa

Com Python 3.12, abra um terminal na pasta extraída e instale todas as dependências, incluindo o Streamlit.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No Windows, depois da instalação, dê dois cliques em `Abrir Analisador Magnojet.bat`. Se preferir abrir a interface pelo PowerShell, execute:

```powershell
.\.venv\Scripts\python.exe -m analisador_magnojet --interface
```

No macOS ou Linux, crie o ambiente com `python3.12 -m venv .venv`, instale com `.venv/bin/python -m pip install -r requirements.txt` e abra com `.venv/bin/python -m analisador_magnojet --interface`.

O Streamlit abre no navegador. Se a página não abrir automaticamente, acesse `http://127.0.0.1:8501` ou use o endereço exibido no terminal. Para encerrar, pressione `Ctrl+C` no terminal.

## Usar a interface

- **Análise** permite anexar fotos ou capturar com a câmera. Para acumular capturas, use **Adicionar foto ao lote** entre elas. O modelo padrão é **Oficial-v1**, com confiança de 50% e resolução de 960 px. Clique em **Analisar** para ver as imagens marcadas e a contagem por classe.
- **Histórico** lista os lotes de `runs/analises`. Cada lote tem imagens marcadas, contagens, coordenadas e um JSON para baixar. Uma foto sem caixas indica ausência de detecção acima do limiar.
- **Estoque e financeiro** permite registrar ou editar a quantidade e o valor unitário de cada classe. O programa soma os subtotais em reais e grava as edições em `estoque.json`.

## Terminal

Use o Python do ambiente virtual nos comandos seguintes.

```text
python -m analisador_magnojet "caminho/da/foto.jpg"
python -m analisador_magnojet "caminho/das/fotos" --confianca 0.25
python -m scripts.conferir_dataset
python -m scripts.modelos
python -m scripts.avaliar_modelos
python -m scripts.testar_analise rapido
python -m scripts.testar_analise base
python -m scripts.testar_analise ampliado
python -m scripts.testar_analise classe --classe PBIA-06
python -m scripts.testar_analise classe --classe todas
python -m scripts.testar_analise online
python -m scripts.treinar base --epocas 16
python -m scripts.treinar ampliado --epocas 10
python -m scripts.treinar ajuste --epocas 6 --inicial modelos/ampliado.pt
```

`runs/analises` guarda análises de uso, `runs/testes` recebe os testes dos scripts e `runs/treinos` recebe novos experimentos com pesos e métricas. O modelo padrão está definido em `modelos/catalogo.json`.

## Dados e fontes

`Bicos de Pulverização` guarda os originais com nomes padronizados. `dataset` concentra a base YOLO com as 84 fotos, as variações organizadas por transformação e as imagens de avaliação externa. `analise_dados/resumo.json` tem o inventário verificável. O catálogo, o seminário e a exportação original do Roboflow ficam em `fontes`. Coloque ali o arquivo final do grupo quando estiver disponível.

As tabelas de treino estão em `docs/RESULTADOS.md`.
