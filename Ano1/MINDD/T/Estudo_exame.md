# Modelos Preditivos

## Aprendizagem Baseada em Instâncias (KNN)

- Conhecido como o método dos k-vizinhos mais próximos
- a previsão de valores (discretos/contínuos) é feita com base nos valores mais próximos
- Baseia-se em dois conceitos:
    - Distância entre 2 registos
    - Combinação dos resultados através dos vizinhos
- Distância Euclidiana é usada para calcular a distância entre 2 pontos
- Normalização deve ser aplicada aos atributos
- Para uma função ser usada como distância as seguintes propriedades têm de ser válidas, para quaisquer p, q, d:
    - ![Propriedades](images/Propriedades-distancia.png)
    - 1: A distância entre 2 pontos não pode ser negativa
    - 2: A distância de um ponto a ele próprio é nula
    - 3: A ordem dos pontos não afeta a distância entre eles (simetria)
    - 4: A distância entre dois pontos é sempre menor ou igual à soma das distâncias de um ponto intermediário (Desigualdade triangular)
- Escola do K
    - O valor deve ser ímpar
    - A escolha deve ser experimental (o k com os melhores resultados, será o k escolhido)
    - Valores pequenos de k -> podem aumentar a contribuição de exemplos ruidosos
    - Valores maiores de k -> podem aumentar a contribuição de exemplos pouco similares, ou seja, menos relevantes
-Vantagens/desvantagens: 

| Aspecto                              | Vantagens                                                                                        | Desvantagens                                                                                                |
| -------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Processamento de variáveis dependentes | Processa qualquer número de variáveis dependentes                                                 | Computacionalmente intensivo no cálculo das distâncias entre casos                                        |
| Tipo de previsão                      | Pode ser usada para prever valores contínuos ou discretos                                         | Os resultados dependem da função distância usada, da função combinação e do número de vizinhos usados      |
| Função de distância                   | Qualquer função de distância pode ser usada                                                       | Necessita de grandes conjuntos de treino                                                                    |
| Implementação fácil                   | Fácil de implementar                                                                             | Sensibilidade a valores isolados e variáveis irrelevantes                                                  |
| Atualização do modelo                 | Facilmente atualizado por expansão ou substituição do conjunto de treino                         | Ausência de qualquer modelo para "mostrar" ao utilizador                                                  |
| Compreensão dos resultados            | É fácil entender os resultados                                                                  |                                                                                                            |

## Aprendizagem Baseada em Probabilidades (Naive Bayes)

- Teoria Bayesiana -> Usa dados do passado para estimar probabilidades de eventos futuros
    - Requer probabilidades à priorio
- A teria Bayesiana faz 2 assunções:
    - Os atributos são todos igualmente importantes
    - Os atributos são estatisticamente independentes
- Teoria da Probabilidade
    1. **Espaço Amostral (S):** O conjunto de todos os resultados possíveis de um experimento aleatório é chamado de espaço amostral.

    2. **Evento (E):** Um evento é um subconjunto do espaço amostral, ou seja, é um conjunto de resultados possíveis.

    3. **Probabilidade de um Evento (P(E)):** A probabilidade de um evento é uma medida numérica que representa a chance relativa de o evento ocorrer. A probabilidade de um evento está sempre no intervalo de 0 a 1.
        - $$ 0 \leq P(E) \leq 1 $$


    4. **Regra da Soma:** Para quaisquer dois eventos mutuamente exclusivos (eventos que não podem ocorrer simultaneamente), a probabilidade da união dos eventos é a soma das probabilidades dos eventos individuais.
        - $$ P(A \cup B) = P(A) + P(B) $$,
         se \( A \) e \( B \) são mutuamente exclusivos.

    5. **Regra Geral da Soma:** A probabilidade de qualquer evento pode ser encontrada pela soma das probabilidades dos eventos individuais e subtraindo a probabilidade da interseção dos eventos, se houver.
        - $$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$

    6. **Probabilidade Condicional:** A probabilidade condicional de um evento \(A\) dado que ocorreu um evento \(B\) é denotada por \(P(A|B)\) e é definida como a probabilidade de \(A\) ocorrer, dado que sabemos que \(B\) ocorreu.
        - $$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$


    7. **Regra do Produto:** A probabilidade da interseção de dois eventos, \(P(A \cap B)\), pode ser encontrada multiplicando a probabilidade de um evento pelo condicional do outro evento.
        - $$P(A \cap B) = P(A) \cdot P(B|A)$$

    8. **Eventos Independentes:** Dois eventos, \(A\) e \(B\), são independentes se a ocorrência (ou não ocorrência) de um evento não afeta a probabilidade do outro.
        - $$ P(A \cap B) = P(A) \cdot P(B) $$
- Classificador Bayesiano Naive (Ingénuo)
    - O **Classificador Bayesiano Naive** realiza a suposição ingênua, ou seja, assume que as variáveis \(a_1, a_2, ..., a_n\) são independentes. Seja \(v_j\) o valor do atributo a ser previsto para uma instância da amostra com \(n\) atributos preditivos \(a_1, a_2, ..., a_n\), a probabilidade do valor \(v_j\) do atributo a ser previsto é igual ao produto das probabilidades individuais de cada atributo.
    - ![f1](images/f1.png)
    - ![Alt text](images/f2-produto.png)
-  Suposição Naive Bayes
    - O **Naive Bayes** assume independência condicional de classe, o que implica que os eventos são considerados independentes quando condicionados ao mesmo valor de classe.
- Problemas do Classificador Bayesiano
    - Se a probabilidade condicional de um atributo for nula, a probabilidade da classe também será nula.

    - Se os exemplos de treino não cobrirem todos os valores possíveis dos atributos, a classificação de determinados registros pode se tornar impossível.
- Estimativa de Laplace
    - O problema anterior pode ser resolvido, usando a **estimativa de Laplace**
    - O **estimador de Laplace** envolve adicionar uma pequena quantidade a cada uma das contagens na tabela de frequência, garantindo que cada característica tenha uma probabilidade não nula. Geralmente, o estimador de Laplace é ajustado para 1, assegurando que cada combinação de características da classe esteja presente nos dados pelo menos uma vez.
- Teorema de Bayes
    - O **Teorema de Bayes** aplicado como classificador requer o conhecimento de:

    - Duas probabilidades a priori: \(P(\text{decisão}_i)\).
    - Uma probabilidade condicional: \(P(x|\text{decisão}_i)\).

    - Este classificador é ótimo no sentido de que, em média, nenhum outro classificador pode obter melhores resultados usando a mesma informação. No entanto, na prática, essas probabilidades são desconhecidas.

    - Estimar confiavelmente essas probabilidades a partir de um conjunto de exemplos requer um número infinito de exemplos.

    - São feitas simplificações no cálculo de \(P(x|\text{decisão})\), assumindo que os atributos são independentes da decisão.

    - O **Classificador Bayesiano Naive** é uma aplicação prática desse teorema, assumindo a independência condicional entre os atributos.
- Probabilidades a partir de Atributos Contínuos
    - Para lidar com atributos contínuos, é comum:

    - **Discretizar:**
        - Realizar uma partição baseada em dois valores, como \( (A < v) \) ou \( (A > v) \).

    - **Estimativa baseada na densidade de Probabilidade:**
        - Assume-se que o atributo segue uma distribuição normal ou binomial.
        - Utiliza-se a amostra para estimar os parâmetros da distribuição, como média (\(\mu\)) e desvio padrão (\(s\)).
    - Estima-se a probabilidade condicional \(P(A_i|c)\) usando a fórmula:

    $$ P(A_i|c) = \frac{1}{\sqrt{2\pi s^2}} \exp\left(-\frac{(A_i - \mu)^2}{2s^2}\right) $$

    - onde:
        - \(\mu\) é a média.
        - \(s\) é o desvio padrão.
        - \(A_i\) é o valor do atributo contínuo.

    Essa abordagem permite trabalhar com atributos contínuos no contexto do Classificador Bayesiano Naive, assumindo uma distribuição conhecida e estimando seus parâmetros a partir dos dados amostrais.
- Vantagens/Desvantagens:

| **Vantagens**                                  | **Desvantagens**                                      |
| ---------------------------------------------- | ------------------------------------------------------ |
| 1. Robusto no tratamento de valores isolados    | 1. Cálculo de um número elevado de probabilidades      |
| 2. Robusto no tratamento de atributos irrelevantes | 2. Necessidade de amostras suficientemente representativas (elevada dimensão) |
| 3. Fácil de implementar                        | 3. Suposição de independência condicional               |
| 4. Capaz de classificar amostras com valores ausentes | 4. Não capta dependências entre variáveis               |
| 5. Considera todos os atributos como igualmente importantes | 5. Desempenho pode ser afetado pela presença de atributos correlacionados |
| 6. Complexidade computacional linear em todas as variáveis do problema |                                                      |















 




