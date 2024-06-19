import * as readline from 'readline';

const LIMITE: number = 10000;

// constants associated with server state
const OCUPADO: number = 1;
const LIVRE: number = 0;

// constants associated with event types
const EV_CHEGADA: number = 0;
const EV_SAIDA: number = 1;
const EV_FIM: number = 2;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});




function inicializacao(myData: MySimulationData): void {

    // Schedule arrival of the first client
    myData.tempo_prox_evento[EV_CHEGADA] = Math.random() * 19;
    myData.tempo_prox_evento[EV_SAIDA] = -1;
    myData.tempo_prox_evento[EV_FIM] = myData.tempo_max;

}

function temporizacao(MyData:MySimulationData): number {
    let min_tempo_prox_evento: number = NaN;

    MyData.tipo_prox_evento= -1;
    
    for (let i = 0; i < MyData.n_eventos; i++) {
        if (MyData.tipo_prox_evento === -1 && MyData.tempo_prox_evento[i] !== -1) {
            MyData.tipo_prox_evento = i;
            min_tempo_prox_evento = MyData.tempo_prox_evento[i];
        } else if (MyData.tipo_prox_evento !== -1 && MyData.tempo_prox_evento[i] !== -1 && MyData.tempo_prox_evento[i] < min_tempo_prox_evento) {
            min_tempo_prox_evento = MyData.tempo_prox_evento[i];
            MyData.tipo_prox_evento = i;
        }
    }

    if (MyData.tipo_prox_evento === -1) {
        console.log("Lista de eventos vazia no instante " + MyData.clock);
        process.exit(1);
    }

    MyData.clock = min_tempo_prox_evento;
    return MyData.tipo_prox_evento;
}

function evento_chegada(MyData:MySimulationData): void {
    let atraso: number;

    console.log("Tempo de chegada: " + MyData.tempo_prox_evento[EV_CHEGADA]);

    MyData.tempo_prox_evento[EV_CHEGADA] = MyData.clock + Math.random() * 19 + 1;

    if (MyData.estado_servidor === OCUPADO) {
        MyData.n_clientes_espera++;
        if (MyData.n_clientes_espera > LIMITE) {
            console.log("Overflow da fila. Tempo=" + MyData.clock);
            process.exit(1);
        }
        MyData.tempos_chegada.push(MyData.clock);
    } else {
        atraso = 0.0;
        MyData.atraso_total += atraso;
        MyData.n_clientes_atendidos++;
        MyData.estado_servidor = OCUPADO;
        MyData.tempo_prox_evento[EV_SAIDA] = MyData.clock + 1 + Math.random() * 22;
        console.log("Tempo de saida: " + MyData.tempo_prox_evento[EV_SAIDA]);
    }
}

function evento_saida(MyData:MySimulationData): void {
    let atraso: number;

    if (MyData.n_clientes_espera === 0) {
        MyData.tempo_prox_evento[EV_SAIDA] = -1;
        MyData.estado_servidor = LIVRE;
    } else {
        MyData.n_clientes_espera--;
        atraso = MyData.clock - MyData.tempos_chegada.shift()!;
        MyData.atraso_total += atraso;
        MyData.n_clientes_atendidos++;
        MyData.tempo_prox_evento[EV_SAIDA] = MyData.clock + 1 + Math.random() * 22;
    }
}

function evento_fim_sim(MyData: MySimulationData): void {
    console.log("Numero de clientes a atender = " + MyData.n_clientes_espera);
    MyData.fim = true;
    MyData.tempo_prox_evento[EV_CHEGADA] = -1; // eliminar evento de chegada
    MyData.tempo_prox_evento[EV_FIM] = -1;     // eliminar evento de fim
    // Implement any necessary logic here for the end of simulation
}

function act_estatistica(MyData:MySimulationData): void {
    let tempo_desde_ult_evento: number = MyData.clock - MyData.tempo_ult_evento;
    MyData.tempo_ult_evento = MyData.clock;
    MyData.num_medio_clientes_fila += MyData.n_clientes_espera * tempo_desde_ult_evento;
    MyData.tempo_utilizacao += MyData.estado_servidor * tempo_desde_ult_evento;
    if(MyData.n_clientes_espera > MyData.max_clientes_fila) {
        MyData.max_clientes_fila = MyData.n_clientes_espera;
    }
}

function relatorio_final(MyData: MySimulationData): void {
    console.log("Tempo = " + MyData.clock);
    console.log("Numero de clientes atendidos = " + MyData.n_clientes_atendidos);
    console.log("Ficaram por atender = " + MyData.n_clientes_espera);
    console.log("Maximo de Clientes na fila de espera = " + MyData.max_clientes_fila);
    console.log("Tempo medio de atraso em fila de espera = " + MyData.atraso_total / MyData.n_clientes_atendidos);
    console.log("Taxa utilizacao do servidor = " + (MyData.tempo_utilizacao / MyData.clock * 100));
    console.log("Numero medio de clientes em espera = " + MyData.num_medio_clientes_fila / MyData.clock);
}

class MySimulationData {
    tipo_prox_evento: number;
    n_clientes_espera: number;
    max_clientes_fila: number;
    n_clientes_atendidos: number;
    n_eventos: number;
    estado_servidor: number;
    tempo_utilizacao: number;
    num_medio_clientes_fila: number;
    clock: number;
    tempos_chegada: number[];
    tempo_ult_evento: number;
    tempo_prox_evento: number[];
    atraso_total: number;
    tempo_max: number;
    fim: boolean;

    constructor() {
        this.tipo_prox_evento=0;     // next event type
        this.n_clientes_espera=0;    // number of clients waiting
        this.max_clientes_fila=0;    // maximum number of clients in queue
        this.n_clientes_atendidos=0; // number of clients served
        this.n_eventos=3;            // number of event types EV_CHEGADA, EV_SAIDA, EV_FIM
        this.estado_servidor=LIVRE;  // server status
        this.tempo_utilizacao=0;     // server utilization
        this.num_medio_clientes_fila=0; // average number of clients in queue
        this.clock=0;                // simulation clock
        this.tempos_chegada=new Array(); // Array of client arrival times
        this.tempo_ult_evento=0;     // time of last event
        this.tempo_prox_evento=new Array(this.n_eventos); // Array of next events times
        this.atraso_total=0;         // total delay time
        this.tempo_max=0;           // maximum simulation time
        this.fim=false;             // end of simulation flag

        // Initialize tempo_prox_evento array
        for (let i:number = 0; i < this.n_eventos; i++) {
          this.tempo_prox_evento[i] = 0;
        }
    }
}


rl.question('Quanto tempo pretende simular? ', (answer) => {
    const MyData: MySimulationData=new MySimulationData();
    
    MyData.tempo_max = parseInt(answer);
    console.log(`You entered: ${MyData.tempo_max}`);
        
    MyData.n_eventos = 3;

    // call initialization routine
    inicializacao(MyData);

    // execute simulation as necessary
    do {
        // determine the next event
        MyData.tipo_prox_evento = temporizacao(MyData);
        // update statistical accumulators
        act_estatistica(MyData);
        // invoke routine associated with the event
        switch (MyData.tipo_prox_evento) {
            case EV_CHEGADA:
                console.log("Chegou cliente. " + MyData.clock.toFixed(2));
                evento_chegada(MyData);
                break;
            case EV_SAIDA:
                console.log("Partiu cliente.");
                evento_saida(MyData);
                break;
            case EV_FIM:
                console.log("Fim da simulação");
                evento_fim_sim(MyData);
                break;
        }
    } while ((MyData.fim != true) || (MyData.n_clientes_espera != 0));
    // invoke the report generator
    relatorio_final(MyData);
    // System pause removed as there is no direct equivalent in JavaScript/TypeScript
});