# Respostas aos exames de 21-22

## Exame normal

#### **Pergunta 1** : Considere que o diagnóstico de problemas numa máquina pode ser obtido através da identificação de sequências típicas de eventos que ocorrem durante o funcionamento da máquina, ou seja, a diferentes tipos de avarias é possível associar sequências prováveis de eventos. Se pretendermos implementar um sistema de diagnóstico baseado em conhecimento, qual seria o formalismo de representação de conhecimento mais apropriado para a construção da base de conhecimento deste sistema? Indique ainda as circunstâncias em que tal sistema poderá ser classificado como event driven ou data driven. Justifique a sua resposta

- O conhecimento deveria ser representado como procedimental, assim seria possível definir/seguir sequências de conhecimento específicas para cada avaria.

- Eis as circustâncias em que será event-driven e data-driven:
    - Sistema Event-Driven:
        - Definição: Um sistema event-driven responde a eventos em tempo real ou quase real, ativando procedimentos específicos em resposta a esses eventos.
        - Circunstâncias: Quando o sistema precisa reagir imediatamente a eventos específicos para evitar falhas ou danos.
        - Exemplo: Um evento de temperatura elevada ativa imediatamente uma sequência de diagnóstico e ações corretivas.

    - Sistema Data-Driven:
        - Definição: Um sistema data-driven analisa grandes quantidades de dados coletados ao longo do tempo para identificar padrões e tendências que informam o diagnóstico.
        - Circunstâncias:
        Quando o sistema usa dados históricos e estatísticas para identificar padrões que precedem falhas.
        - Exemplo: Analisando dados históricos de vibração e temperatura para prever falhas antes que ocorram, baseando-se em procedimentos derivados de padrões de dado


#### **Pergunta 2**: Indique de que forma são representados os factos presentes na memória de trabalho do Drools. Descreva ainda os passos necessários para incluir um facto na memória de trabalho do Drools.

- Os factos são objetos/classes java, que são adicionados durante a seesão através de inserts
- Tutorial de como criar factos:
    - Criar a classe do facto
    - Criar regras
    - Configurar a sessão
    - Inserir factos
    - Disparar regras


#### **Pergunta 3**: 

- A-> Como o bro drools tem um mecanismos de especificidade, este irá disparar a regra 2, pois é a mais específica (tem mais premissas), tendo em conta, que tanto a 1 e a 2 disparam na presença do factoA

- B-> Como o drools tem um mecanismo de prioridades, teríamos de atribuir saliências às regras, sendo que a da regra 2 seria maior, ou seja, seria a regra mais prioritária.


#### **Pergunta 4**: Indique em que situações a lógica difusa é especialmente adequada para a implementação de sistemas baseados em conhecimento.

- A lógica difusa permite tratar de fontes de incerteza onde está presente o uso de linguagem. É mais fácil para representar situações em que o conhecimento literal não seja útil, exemplo:

```
Em muitos casos, a precisão pode ser um tanto inútil, enquanto instruções vagas
podem ser melhor interpretadas e realizadas
Exemplo de compreensão humana
– Invulgar:
“Comece a travar 10 metros antes do sinal STOP”
– Vulgar:
“Comece a travar perto da faixa dos peões”
```

#### **Pergunta 5**: Considere que a sua casa dispõe de um sistema de alarme. Quando o alarme é acionado, às vezes os seus vizinhos, John e Mary, ligam para si. As chamadas de John e Mary (johnCalls e maryCalls) são eventos independentes. Considere a seguinte regra probabilística para definir as relações entre esses eventos:

- A->
    - LSJohn = 18
    - LNJohn = 0.11
    - LsMary = 70
    - LNMary = 0.3

- B P(H|E1 AND ~E2) -> dunno
ver ficheiro html


- C => O(H|E1 AND E2) = 18*70*0.001 = 1.26 -> converter para probabilidade = 0.56
- P(H|E1 AND E2) = 0.


## Exame recurso

#### **Pergunta 1**: O raciocínio abdutivo é um dos mecanismos que pode ser usado para implementar mecanismos de inferência. Explique em que consiste este tipo de raciocínio e estabeleça um paralelismo entre a aplicação deste mecanismo de raciocínio na implementação de um motor de inferência e a forma como um perito usa este tipo de raciocínio para gerar inferência. Indique de que forma este mecanismo de raciocínio está relacionado com o mecanismo de raciocínio não-monotónico.

- Este tipo de racíocinio segue esta lógica:
    - Observamos algo como sendo verdadeiro e conjecturamos sobre o que
    pode ter levado a essa observação
    - Tipo de raciocínio usado geralmente na produção de explicações
    - Não garante que se chegue a conclusões verdadeiras


O raciocínio abdutivo é um tipo de raciocínio que parte de uma observação ou de um conjunto de dados específicos para inferir uma explicação plausível ou uma hipótese que possa explicar esses dados. Em outras palavras, é uma forma de raciocínio que vai do efeito à causa, tentando encontrar a melhor explicação para um conjunto de observações.

### Raciocínio Abdutivo na Implementação de um Motor de Inferência

Na implementação de um motor de inferência, o raciocínio abdutivo é utilizado para fazer deduções a partir de observações ou evidências disponíveis. Aqui estão alguns passos que podem ilustrar como isso ocorre:

1. **Observação de Dados**: O motor de inferência recebe um conjunto de dados ou fatos observados.
   
2. **Identificação de Padrões**: Utilizando regras e conhecimento prévio (base de conhecimento), o motor de inferência busca identificar padrões ou relações entre os dados observados.

3. **Inferência Abdutiva**: Com base nos padrões identificados, o motor de inferência realiza raciocínio abdutivo para gerar explicações plausíveis ou hipóteses que justifiquem os dados observados. Essas hipóteses são consideradas como sendo as mais prováveis dadas as informações disponíveis.

4. **Geração de Conclusões**: A partir das hipóteses geradas, o motor de inferência pode então gerar novas conclusões ou inferências que não estavam diretamente presentes nos dados observados inicialmente.

### Paralelismo com o Raciocínio de um Perito

Um perito humano utiliza o raciocínio abdutivo de maneira similar ao motor de inferência, especialmente em domínios onde há uma base de conhecimento extensa e experiência acumulada:

1. **Observação e Análise**: O perito analisa uma situação ou conjunto de dados específicos.

2. **Identificação de Padrões**: Com base em seu conhecimento prévio e experiência, o perito identifica padrões relevantes nos dados.

3. **Raciocínio Abdutivo**: Utilizando raciocínio abdutivo, o perito formula hipóteses ou explicações plausíveis que podem justificar os dados observados.

4. **Tomada de Decisão**: Com as hipóteses geradas, o perito pode tomar decisões informadas ou gerar novas ideias que não eram diretamente evidentes na observação inicial.

### Relação com o Raciocínio Não-Monotônico

O raciocínio abdutivo está relacionado ao raciocínio não-monotônico principalmente porque ambos lidam com a incerteza e a revisão de conclusões à medida que novas informações são apresentadas:

- **Raciocínio Abdutivo**: Parte de um conjunto de dados para uma conclusão, que pode ser revisada ou ajustada com base em novas evidências.
  
- **Raciocínio Não-Monotônico**: Também revisa conclusões à medida que novas informações são introduzidas, podendo alterar inferências prévias.

Ambos os tipos de raciocínio são essenciais em sistemas de inteligência artificial e em atividades humanas que envolvem decisões baseadas em informações incompletas ou incertas. Eles permitem uma abordagem flexível e adaptativa para lidar com o mundo complexo e dinâmico ao nosso redor.


#### **Pergunta 2**: No contexto da aplicação do raciocínio baseado em Lógica Difusa nos SBC, explique qual é o propósito das etapas designadas de Composição e de Agregação que se encontram presentes no mecanismo de raciocínio ”Fuzzy“.

- Agregação
    - Calcula a importância de uma determinada regra para a situação corrente 

- Composição
    - Calcula a influência de cada regra nas variáveis de saída. 


#### **Pergunta 3**: A lógica Bayesiana aplicada aos sistemas baseados em regras de produção permite representar a incerteza existente numa relação entre um conjunto de evidências e uma hipótese. Indique em que pressuposto se baseia a aplicação desta técnica, frequentemente designada de modelo ”Naive Bayes“. Indique ainda uma possível abordagem para lidar com situações em que existe incerteza relativamente à observação das evidências relacionadas com uma hipótese, ou seja, quando a probabilidade de uma evidência relacionada com uma hipótese é inferior a 1.

- O presusposto é qu eas evidências são independentes entre si.
- Um alternativa consiste em modificar os pesos LS e LN de forma
a refletir a incerteza inerente à evidência E – pode ser alcançado
através de um interpolação linear dos pesos à medida que a
probabilidade de E varia de 0 a 1


#### **Pergunta 4**:Considere as seguintes regras retiradas de uma base de conhecimento de um sistema baseado na teoria dos Fatores de Certeza: r1 : Se a e b então z pCF “ 0.5q r2 : Se c e d então z pCF “ 0.7q Perante a observação de um conjunto de evidências associadas aos eventos a, b, c e d, o observador decidiu atribuir os factores de certeza -1.0, 0.3, 0.7 e 1.0 a esses eventos, respectivamente.

- A-> "-1" temos a certeza que um acontecimento **definitivamente não** aconteceu

- B-> Apenas a regra 2 dispara, calcular o fator dessa regra e atualizar (sendo que inicialmente era 0.1). Resultado final -> 0.541


#### **Pergunta 5**:  Explique qual é o papel dos Sistemas de Manutenção de Verdade no âmbito de um SBC. Indique de forma sucinta como é utilizado o Sistema de Manutenção de Verdade incorporado no Drools.


- O papel destes sistemas é terem a capacidade de restaurar a consistência do conhecimento, ou seja, podem representar as crenças do sistemas, as suas dependências, guardar inferências, permitir raciocínio baseado em assunções e gerar inconsistências No fundo, validar o conhecimento.

- Exemplo em drools: são permitidos 2 tipos de inserts (stated e lógicos), eis os detalhes: ver página 14 do slide 10 (tms)