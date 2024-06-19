# Respostas aos exames de 22-23

## Exame Recurso

#### **Pergunta 1**: Na construção de Bases de Conhecimento é comum usarem-se linguagens de especificação do conhecimento cuja sintaxe se aproxima da sintaxe da língua natural. Explique porque razão isto sucede. (20%)

- São usadas linguagens de sintaxe natural, pois estas permitem representar o conhecimento num formato de fácil compreensão por parte de um perito/humano, facilidade de comunicação/interpretação entre um sistema pericial e o perito, devido à sua expressividade e clareza sendo capaz de detetar aspetos complexos e relações

#### **Pergunta 2**: Diga o que entende por metaconhecimento e qual a sua utilidade no âmbito dos Sistemas Baseados em Conhecimento. Complemente a sua resposta com um exemplo de aplicação. (20%)

- Meta-conhecimento representa conhecimento acerca do próprio conhecimento.
- Usado para aceder a conhecimento mais orientado para resolver um determinado problema
- Aumenta a eficiência da resoluçao de problemas, levando o racíocinio a um conjunto de regras mais adequado
- É representado através de meta-regras -> regras que descrevem como usar outras regras

Exemplo: 
```
Se o carro não pega
E o sistema eléctrico está operacional
Então usar regras relativas ao circuito de alimentação
```

#### **Pergunta 3**: Considere que a função de pertença da variável fuzzy ”temperatura alta“ tem a forma de rampa ascendente com os pontos de quebra situados em valores de 70 e 100 no eixo horizontal (oC). Ilustre como pode ser alterada a forma desta função de pertença se esta for associada ao intensificador linguístico ”muito“. Justifique a forma desta nova função e a sua relação com o intensificador linguístico ”muito“ (20%)

- portanto, qualquer valor x, tal que 70 < x < 100, x represetnta uma temperature alta. Uma representação mais formal seria esta:

$$
\mu_{\text{alta}}(x) =
\begin{cases}
0 & \text{se } x \leq 70 \\
\frac{x - 70}{100 - 70} & \text{se } 70 < x < 100 \\
1 & \text{se } x \geq 100
\end{cases}
$$

- Para conseguirmos representar o "muito alta", teremos que modificar a situaçãoa anterior, de forma a que temperaturas proximas dos 100, sejam as que são, efetivamente, "muito altas".

$$
\mu_{\text{muito\_alta}}(x) = (\mu_{\text{alta}}(x))^2 =
\begin{cases}
0 & \text{se } x \leq 70 \\
\left( \frac{x - 70}{30} \right)^2 & \text{se } 70 < x < 100 \\
1 & \text{se } x \geq 100
\end{cases}
$$

- De forma mais prática, se entre 70-100 é alto, apenas entre 85-100 será muito alto.





#### **Pergunta 4**: Considere uma regra de produção probabilística que relaciona a observação de uma evidência E1 com uma hipótese H1: IF E1 THEN H1 (LS1; LN1) Indique valores qualitativos para os pesos LS1 (Likelihood of Sufficiency) e LN1 (Likelihood of Necessity) no caso em que a observação da evidência E1 contribui fortemente para a obtenção da hipótese H1 e a ausência da evidência E1 não ter influência sobre a obtenção da hipótese H1. Considere agora uma outra regra de produção que relaciona a evidência E2 com a hipótese H2: IF E2 THEN H2 (LS2 “ 1; LN2 “ 1000) Determine o valor de probabilidade revista de H2 perante a situação em que PpE2q “ 0, 2 e a probabilidade à priori de H2 é 0,7.(20%)

- Valores qualitativos serão:
    - LS = Valor grande
    - LN = 1

- Probabilidade revista de H2 será 70% (está bem?, dunno!)

Como o LS = 1 e a probabilidade revista de H2 = P(H2|E2)

#### **Pergunta 5**: Considere as seguintes regras: R1: IF E1 and E2 and E3 THEN H (CFR1 ) R2: IF E4 or E5 THEN H (CFR2 ) Onde, CFpE1q “ ´0, 2; CFpE2q “ 0, 4; CFpE3q “ 0, 2; CFpE4q “ 0, 6; CFpE5q “ ´0, 2; CFR1 “ 0, 4; CFR2 “ 0, 8 Considerando que CFpHq inicial é 0,2, qual será o CF (factor de certeza) da hipótese H após o disparo da sequência de regras R1, R2? Apresente todos os cálculos efectuados necessários para fundamentar a sua resposta.(20%)

- 1º -> calcular o fator de certeza para cada regras (após ser diaparada)
    - CF (r1) = Min (cf Evidências) * CfR1(antes)   
        - (-0.08)
    - CF (r2) = Max (cf Evidências) * CfR2(antes) 
        - 0.48
- 2º calcular fator de certeza das regras combinadas
    - seguir formula nos slides e verificar a condição em que nos encontramos
    - 
$$
cf(cf1, cf2) =
\begin{cases} 
cf1 + cf2 \times (1 - cf1) & \text{if } cf1 > 0 \text{ and } cf2 > 0 \\
\frac{cf1 + cf2}{1 - \min[|cf1|, |cf2|]} & \text{if } cf1 < 0 \text{ xor } cf2 < 0 \\
cf1 + cf2 \times (1 + cf1) & \text{if } cf1 < 0 \text{ and } cf2 < 0 
\end{cases}
$$
- Como cf1 e cf2 têm sinais contrários, seguimos o caso do meio, em que
    - CF (r1, r2) = (-0.08+0.48)/(1-0.08) = 0.43

- Resposta: Após as regras serem disparadas, o fator de certeza de H é 0.43