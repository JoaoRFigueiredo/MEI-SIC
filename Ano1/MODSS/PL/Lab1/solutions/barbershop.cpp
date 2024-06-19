#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

#define LIMITE 10000

// constantes associadas ao estado dos servidores
#define OCUPADO 1
#define LIVRE 0

// constantes associadas aos tipos de evento considerados
#define EV_CHEGADA 0
#define EV_SAIDA   1
#define EV_FIM     2

void inicializacao(float &clock, int &estado_servidor, int &n_clientes_espera, int &max_clientes_espera,
                   float &tempo_ult_evento, int &n_clientes_atendidos, float &atraso_total,
                   float &num_medio_clientes_fila, float &tempo_utilizacao,
                   float &tempo_max, float *tempo_prox_evento)
{
  clock = 0;

  // inicilalizar variáveis de estado
  estado_servidor = LIVRE;
  n_clientes_espera = 0;
  tempo_ult_evento = 0;

  // inicializar contadores estatisticos
  n_clientes_atendidos = 0;
  atraso_total = 0.0;
  num_medio_clientes_fila = 0.0;
  tempo_utilizacao = 0.0;

  // inicializar lista de eventos
  srand((unsigned)time(NULL)); // inicializar o gerador de números aleatórios
  // escalonar chegada do primeiro cliente
  tempo_prox_evento[EV_CHEGADA] = (float)rand() * 19 / ((float)RAND_MAX + 1);
  // eliminar eventos de saida
  tempo_prox_evento[EV_SAIDA] = -1;
  // escalonar evento fictício associado ao fim da simulação
  tempo_prox_evento[EV_FIM] = tempo_max;
}
void temporizacao(int &tipo_prox_evento, int n_eventos, float &clock, float *tempo_prox_evento)
{
  int i;
  float min_tempo_prox_evento;

  tipo_prox_evento = -1;

  for (i = 0; i < n_eventos; i++)
  {
    if (tipo_prox_evento == -1 && tempo_prox_evento[i] != -1)
    {
      tipo_prox_evento = i;
      min_tempo_prox_evento = tempo_prox_evento[i];
    }
    else if (tipo_prox_evento != -1 && tempo_prox_evento[i] != -1 && tempo_prox_evento[i] < min_tempo_prox_evento)
    {
      min_tempo_prox_evento = tempo_prox_evento[i];
      tipo_prox_evento = i;
    } 
  }
  if (tipo_prox_evento == -1)
  {
    printf("Lista de eventos vazia no instante %.2f", clock);
    exit(1);
  }
  clock = min_tempo_prox_evento; // avança relógio para o instante de ocorrência do prox. evento
}

void evento_chegada(float clock, float *tempo_prox_evento, int &n_clientes_espera,
                    int &estado_servidor, float *tempos_chegada, 
                    float &atraso_total, int &n_clientes_atendidos)
{
  float atraso;

  // escalonar próxima chegada
  tempo_prox_evento[EV_CHEGADA] = clock + (19 * (float)rand() / ((float)RAND_MAX + 1));

  // se o servidor está ocupado o cliente que chega tem que aguardar em fila de espera
  if (estado_servidor == OCUPADO)
  {
    (n_clientes_espera)++;
    if (n_clientes_espera > LIMITE)
    {
      printf("Overflow da fila. Tempo=%f\n", clock);
      exit(1);
    }
    tempos_chegada[(n_clientes_espera)] = clock; // guarda o instante em que o cliente chegou
  }
  // se o servidor está livre o cliente que chega começa a ser atendido no mesmo instante
  else
  {
    // clientes cujo atraso é zero tb devem ser contabilizados...
    atraso = 0.0;
    atraso_total = atraso_total + atraso;
    (n_clientes_atendidos)++;
    estado_servidor = OCUPADO;
    // gera o instante de saida
    tempo_prox_evento[EV_SAIDA] = clock + 1 + (float)rand() / ((float)RAND_MAX + 1) * (22);
    cout << "Tempo de saida: " << tempo_prox_evento[EV_SAIDA] << endl;
  }
}
void evento_saida(float clock, float *tempo_prox_evento, int &n_clientes_espera, int &estado_servidor, float *tempos_chegada, float &atraso_total, int &n_clientes_atendidos)
{
  int i;
  float atraso;
  // se não há clientes em fila de espera
  if (n_clientes_espera == 0)
  {
    // obrigatório eliminar ocorrências de eventos de saida...
    tempo_prox_evento[EV_SAIDA] = -1;
    estado_servidor = LIVRE;
  }
  else
  {
    // retira 1 cliente
    (n_clientes_espera)--;
    atraso = clock - tempos_chegada[1]; // calcular o seu atraso 
    atraso_total += atraso;
    (n_clientes_atendidos)++;
    // gerar o instante de saida
    tempo_prox_evento[EV_SAIDA] = clock + 1 + (float)rand() / ((float)RAND_MAX + 1) * (22);

    // reorganizar fila de espera (necessário por se tartar de um vector... para estruturas de dados, mais adequadas, como uma Queue, não seria necessário...
    for (i = 1; i <= n_clientes_espera; i++)
      tempos_chegada[i] = tempos_chegada[i + 1];
  }
}

void evento_fim_sim(bool &fim, float *tempo_prox_evento, int n_clientes_espera)
{
  // a simulação termina só depois de serem atendidos os clientes que já estão em fila de espera...
  // podem-se testar outras modalidades...
  printf("Numero de clientes a atender = %d\n", n_clientes_espera);
  system("pause");
  fim = true;
  tempo_prox_evento[EV_CHEGADA] = -1; // eliminar eventos de chegada
  tempo_prox_evento[EV_FIM] = -1; // eliminar novo evento (fictício) de fim de simulação
}
void act_estatistica(float &num_medio_clientes_fila, float &tempo_utilizacao,
              int estado_servidor, int &max_clientes_fila, float clock, 
              float &tempo_ult_evento, int n_clientes_espera)
{
  float tempo_desde_ult_evento;
  tempo_desde_ult_evento = clock - tempo_ult_evento;
  tempo_ult_evento = clock;
  num_medio_clientes_fila += n_clientes_espera * tempo_desde_ult_evento;
  tempo_utilizacao += estado_servidor * tempo_desde_ult_evento;
  if(n_clientes_espera > max_clientes_fila)
    max_clientes_fila = n_clientes_espera;
}
void relatorio_final(float clock, int n_clientes_atendidos, int n_clientes_espera,
                     int max_clientes_fila, float atraso_total, float tempo_utilizacao, 
                     float num_medio_clientes_fila)
{
  printf("Tempo = %f\n", clock);
  printf("Numero de clientes atendidos = %d\n", n_clientes_atendidos);
  printf("Ficaram por atender = %d\n", n_clientes_espera);
  printf("Maximo de Clientes na fila de espera = %d\n", max_clientes_fila);
  printf("Tempo medio de atraso em fila de espera = %f\n", atraso_total / n_clientes_atendidos);
  printf("Taxa utilizacao do servidor = %f \n", (tempo_utilizacao / clock * 100));
  printf("Numero medio de clientes em espera = %f\n", num_medio_clientes_fila / clock);
}

int main()
{
  int tipo_prox_evento, n_clientes_espera, max_clientes_fila,
      n_clientes_atendidos, n_eventos, estado_servidor;

  bool fim = false;

  float tempo_utilizacao, num_medio_clientes_fila, clock, tempos_chegada[LIMITE + 1],
      tempo_ult_evento, tempo_prox_evento[3], atraso_total, tempo_max;

  n_eventos = 3;

  cout << "Quanto tempo pretende simular?";

  cin >> tempo_max;

  // chamada da rotina de inicialização
  inicializacao(clock, estado_servidor, n_clientes_espera, max_clientes_fila,
                tempo_ult_evento, n_clientes_atendidos, atraso_total,
                num_medio_clientes_fila, tempo_utilizacao, tempo_max,
                tempo_prox_evento);

  // executar a simulação enquanto necessário
  do
  {
    // determinar o proximo evento
    temporizacao(tipo_prox_evento, n_eventos, clock, tempo_prox_evento);
    // actualização dos acumuladores estatísticos
    act_estatistica(num_medio_clientes_fila, tempo_utilizacao, estado_servidor,
                    max_clientes_fila, clock, tempo_ult_evento, n_clientes_espera);
    // invocar rotina associada ao evento
    switch (tipo_prox_evento)
    {
    case EV_CHEGADA:
      // evento_chegada();
      evento_chegada(clock, tempo_prox_evento, n_clientes_espera,
                     estado_servidor, tempos_chegada, atraso_total, n_clientes_atendidos);
      printf("Chegou cliente. %f.2 Fila de espera %d\n", clock, n_clientes_espera);
      break;
    case EV_SAIDA:
      printf("Partiu cliente.\n");
      evento_saida(clock, tempo_prox_evento, n_clientes_espera, estado_servidor,
                   tempos_chegada, atraso_total, n_clientes_atendidos);
      break;
    case EV_FIM:
      printf("Fim da simulação\n");
      evento_fim_sim(fim, tempo_prox_evento, n_clientes_espera);
      printf("clock: %.2f fim: %s numero Clientes Espera %d\n", clock, (fim) ? "true" : "false", n_clientes_espera);

      break;
    }
  } while ((fim != true) || (n_clientes_espera != 0));
  // invocar o gerador de relatórios
  relatorio_final(clock, n_clientes_atendidos, n_clientes_espera, max_clientes_fila,
                  atraso_total, tempo_utilizacao, num_medio_clientes_fila);
  //system("pause");
  return 0;
}