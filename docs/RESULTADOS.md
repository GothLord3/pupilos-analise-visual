# Resultados de treino

O detector YOLO11n tem oito classes PB-IA. Caixas de outras famílias ficam como fundo. A base reúne 84 fotos, com 59 de treino, 19 de validação e seis de teste. As 332 variações incluem 201 admitidas no treino e 12 reservadas para medir sensibilidade à saturação. As cinco imagens externas ficam fora dos três treinos novos. As divisões seguem grupos visuais do acervo e podem compartilhar exemplares.

## Seleção do modelo

O oficial é **Oficial-v1**, com confiança de 50% e inferência a 960 px. O F1 médio de validação foi 0.923, considerando os 19 originais e as 41 variações de validação em grupos separados. Cada acerto exige classe igual e IoU de pelo menos 0,50, sem reutilizar caixas. Uma foto inteira só é acertada quando todas as caixas de referência correspondem às previsões e sobram zero caixas. Os pesos históricos ficam disponíveis para comparação. Seus treinos podem ter visto fotos que hoje estão reservadas, incluindo imagens da validação e do teste externo do Roboflow. A comparação entre esses pesos é descritiva.

## Avaliação com o limiar de cada versão

Cada célula mostra **fotos completas/total · F1 por objeto**. As seis fotos originais de teste são arranjos no sofá. O teste ampliado usa duas saturações de cada uma delas. A amostra online reúne três referências do Roboflow e duas imagens de fontes externas. A amostra online é pequena e não estabelece desempenho em campo.

| Modelo | Grupo | Confiança | Validação original | Teste original | Teste ampliado | Online |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| **Oficial-v1** | oficial | 50.0% | 15/19 · 0.897 | 0/6 · 0.455 | 0/12 · 0.419 | 1/5 · 0.250 |
| piloto-controle | histórico | 50.0% | 16/19 · 0.815 | 0/6 · 0.231 | 0/12 · 0.214 | 2/5 · 0.533 |
| piloto-saturacao | histórico | 50.0% | 16/19 · 0.750 | 0/6 · 0.259 | 0/12 · 0.243 | 1/5 · 0.500 |
| roboflow-inicial | histórico | 50.0% | 0/19 · 0.000 | 0/6 · 0.000 | 0/12 · 0.000 | 1/5 · 0.000 |
| roboflow-final | histórico | 25.0% | 16/19 · 0.882 | 0/6 · 0.600 | 0/12 · 0.579 | 0/5 · 0.286 |
| roboflow-rotacao | histórico | 30.0% | 14/19 · 0.571 | 0/6 · 0.000 | 0/12 · 0.000 | 1/5 · 0.222 |
| ampliado-historico | histórico | 25.0% | 15/19 · 0.620 | 0/6 · 0.091 | 0/12 · 0.104 | 0/5 · 0.000 |
| ampliado-ajuste-historico | histórico | 50.0% | 16/19 · 0.627 | 0/6 · 0.000 | 0/12 · 0.000 | 0/5 · 0.000 |
| ampliado-coco-historico | histórico | 50.0% | 16/19 · 0.604 | 0/6 · 0.000 | 0/12 · 0.019 | 1/5 · 0.250 |
| ajuste | novo | 2.5% | 12/19 · 0.618 | 0/6 · 0.354 | 0/12 · 0.379 | 0/5 · 0.250 |
| ampliado | novo | 7.5% | 8/19 · 0.406 | 0/6 · 0.231 | 0/12 · 0.237 | 2/5 · 0.333 |
| base | novo | 1.0% | 2/19 · 0.222 | 0/6 · 0.000 | 0/12 · 0.000 | 1/5 · 0.105 |

## Configurações e métricas nativas dos treinos

O mAP50–95 máximo por época vem da validação usada no respectivo treino. As bases históricas têm divisões diferentes. O JSON contém parâmetros, histórico por época, precisão, revocação, F1, erros de contagem e os hashes dos pesos.

| Modelo | Base de treino | Inicialização | Épocas | Entrada | Otimizador | LR inicial | Camadas congeladas | mAP50–95 máximo |
| --- | --- | --- | ---: | ---: | --- | ---: | ---: | ---: |
| piloto-controle | roboflow-pbia-ampliado-298-v1 | pupilos-pbia-yolo11n.pt | 8 | 640 | AdamW | 0.0003 | 10 | 0.460 |
| piloto-saturacao | roboflow-pbia-saturacao-20261103 | pupilos-pbia-yolo11n.pt | 8 | 640 | AdamW | 0.0003 | 10 | 0.443 |
| roboflow-inicial | roboflow-pbia | yolo11n.pt | 34 | 640 | AdamW | 0.001 | None | 0.007 |
| roboflow-final | roboflow-pbia | retreino-pbia-20261102-final-inicial.pt | 77 | 640 | AdamW | 0.0003 | 10 | 0.579 |
| roboflow-rotacao | roboflow-pbia | last.pt | 23 | 640 | AdamW | 0.001 | None | 0.042 |
| ampliado-historico | roboflow-pbia-ampliado-298-v1 | retreino-pbia-ampliado-20261102-inicial.pt | 1 | 640 | AdamW | 0.0003 | 10 | 0.168 |
| ampliado-ajuste-historico | roboflow-pbia-ampliado-298-v1 | last.pt | 16 | 640 | AdamW | 0.0003 | 0 | 0.011 |
| ampliado-coco-historico | roboflow-pbia-ampliado-298-v1 | yolo11n.pt | 19 | 640 | AdamW | 0.0003 | 10 | 0.058 |
| ajuste | base + 201 variações | ampliado.pt | 6 | 480 | SGD | 0.004 | 5 | 0.696 |
| ampliado | base + 201 variações | yolo11n-coco.pt | 10 | 320 | AdamW | 0.001 | 5 | 0.524 |
| base | base | yolo11n-coco.pt | 16 | 320 | AdamW | 0.002 | 0 | 0.127 |

O ajuste de 480 px parte do peso do treino ampliado, aplica SGD com taxa inicial 0,004 e usa a mesma divisão. As imagens de teste alteradas medem somente robustez a saturação. As anotações recuperadas por revisão visual e a identificação comercial das classes podem ser conferidas pelo grupo antes de uso operacional.
