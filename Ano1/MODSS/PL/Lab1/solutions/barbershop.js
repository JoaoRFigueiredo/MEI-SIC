let readline = require("readline");
const LIMITE = 10000;
// constants associated with server state
const OCUPADO = 1;
const LIVRE = 0;
// constants associated with event types
const EV_CHEGADA = 0;
const EV_SAIDA = 1;
const EV_FIM = 2;
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
function inicializacao(myData) {
    myData.clock = 0;
    myData.estado_servidor = LIVRE;
    myData.n_clientes_espera = 0;
    myData.tempo_ult_evento = 0;
    myData.n_clientes_atendidos = 0;
    myData.atraso_total = 0.0;
    myData.num_medio_clientes_fila = 0.0;
    myData.tempo_utilizacao = 0.0;
    myData.n_eventos = 3;
    // Initialize tempo_prox_evento array
    myData.tempo_prox_evento = new Array(myData.n_eventos);
    for (var i = 0; i < myData.n_eventos; i++) {
        myData.tempo_prox_evento[i] = 0;
        console.log("Tempo prox evento " + i + " = " + myData.tempo_prox_evento[i]);
    }
    // Schedule arrival of the first client
    myData.tempo_prox_evento[EV_CHEGADA] = Math.random() * 19;
    myData.tempo_prox_evento[EV_SAIDA] = -1;
    myData.tempo_prox_evento[EV_FIM] = myData.tempo_max;
    for (var i = 0; i < myData.n_eventos; i++) {
        console.log("Tempo prox evento " + i + " = " + myData.tempo_prox_evento[i]);
    }
}
function temporizacao(MyData) {
    var min_tempo_prox_evento = NaN;
    MyData.tipo_prox_evento = -1;
    for (var i = 0; i < MyData.n_eventos; i++) {
        if (MyData.tipo_prox_evento === -1 && MyData.tempo_prox_evento[i] !== -1) {
            MyData.tipo_prox_evento = i;
            min_tempo_prox_evento = MyData.tempo_prox_evento[i];
        }
        else if (MyData.tipo_prox_evento !== -1 && MyData.tempo_prox_evento[i] !== -1 && MyData.tempo_prox_evento[i] < min_tempo_prox_evento) {
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
function evento_chegada(MyData) {
    var atraso;
    console.log("Tempo de chegada: " + MyData.tempo_prox_evento[EV_CHEGADA]);
    MyData.tempo_prox_evento[EV_CHEGADA] = MyData.clock + Math.random() * 19 + 1;
    if (MyData.estado_servidor === OCUPADO) {
        MyData.n_clientes_espera++;
        if (MyData.n_clientes_espera > LIMITE) {
            console.log("Overflow da fila. Tempo=" + MyData.clock);
            process.exit(1);
        }
        MyData.tempos_chegada.push(MyData.clock);
    }
    else {
        atraso = 0.0;
        MyData.atraso_total += atraso;
        MyData.n_clientes_atendidos++;
        MyData.estado_servidor = OCUPADO;
        MyData.tempo_prox_evento[EV_SAIDA] = MyData.clock + 1 + Math.random() * 22;
        console.log("Tempo de saida: " + MyData.tempo_prox_evento[EV_SAIDA]);
    }
}
function evento_saida(MyData) {
    var atraso;
    if (MyData.n_clientes_espera === 0) {
        MyData.tempo_prox_evento[EV_SAIDA] = -1;
        MyData.estado_servidor = LIVRE;
    }
    else {
        MyData.n_clientes_espera--;
        atraso = MyData.clock - MyData.tempos_chegada.shift();
        MyData.atraso_total += atraso;
        MyData.n_clientes_atendidos++;
        MyData.tempo_prox_evento[EV_SAIDA] = MyData.clock + 1 + Math.random() * 22;
    }
}
function evento_fim_sim(MyData) {
    console.log("Numero de clientes a atender = " + MyData.n_clientes_espera);
    MyData.fim = true;
    MyData.tempo_prox_evento[EV_CHEGADA] = -1; // eliminar evento de chegada
    MyData.tempo_prox_evento[EV_FIM] = -1; // eliminar evento de fim
    // Implement any necessary logic here for the end of simulation
}
function act_estatistica(MyData) {
    var tempo_desde_ult_evento = MyData.clock - MyData.tempo_ult_evento;
    MyData.tempo_ult_evento = MyData.clock;
    MyData.num_medio_clientes_fila += MyData.n_clientes_espera * tempo_desde_ult_evento;
    MyData.tempo_utilizacao += MyData.estado_servidor * tempo_desde_ult_evento;
}
function relatorio_final(MyData) {
    console.log("Tempo = " + MyData.clock);
    console.log("Numero de clientes atendidos = " + MyData.n_clientes_atendidos);
    console.log("Ficaram por atender = " + MyData.n_clientes_espera);
    console.log("Tempo medio de atraso em fila de espera = " + MyData.atraso_total / MyData.n_clientes_atendidos);
    console.log("Taxa utilizacao do servidor = " + (MyData.tempo_utilizacao / MyData.clock * 100));
    console.log("Numero medio de clientes em espera = " + MyData.num_medio_clientes_fila / MyData.clock);
}
var MySimulationData = /** @class */ (function () {
    function MySimulationData() {
        this.tipo_prox_evento = 0;
        this.n_clientes_espera = 0;
        this.n_clientes_atendidos = 0;
        this.n_eventos = 0;
        this.estado_servidor = 0;
        this.tempo_utilizacao = 0;
        this.num_medio_clientes_fila = 0;
        this.clock = 0;
        this.tempos_chegada = new Array();
        this.tempo_ult_evento = 0;
        this.tempo_prox_evento = new Array(3);
        this.atraso_total = 0;
        this.tempo_max = 0;
        this.fim = false;
    }
    return MySimulationData;
}());
rl.question('Quanto tempo pretende simular? ', function (answer) {
    var MyData = new MySimulationData();
    MyData.tempo_max = parseInt(answer);
    console.log("You entered: ".concat(MyData.tempo_max));
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
