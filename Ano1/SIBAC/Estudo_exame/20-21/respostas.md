# Exames 20-21

## Exame normal

#### **pergunta 1:**A tarefa de diagnóstico de avarias, que é função do Sistema Baseado em Conhecimento, é realizada com base na identificação de sequências estereotipadas de mensagens geradas no sistema de transporte de energia eléctrica e na verificação de restrições temporais entre mensagens presentes nas sequências. Considerando os diferentes tipos de conhecimento estudados, caracterize o conhecimento que será utilizado pelo sistema a desenvolver e identifique, justificando, o formalismo de representação de conhecimento mais adequado para a construção da base de conhecimento.

- Usar conhecimento procedimental, pois permite definir sequências e serve para lidar com situações distintas. Ver resposta do exame normal 21-22

#### **Pergunta 2:** Considere que pretendemos implementar o SBC descrito em Drools e que as mensagens descritivas de eventos são representadas na memória de trabalho através de factos com a designação ScadaMessage. Estes factos possuem os atributos type, plant, panel, plant2 e nl. Todos estes atributos são do tipo string. Apresente o código necessário para declarar este tipo de facto em Drools.

- Criar a classe em java, associar ao drools atravé sde um declare ScadaMessage
- Nas regras utilizar $Message para utilizar as strings ($message : ScadaMessage(type == "Alerta", plant == "Planta A"))
- i dunno

#### **Pergunta 3**: Considere que o motor de inferência do Drools foi adaptado para usar um mecanismo de resolução de conflitos por especificidade. Neste cenário, indique como é que o motor de inferência deve atuar. Justifique a sua resposta

- Neste caso, o drools vai disparar a primeira regra, pois é a que possui mais detalhe (maior nível de especifidade/mais condições). Regras 1  e 2 possuem uma condição em semelhante, no entanto a 1 é mais completa.

#### **Pergunta 4**: Considere ainda que a regra d1 dispara e que na memória de trabalho existe um facto que permite validar a segunda condição da regra d3 (ScadaMessagepq), com os mesmos valores para os atributos plant, panel, plant2 e nl que permitiram o disparo da regra d1. Nas circunstâncias descritas, indique se a regra d3 dispara. Justifique a sua resposta.


- Sim, a regra dispara, pois todas as suas condições estrão satisfeitas. Como a regra d1 já disparou e criou a conclusão que d3 verifica, não haverão problemas.


#### **Pergunta 5**:Indique quais são os factos do tipo Conclusionpq presentes na memória de trabalho logo após o instante T1 e logo após o instante T2

- Logo após o T1 temos esta concluão:

Conclusion c = new Conclusion ( $plant1 , $panel1 , $plant2 , $nl ,
ConclusionType . DISP_TRIF_DISJ_MOV );

- logo após T2 temos:

Conclusion(plant="PlantA", panel="PanelA", plant2="PlantB", nl="1", conclusion=DISP_TRIF_DISJ_MOV) e Conclusion(plant="PlantA", panel="PanelA", plant2="PlantB", nl="1", conclusion=RELIG_TRIF)
