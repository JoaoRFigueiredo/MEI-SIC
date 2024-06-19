import random

LIMITE = 10000

# constants associated with server state
OCUPADO = 1
LIVRE = 0

# constants associated with event types
EV_CHEGADA = 0
EV_SAIDA = 1
EV_FIM = 2

def inicializacao(myData):
    # Schedule arrival of the first client
    myData.tempo_prox_evento[EV_CHEGADA] = random.random() * 19
    myData.tempo_prox_evento[EV_SAIDA] = -1
    myData.tempo_prox_evento[EV_FIM] = myData.tempo_max

def temporizacao(MyData):
    min_tempo_prox_evento = float('nan')
    MyData.tipo_prox_evento = -1
    
    for i in range(MyData.n_eventos):
        if MyData.tipo_prox_evento == -1 and MyData.tempo_prox_evento[i] != -1:
            MyData.tipo_prox_evento = i
            min_tempo_prox_evento = MyData.tempo_prox_evento[i]
        elif MyData.tipo_prox_evento != -1 and MyData.tempo_prox_evento[i] != -1 and MyData.tempo_prox_evento[i] < min_tempo_prox_evento:
            min_tempo_prox_evento = MyData.tempo_prox_evento[i]
            MyData.tipo_prox_evento = i

    if MyData.tipo_prox_evento == -1:
        print("Lista de eventos vazia no instante", MyData.clock)
        sys.exit(1)

    MyData.clock = min_tempo_prox_evento
    return MyData.tipo_prox_evento

def evento_chegada(MyData):
    atraso = 0.0

    print("Tempo de chegada:", MyData.tempo_prox_evento[EV_CHEGADA])

    MyData.tempo_prox_evento[EV_CHEGADA] = MyData.clock + random.random() * 19 + 1

    if MyData.estado_servidor == OCUPADO:
        MyData.n_clientes_espera += 1
        if MyData.n_clientes_espera > LIMITE:
            print("Overflow da fila. Tempo=", MyData.clock)
            sys.exit(1)
        MyData.tempos_chegada.append(MyData.clock)
    else:
        MyData.atraso_total += atraso
        MyData.n_clientes_atendidos += 1
        MyData.estado_servidor = OCUPADO
        MyData.tempo_prox_evento[EV_SAIDA] = MyData.clock + 1 + random.random() * 22
        print("Tempo de saida:", MyData.tempo_prox_evento[EV_SAIDA])

class MySimulationData:
    def __init__(self):
        self.tipo_prox_evento = 0     # next event type
        self.n_clientes_espera = 0    # number of clients waiting
        self.max_clientes_fila = 0    # maximum number of clients in queue
        self.n_clientes_atendidos = 0 # number of clients served
        self.n_eventos = 3            # number of event types EV_CHEGADA, EV_SAIDA, EV_FIM
        self.estado_servidor = LIVRE  # server status
        self.tempo_utilizacao = 0     # server utilization
        self.num_medio_clientes_fila = 0 # average number of clients in queue
        self.clock = 0                # simulation clock
        self.tempos_chegada = []      # Array of client arrival times
        self.tempo_ult_evento = 0     # time of last event
        self.tempo_prox_evento = [0] * self.n_eventos # Array of next events times
        self.atraso_total = 0         # total delay time
        self.tempo_max = 0             # maximum simulation time
        self.fim = False              # end of simulation flag

def evento_saida(MyData):
    atraso = 0.0

    if MyData.n_clientes_espera == 0:
        MyData.tempo_prox_evento[EV_SAIDA] = -1
        MyData.estado_servidor = LIVRE
    else:
        MyData.n_clientes_espera -= 1
        atraso = MyData.clock - MyData.tempos_chegada.pop(0)
        MyData.atraso_total += atraso
        MyData.n_clientes_atendidos += 1
        MyData.tempo_prox_evento[EV_SAIDA] = MyData.clock + 1 + random.random() * 22

def evento_fim_sim(MyData):
    print("Numero de clientes a atender =", MyData.n_clientes_espera)
    MyData.fim = True
    MyData.tempo_prox_evento[EV_CHEGADA] = -1  # eliminar evento de chegada
    MyData.tempo_prox_evento[EV_FIM] = -1      # eliminar evento de fim
    # Implement any necessary logic here for the end of simulation

def act_estatistica(MyData):
    tempo_desde_ult_evento = MyData.clock - MyData.tempo_ult_evento
    MyData.tempo_ult_evento = MyData.clock
    MyData.num_medio_clientes_fila += MyData.n_clientes_espera * tempo_desde_ult_evento
    MyData.tempo_utilizacao += MyData.estado_servidor * tempo_desde_ult_evento
    if MyData.n_clientes_espera > MyData.max_clientes_fila:
        MyData.max_clientes_fila = MyData.n_clientes_espera

def relatorio_final(MyData):
    print("Tempo =", MyData.clock)
    print("Numero de clientes atendidos =", MyData.n_clientes_atendidos)
    print("Ficaram por atender =", MyData.n_clientes_espera)
    print("Maximo de Clientes na fila de espera =", MyData.max_clientes_fila)
    print("Tempo medio de atraso em fila de espera =", MyData.atraso_total / MyData.n_clientes_atendidos)
    print("Taxa utilizacao do servidor =", (MyData.tempo_utilizacao / MyData.clock * 100))
    print("Numero medio de clientes em espera =", MyData.num_medio_clientes_fila / MyData.clock)

# Example usage:
if __name__ == "__main__":
    # Ask for simulation duration
    tempo_max = int(input('Quanto tempo pretende simular? '))
    MyData = MySimulationData()
    MyData.tempo_max = tempo_max
    print(f"You entered: {MyData.tempo_max}")

    MyData.n_eventos = 3

    # Call initialization routine
    inicializacao(MyData)

    # Execute simulation as necessary
    while not MyData.fim or MyData.n_clientes_espera != 0:
        # Determine the next event
        MyData.tipo_prox_evento = temporizacao(MyData)
        # Update statistical accumulators
        act_estatistica(MyData)
        # Invoke routine associated with the event
        if MyData.tipo_prox_evento == EV_CHEGADA:
            print(f"Chegou cliente. {MyData.clock:.2f}")
            evento_chegada(MyData)
        elif MyData.tipo_prox_evento == EV_SAIDA:
            print("Partiu cliente.")
            evento_saida(MyData)
        elif MyData.tipo_prox_evento == EV_FIM:
            print("Fim da simulação")
            evento_fim_sim(MyData)

    # Invoke the report generator
    relatorio_final(MyData)