# Funcionamento por arquivo

A interface e o terminal chamam a mesma função de análise. Ela lê as fotos, aplica o detector, grava os JPGs e publica o JSON por último. A interface usa esse JSON para reabrir o lote e localizar as imagens. O estoque é editado separadamente e não depende de uma detecção.

## Arquivos incluídos

.github/workflows/testes.yml: Executa a conferência do dataset no GitHub Actions a cada push ou pull request. Configura Python 3.12, instala Pillow e chama scripts.conferir_dataset.

.gitignore: Exclui ambiente virtual, cache, saídas locais, arquivo de estoque e trava dos arquivos versionados.

Abrir Analisador Magnojet.cmd: Entra na pasta do projeto e abre app.py com Streamlit em 127.0.0.1. Usa o Python de .venv quando instalado.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-01.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-02.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-03.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-04.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-05.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-06.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-07.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-08.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-09.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-10.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-11.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-12.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-13.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/mesa/mesa-14.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/sofa/sofa-01.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/sofa/sofa-02.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/sofa/sofa-03.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/sofa/sofa-04.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/sofa/sofa-05.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/Mistas/sofa/sofa-06.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-01.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-02.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-03.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-04.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-05.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-06.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-07.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-08.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-09.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-10.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-01/PBIA-01-11.jpg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-015/PBIA-015-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-015/PBIA-015-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-015/PBIA-015-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-015/PBIA-015-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-015/PBIA-015-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-015/PBIA-015-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-07.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-02/PBIA-02-08.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-07.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-08.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-09.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-10.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-025/PBIA-025-11.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-03/PBIA-03-07.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-04/PBIA-04-07.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-05/PBIA-05-07.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-01.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-02.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-03.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-04.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-05.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-06.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

Bicos de Pulverização/PB-IA/PBIA-06/PBIA-06-07.jpeg: Fotografia original renomeada. Os bytes são os mesmos do acervo recebido.

FUNCIONAMENTO.md: Este índice descreve os arquivos estáticos da entrega e os gerados em uso.

LICENSE: Aviso de direitos sobre o material original da equipe Pupilos e indicação das condições próprias dos materiais de terceiros.

README.md: Apresenta o programa, instalação, interface, comandos e estrutura de dados.

analisador_magnojet/__init__.py: Define RAIZ como a pasta acima do pacote, permitindo localizar arquivos por caminhos absolutos internos.

analisador_magnojet/__main__.py: Valida a entrada do terminal, aceita imagem ou pasta recursiva, chama a análise e imprime a pasta de saída com a contagem.

analisador_magnojet/analise.py: Lê o catálogo, carrega os pesos YOLO, normaliza orientação, detecta oito classes em CPU, desenha caixas, numera detecções e grava JPGs e resultados.json por lote. As coordenadas do JSON são x1, y1, x2, y2 em pixels da foto orientada. A confiança é de 0 a 1, o tamanho é o lado de entrada e a supressão de duplicatas usa IoU 0,50 entre classes.

analisador_magnojet/arquivos.py: Lê JSON UTF-8, grava JSON por substituição atômica e calcula SHA-256 lendo o arquivo como fluxo.

analisador_magnojet/dataset.py: Carrega as oito classes, identifica extensões aceitas, resolve rótulos YOLO e seleciona imagens por grupo ou por uma classe isolada.

analisador_magnojet/estoque.py: Consulta estoque.json e atualiza o registro de uma classe com trava de arquivo. O valor unitário é persistido como centavos inteiros.

analisador_magnojet/metricas.py: Calcula IoU pela interseção dividida pela união. Pareia caixas de mesma classe por maior IoU, uma a uma, e calcula precisão, revocação, F1 e erro absoluto médio de contagem.

analise_dados/resumo.json: Inventário de originais, grupos, divisões, caixas por classe, procedência, negativos e variações.

app.py: Cria três telas no Streamlit. Análise controla modelo, resolução, confiança e lote de câmera ou upload. Histórico lista os JSONs prontos e lê as imagens salvas. Estoque mostra e edita os itens e calcula o total em reais.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-08-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-09-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-10-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-01-11-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-015-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-015-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-015-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-015-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-015-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-015-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-02-08-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-08-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-09-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-10-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-025-11-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-03-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-04-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-05-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-01-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-02-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-03-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-04-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-05-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-06-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/images/PBIA-06-07-luz-e-desfoque.jpg: Variação de luz-e-desfoque, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-08-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-09-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-10-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-01-11-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-015-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-015-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-015-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-015-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-015-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-015-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-02-08-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-08-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-09-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-10-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-025-11-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-03-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-04-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-05-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-01-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-02-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-03-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-04-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-05-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-06-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/luz-e-desfoque/labels/PBIA-06-07-luz-e-desfoque.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-08-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-09-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-10-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-01-11-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-015-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-015-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-015-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-015-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-015-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-015-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-02-08-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-08-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-09-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-10-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-025-11-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-03-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-04-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-05-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-01-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-02-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-03-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-04-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-05-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-06-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/images/PBIA-06-07-recorte-e-fundo.jpg: Variação de recorte-e-fundo, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-08-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-09-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-10-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-01-11-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-015-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-015-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-015-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-015-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-015-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-015-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-02-08-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-08-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-09-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-10-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-025-11-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-03-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-04-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-05-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-01-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-02-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-03-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-04-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-05-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-06-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/recorte-e-fundo/labels/PBIA-06-07-recorte-e-fundo.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/images/PBIA-01-01-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-02-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-04-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-05-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-06-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-07-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-08-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-09-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-10-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-01-11-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-015-01-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-015-02-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-015-03-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-015-04-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-015-05-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-015-06-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-01-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-02-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-04-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-05-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-06-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-07-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-02-08-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-01-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-02-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-04-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-05-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-06-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-07-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-08-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-09-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-10-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-025-11-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-01-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-02-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-04-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-05-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-06-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-03-07-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-01-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-02-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-04-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-05-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-06-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-04-07-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-01-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-02-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-04-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-05-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-06-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-05-07-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-01-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-02-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-03-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-04-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-05-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-06-rotacao.jpg: Variação de rotacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/images/PBIA-06-07-rotacao.jpg: Variação de rotacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/rotacao/labels/PBIA-01-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-08-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-09-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-10-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-01-11-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-015-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-015-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-015-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-015-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-015-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-015-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-02-08-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-08-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-09-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-10-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-025-11-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-03-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-04-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-05-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-01-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-02-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-03-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-04-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-05-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-06-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/rotacao/labels/PBIA-06-07-rotacao.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/images/PBIA-01-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-04-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-04-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-06-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-06-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-07-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-07-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-08-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-08-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-09-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-09-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-10-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-10-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-11-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-01-11-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-04-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-04-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-06-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-015-06-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-04-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-04-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-06-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-06-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-07-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-07-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-08-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-02-08-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-04-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-04-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-06-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-06-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-07-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-07-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-08-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-08-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-09-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-09-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-10-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-10-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-11-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-025-11-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-01-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-01-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-04-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-04-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-06-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-06-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-07-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-03-07-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-04-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-04-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-06-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-06-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-07-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-04-07-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-04-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-04-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-06-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-06-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-07-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-05-07-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-01-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-01-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-02-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-02-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-03-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-03-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-04-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-04-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-05-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-05-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-06-0p8.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-06-1p2.jpg: Variação de saturacao, reservada para treino. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-07-0p8.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/PBIA-06-07-1p2.jpg: Variação de saturacao, reservada para consulta. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-01-teste-0p8.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-01-teste-1p2.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-02-teste-0p8.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-02-teste-1p2.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-03-teste-0p8.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-03-teste-1p2.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-04-teste-0p8.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-04-teste-1p2.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-05-teste-0p8.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-05-teste-1p2.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-06-teste-0p8.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/images/sofa-06-teste-1p2.jpg: Variação de saturacao, reservada para teste. Origem e fundo registrados em dataset/manifesto.json.

dataset/ampliado/saturacao/labels/PBIA-01-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-08-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-08-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-09-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-09-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-10-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-10-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-11-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-01-11-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-015-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-08-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-02-08-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-08-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-08-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-09-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-09-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-10-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-10-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-11-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-025-11-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-03-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-04-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-05-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-01-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-01-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-02-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-02-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-03-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-03-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-04-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-04-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-05-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-05-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-06-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-06-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-07-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/PBIA-06-07-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-01-teste-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-01-teste-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-02-teste-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-02-teste-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-03-teste-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-03-teste-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-04-teste-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-04-teste-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-05-teste-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-05-teste-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-06-teste-0p8.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/ampliado/saturacao/labels/sofa-06-teste-1p2.txt: Rótulo YOLO com as caixas correspondentes aos bicos desta imagem transformada.

dataset/base/test/images/sofa-01.jpg: Foto mista da divisão test, com 8 caixas PB-IA provenientes de Roboflow.

dataset/base/test/images/sofa-02.jpg: Foto mista da divisão test, com 8 caixas PB-IA provenientes de Roboflow.

dataset/base/test/images/sofa-03.jpg: Foto mista da divisão test, com 7 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/test/images/sofa-04.jpg: Foto mista da divisão test, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/test/images/sofa-05.jpg: Foto mista da divisão test, com 7 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/test/images/sofa-06.jpg: Foto mista da divisão test, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/test/labels/sofa-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/test/labels/sofa-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/test/labels/sofa-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/test/labels/sofa-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/test/labels/sofa-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/test/labels/sofa-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/images/PBIA-01-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-04.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-06.jpg: Foto individual da divisão train, com 2 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-07.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-10.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-01-11.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-015-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-015-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-015-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-015-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-02-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-02-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-02-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-02-04.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-02-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-02-07.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-04.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-07.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-08.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-09.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-025-10.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-03-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-03-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-03-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-03-06.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-03-07.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-04-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-04-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-04-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-04-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-04-06.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-05-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-05-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-05-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-05-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-05-06.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-06-01.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-06-02.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-06-03.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-06-05.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/PBIA-06-06.jpg: Foto individual da divisão train, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/mesa-01.jpg: Foto mista da divisão train, com 5 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-02.jpg: Foto mista da divisão train, com 8 caixas PB-IA provenientes de Roboflow.

dataset/base/train/images/mesa-04.jpg: Foto mista da divisão train, com 1 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-05.jpg: Foto mista da divisão train, com 2 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-07.jpg: Foto mista da divisão train, com 3 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-08.jpg: Foto mista da divisão train, com 0 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-09.jpg: Foto mista da divisão train, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-11.jpg: Foto mista da divisão train, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-12.jpg: Foto mista da divisão train, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-13.jpg: Foto mista da divisão train, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/images/mesa-14.jpg: Foto mista da divisão train, com 8 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/train/labels/PBIA-01-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-10.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-01-11.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-015-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-015-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-015-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-015-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-02-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-02-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-02-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-02-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-02-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-02-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-08.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-09.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-025-10.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-03-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-03-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-03-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-03-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-03-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-04-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-04-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-04-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-04-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-04-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-05-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-05-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-05-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-05-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-05-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-06-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-06-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-06-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-06-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/PBIA-06-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-02.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-05.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-08.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-09.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-11.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-12.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-13.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/train/labels/mesa-14.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/images/PBIA-01-08.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-01-09.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-015-04.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-015-06.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-02-06.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-02-08.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-025-06.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-025-11.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-03-01.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-03-04.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-04-04.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-04-07.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-05-04.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-05-07.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-06-04.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/PBIA-06-07.jpg: Foto individual da divisão val, com 1 caixas PB-IA provenientes de Roboflow.

dataset/base/val/images/mesa-03.jpg: Foto mista da divisão val, com 5 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/val/images/mesa-06.jpg: Foto mista da divisão val, com 5 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/val/images/mesa-10.jpg: Foto mista da divisão val, com 5 caixas PB-IA provenientes de revisão visual pelo catálogo.

dataset/base/val/labels/PBIA-01-08.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-01-09.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-015-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-015-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-02-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-02-08.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-025-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-025-11.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-03-01.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-03-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-04-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-04-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-05-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-05-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-06-04.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/PBIA-06-07.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/mesa-03.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/mesa-06.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/base/val/labels/mesa-10.txt: Rótulo da foto base em formato YOLO, com classe, centro x/y, largura e altura normalizados.

dataset/classes.json: Lista ordenada das oito classes. O índice de cada posição é o inteiro gravado na primeira coluna dos rótulos YOLO. PBIA-25 foi padronizado para PBIA-025.

dataset/manifesto.json: Vincula cada foto base ao original renomeado, hash, divisão, grupo e fonte da anotação. Vincula cada variação à foto e ao fundo que a originaram e marca se pode ser usada para treino ou teste.

dataset/online/fontes.json: Registra origem e expectativa das fotos externas e referências do Roboflow. Inclui crédito e licença quando fornecidos pela origem.

dataset/online/images/bico_pbia_azul_google.jpg: Foto de avaliação externa. 1 bico PBIA-03; código PBIA-03 visível na foto, cor azul

dataset/online/images/hidrante.jpg: Foto de avaliação externa. zero bicos PBIA

dataset/online/images/roboflow-teste1.jpg: Foto de avaliação externa. Referência do teste do Roboflow. Endereço individual da foto indisponível.

dataset/online/images/roboflow-teste2.jpg: Foto de avaliação externa. Referência do teste do Roboflow. Endereço individual da foto indisponível.

dataset/online/images/roboflow-teste3.jpg: Foto de avaliação externa. Referência do teste do Roboflow. Endereço individual da foto indisponível.

dataset/online/labels/bico_pbia_azul_google.txt: Rótulo de referência para avaliação externa. Vazio quando a foto contém zero bicos PB-IA anotados.

dataset/online/labels/hidrante.txt: Rótulo de referência para avaliação externa. Vazio quando a foto contém zero bicos PB-IA anotados.

dataset/online/labels/roboflow-teste1.txt: Rótulo de referência para avaliação externa. Vazio quando a foto contém zero bicos PB-IA anotados.

dataset/online/labels/roboflow-teste2.txt: Rótulo de referência para avaliação externa. Vazio quando a foto contém zero bicos PB-IA anotados.

dataset/online/labels/roboflow-teste3.txt: Rótulo de referência para avaliação externa. Vazio quando a foto contém zero bicos PB-IA anotados.

docs/RESULTADOS.md: Compara configurações, métricas de treino e resultados em validação, fotos originais reservadas, versões com saturação e amostra online.

docs/treinos.json: Guarda o histórico de épocas, arquitetura, parâmetros, hashes, inicializações e métricas para os pesos registrados no catálogo.

fontes/catalogo-magnojet.pdf: Catálogo de referência da Magnojet, usado na revisão dos códigos e cores dos bicos.

fontes/roboflow-original.zip: Exportação original recebida do Roboflow. Preserva as anotações e os nomes de origem, inclusive uma classe PB presente no ZIP bruto. A base integrada usa só PB-IA.

fontes/seminario-projeto-integrador.pdf: Material de referência do seminário do projeto integrador.

modelos/ajuste.pt: Checkpoint YOLO11n treinado da versão ajuste, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/ampliado-ajuste-historico.pt: Checkpoint YOLO11n treinado da versão ampliado-ajuste-historico, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/ampliado-coco-historico.pt: Checkpoint YOLO11n treinado da versão ampliado-coco-historico, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/ampliado-historico.pt: Checkpoint YOLO11n treinado da versão ampliado-historico, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/ampliado.pt: Checkpoint YOLO11n treinado da versão ampliado, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/base.pt: Checkpoint YOLO11n treinado da versão base, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/catalogo.json: Liga o identificador de cada modelo ao arquivo .pt, SHA-256, tamanho e confiança padrão. O campo oficial define o padrão do programa.

modelos/piloto-controle.pt: Checkpoint YOLO11n treinado da versão piloto-controle, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/piloto-saturacao.pt: Checkpoint YOLO11n treinado da versão piloto-saturacao, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/roboflow-final.pt: Checkpoint YOLO11n treinado da versão roboflow-final, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/roboflow-inicial.pt: Checkpoint YOLO11n treinado da versão roboflow-inicial, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/roboflow-rotacao.pt: Checkpoint YOLO11n treinado da versão roboflow-rotacao, pronto para inferência. Parâmetros e resultados em docs/treinos.json.

modelos/yolo11n-coco.pt: Pesos YOLO11n pré-treinados em COCO usados como ponto de partida nos treinos novos base e ampliado.

requirements.txt: Lista dependências para leitura de imagens, YOLO, interface web e trava de gravação do estoque.

scripts/avaliar_modelos.py: Converte caixas de referência para pixels, executa inferência e mede quatro conjuntos com o limiar registrado. A função avaliar também pode escolher limiar pela validação.

scripts/conferir_dataset.py: Abre as imagens, verifica hash dos originais, pares imagem-rótulo, limites das caixas, classes e divisões. Imprime um inventário em JSON.

scripts/modelos.py: Confere o hash de cada checkpoint, combina catálogo com resultados de treino e exibe os dados técnicos.

scripts/testar_analise.py: Executa análise de três fotos, base, variações, online ou fotos de uma classe isolada. A opção todas cria um lote por classe.

scripts/treinar.py: Gera listas absolutas e configuração YOLO por rodada. Treina com os perfis base, ampliado ou ajuste, exportando pesos e resultados por época em runs/treinos.

## Arquivos gerados durante o uso

estoque.json: Registros por classe, com componente, modelo, quantidade e valor unitário em centavos.

estoque.json.lock: Trava usada enquanto o estoque é atualizado.

runs/analises/<lote>/imagem-001.jpg: Primeira imagem do lote com caixas, códigos e porcentagens. O número no nome indica a ordem da entrada.

runs/analises/<lote>/resultados.json: Horário com fuso, modelo, hash, parâmetros, contagens, caixas e erros de leitura. A existência deste arquivo torna o lote visível no histórico.

runs/testes/<lote>/resultados.json: Mesmo formato da análise de uso, gravado separadamente pelo script de teste.

runs/testes/<lote>/imagem-001.jpg: Foto marcada criada pelo script de teste.

runs/treinos/<rodada>/dataset.yaml: Configuração de caminhos e classes entregue ao YOLO.

runs/treinos/<rodada>/train.txt: Caminhos absolutos das imagens de treino.

runs/treinos/<rodada>/val.txt: Caminhos absolutos das imagens de validação.

runs/treinos/<rodada>/test.txt: Caminhos absolutos das imagens do teste original.

runs/treinos/<rodada>/args.yaml: Configuração da execução gravada pela Ultralytics.

runs/treinos/<rodada>/results.csv: Perdas e métricas nativas em cada época.

runs/treinos/<rodada>/treino.json: Perfil, inicialização, hardware lógico, parâmetros e histórico da rodada.

runs/treinos/<rodada>/weights/best.pt: Checkpoint de melhor validação segundo o critério nativo do YOLO.

runs/treinos/<rodada>/weights/last.pt: Checkpoint da última época executada.

runs/cache-yolo/Ultralytics/settings.json: Preferências geradas pela Ultralytics para o ambiente local.
