import simpy
import random
from faker import Faker
import os
from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px



TEMPO_REGISTO = (3, 7)
TEMPO_CONSULTA = (5, 15)
TEMPO_EXAMES = (10, 20)
TEMPO_TRATAMENTO = (15, 25)
TEMPO_CIRURGIA = (20, 40)
TEMPO_OBSERVACAO = (50, 70)
TEMPO_PLANO_DE_ALTA = (5, 15)
TEMPO_LIMPEZA_SALA = (10, 20)
TEMPO_ICU = (1440, 2880)  
TEMPO_DESPEDIDA = (5, 10)

PRIORITY_NON_URGENT = 5
PRIORITY_MODERATE = 4
PRIORITY_REDUCED_MOBILITY = 3
PRIORITY_VULNERABLE = 2
PRIORITY_CRITICAL = 1


new_labels = {1: 'PRIORITY_CRITICAL', 2: 'PRIORITY_VULNERABLE', 3: 'PRIORITY_REDUCED_MOBILITY', 4 : 'PRIORITY_MODERATE', 5:'PRIORITY_NON_URGENT' }

fake = Faker()

file_name = "simulator_output.txt"
file1 = None

st.title("Hospital Simulation")

num_receptionists = st.sidebar.number_input("Number of Receptionists", min_value=1, max_value=10, value=4)
num_consultation_rooms = st.sidebar.number_input("Number of Consultation Rooms", min_value=1, max_value=10, value=5)
num_exam_rooms = st.sidebar.number_input("Number of Exam Rooms", min_value=1, max_value=10, value=5)
num_doctors = st.sidebar.number_input("Number of Doctors", min_value=1, max_value=10, value=7)
num_surgeons = st.sidebar.number_input("Number of Surgeons", min_value=1, max_value=10, value=4)
num_nurses = st.sidebar.number_input("Number of Nurses", min_value=1, max_value=20, value=10)
num_surgery_rooms = st.sidebar.number_input("Number of Surgery Rooms", min_value=1, max_value=10, value=3)
num_icu_rooms = st.sidebar.number_input("Number of ICU Rooms", min_value=1, max_value=10, value=4)
num_cleaning_teams = st.sidebar.number_input("Number of Cleaning Teams", min_value=1, max_value=10, value=4)

simulation_duration = st.sidebar.number_input("Simulation Duration (in days)", min_value=1, max_value=14, value=7)


simulation_duration = 24*60 * simulation_duration

max_patients_waiting = 0

average_waiting_times = {'waiting_registration' : (0, 0), 'waiting_consultation' : (0, 0)}

action_counts = {'chegada': 0, 'registo': 0, 'espera_registo': 0, 'espera_consulta':0, 'consulta':0, 
                 'exames': 0, 'tratamentos':0, 'observação': 0, 'plano_alta': 0, 
                 'saida': 0, 'cirurgia_emergencia': 0, 'observação_icu': 0, 'cirurgia_normal': 0, 'limpeza_sala' : 0}

patients_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

critical_patients_status = {'alive': 0, 'death': 0}

if st.sidebar.button("Run Simulation"):
    if not os.path.exists(file_name):
        with open(file_name, 'x', encoding='utf-8') as file1:
           st.write(f"File '{file_name}' created successfully.")
    else:
        file1 = open(file_name, 'w', encoding='utf-8')
        st.write(f"File '{file_name}' already exists.")

    class Hospital:
        def __init__(self, env):
            self.env = env
            self.recepcao = simpy.PriorityResource(env, capacity=num_receptionists)
            self.sala_consulta = simpy.PriorityResource(env, capacity=num_consultation_rooms)
            self.sala_exames = simpy.PriorityResource(env, capacity=num_exam_rooms)
            self.doctors = simpy.PriorityResource(env, capacity=num_doctors)
            self.surgeons = simpy.PriorityResource(env, capacity=num_surgeons)
            self.nurses = simpy.PriorityResource(env, capacity=num_nurses)
            self.sala_cirurgia = simpy.PriorityResource(env, capacity=num_surgery_rooms)
            self.uti = simpy.PriorityResource(env, capacity=num_icu_rooms)
            self.sala_limpeza = simpy.PriorityResource(env, capacity=num_cleaning_teams)

        

        def registrar(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_REGISTO))
            action_counts['registo'] +=1
           # st.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez o registro no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez o registo no instante {self.env.now}\n")

        def consulta(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_CONSULTA))
            action_counts['consulta'] +=1
            #st.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez a consulta no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez a consulta no instante {self.env.now}\n")

        def exames(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_EXAMES))
            action_counts['exames'] +=1
           # st.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez os exames no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez os exames no instante {self.env.now}\n")

        def tratamento(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_TRATAMENTO))
            action_counts['tratamentos'] +=1
           # st.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez o tratamento no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez o tratamento no instante {self.env.now}\n")

        def cirurgia(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_CIRURGIA))
            if paciente['Prioridade'] == 1:
                action_counts['cirurgia_emergencia'] += 1
            else:
                action_counts['cirurgia_normal'] += 1
           # st.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez a cirurgia no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) fez a cirurgia no instante {self.env.now}\n")

        def observacao(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_OBSERVACAO))
            action_counts['observação'] +=1
           # st.write(f"Paciente {paciente['id']} ({paciente['nome']}) foi para observação no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) foi para observação no instante {self.env.now}\n")

        def plano_alta(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_PLANO_DE_ALTA))
            action_counts['plano_alta'] += 1
           # st.write(f"Paciente {paciente['id']} ({paciente['nome']}) teve o plano de alta no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) teve o plano de alta no instante {self.env.now}\n")

        def limpeza_sala(self):
            yield self.env.timeout(random.uniform(*TEMPO_LIMPEZA_SALA))
            action_counts['limpeza_sala'] += 1
           # st.write(f"Sala de cirurgia limpa no instante {self.env.now}")
            file1.write(f"Sala de cirurgia limpa no instante {self.env.now}\n")

        def icu(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_ICU))
            action_counts['observação_icu'] += 1
            #st.write(f"Paciente {paciente['id']} ({paciente['nome']}) está na UCI no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) está na UCI no instante {self.env.now}\n")

        def despedida(self, paciente):
            yield self.env.timeout(random.uniform(*TEMPO_DESPEDIDA))
            action_counts['saida'] += 1
            #print(f"Paciente {paciente['id']} ({paciente['nome']}) deixou o hospital no instante {self.env.now}")
            file1.write(f"Paciente {paciente['id']} ({paciente['nome']}) deixou o hospital no instante {self.env.now}\n")

    def criar_paciente():
        d_nascimento = fake.date_of_birth().strftime("%Y-%m-%d")
        dob = datetime.strptime(d_nascimento, "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
        priority_levels = [1, 2, 3, 4, 5]
        weights = [1, 2, 3, 4, 5]  

        prioridade = random.choices(priority_levels, weights, k=1)[0]
        
        return {
            'id': fake.uuid4(),
            'nome': fake.name(),
            'endereco': fake.address(),
            'sexo': fake.random_element(elements=('M', 'F')),
            'data_nascimento': d_nascimento,
            'idade': age,
            'Prioridade': prioridade
        }

    def critical_patient(env, dados_paciente, hospital):
        #st.write(f"Critical patient {dados_paciente['nome']} chegou ao hospital no instante {env.now}")
        file1.write(f"Critical patient {dados_paciente['nome']} chegou ao hospital no instante {env.now}\n")
        action_counts['chegada'] +=1

        with hospital.surgeons.request(priority=PRIORITY_CRITICAL) as request_surgeon, \
             hospital.nurses.request(priority=PRIORITY_CRITICAL) as request_nurse_1, \
             hospital.nurses.request(priority=PRIORITY_CRITICAL) as request_nurse_2, \
             hospital.sala_cirurgia.request(priority=PRIORITY_CRITICAL) as request_surgery_room:

            yield request_surgeon
            yield request_nurse_1
            yield request_nurse_2
            yield request_surgery_room

            yield env.process(hospital.cirurgia(dados_paciente))
            
            if random.random() < 0.05:
              #  st.write(f"Paciente crítico {dados_paciente['id']} ({dados_paciente['nome']}) morreu durante a cirurgia no instante {env.now}")
                file1.write(f"Paciente crítico {dados_paciente['id']} ({dados_paciente['nome']}) morreu durante a cirurgia no instante {env.now}\n")
                critical_patients_status['death'] += 1
                return

            critical_patients_status['alive'] += 1
    
            yield env.process(hospital.limpeza_sala())

        with hospital.sala_consulta.request(priority=dados_paciente['Prioridade']) as request_consulta, \
             hospital.doctors.request(priority=dados_paciente['Prioridade']) as request_doctor:
            
            start_wait_consulta = env.now
            
            yield request_consulta & request_doctor

            if env.now > start_wait_consulta:
                wait_time_consulta = env.now - start_wait_consulta
               # st.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) esperou {wait_time_consulta:.2f} minutos para consulta com prioridade {dados_paciente['Prioridade']}.")
                file1.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) esperou {wait_time_consulta:.2f} minutos para consulta com prioridade {dados_paciente['Prioridade']}.\n")
            else:
              #  st.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) não precisou esperar para consulta com prioridade {dados_paciente['Prioridade']}.")
                file1.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) não precisou esperar para consulta com prioridade {dados_paciente['Prioridade']}.\n")

            yield env.process(hospital.consulta(dados_paciente))

            if random.random() < 0.3:
                with hospital.sala_exames.request(priority=dados_paciente['Prioridade']) as request_exames:
                    yield request_exames
                    yield env.process(hospital.exames(dados_paciente))

            if random.random() < 0.2:
                yield env.process(hospital.tratamento(dados_paciente))

            if random.random() < 0.1:
                with hospital.sala_cirurgia.request(priority=dados_paciente['Prioridade']) as request_cirurgia:
                    yield request_cirurgia
                    yield env.process(hospital.cirurgia(dados_paciente))
                    yield env.process(hospital.limpeza_sala())
                    if random.random() < 0.2:
                        yield env.process(hospital.observacao(dados_paciente))
                    else:
                        yield env.process(hospital.plano_alta(dados_paciente))
            else:
                yield env.process(hospital.plano_alta(dados_paciente))
                yield env.process(hospital.despedida(dados_paciente)) 


    def paciente(env, dados_paciente, hospital):
       # st.write(f"{dados_paciente['nome']} chegou ao hospital no instante {env.now}")
        file1.write(f"{dados_paciente['nome']} chegou ao hospital no instante {env.now}\n")
        action_counts['chegada'] += 1

        if dados_paciente['Prioridade'] == PRIORITY_CRITICAL:
            yield env.process(critical_patient(env, dados_paciente, hospital))
            return

        with hospital.recepcao.request(priority=dados_paciente['Prioridade']) as request_recepcao:
            start_wait_recepcao = env.now
            yield request_recepcao
            wait_time_recepcao = env.now - start_wait_recepcao

            if wait_time_recepcao > 0:
                action_counts['espera_registo'] += 1
                tempo_espera = average_waiting_times['waiting_registration'][0]
                num_esperas = average_waiting_times['waiting_registration'][1]
                average_waiting_times['waiting_registration'] = (tempo_espera + wait_time_recepcao, num_esperas+1)
                #st.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) esperou {wait_time_recepcao:.2f} minutos na recepção com prioridade {dados_paciente['Prioridade']}.")
                file1.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) esperou {wait_time_recepcao:.2f} minutos na receção com prioridade {dados_paciente['Prioridade']}.\n")
            else:
               # st.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) não precisou esperar na recepção com prioridade {dados_paciente['Prioridade']}.")
                file1.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) não precisou esperar na receção com prioridade {dados_paciente['Prioridade']}.\n")

            yield env.process(hospital.registrar(dados_paciente))

        with hospital.sala_consulta.request(priority=dados_paciente['Prioridade']) as request_consulta, \
             hospital.doctors.request(priority=dados_paciente['Prioridade']) as request_doctor:
            
            start_wait_consulta = env.now
            
           
            yield request_consulta & request_doctor

            
            if env.now > start_wait_consulta:
                wait_time_consulta = env.now - start_wait_consulta
                action_counts['espera_consulta'] += 1
                tempo_espera = average_waiting_times['waiting_consultation'][0]
                num_esperas = average_waiting_times['waiting_consultation'][1]
                average_waiting_times['waiting_consultation'] = (tempo_espera + wait_time_consulta, num_esperas+1)
               # st.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) esperou {wait_time_consulta:.2f} minutos para consulta com prioridade {dados_paciente['Prioridade']}.")
                file1.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) esperou {wait_time_consulta:.2f} minutos para consulta com prioridade {dados_paciente['Prioridade']}.\n")
            else:
               # st.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) não precisou esperar para consulta com prioridade {dados_paciente['Prioridade']}.")
                file1.write(f"Paciente {dados_paciente['id']} ({dados_paciente['nome']}) não precisou esperar para consulta com prioridade {dados_paciente['Prioridade']}.\n")

           
            yield env.process(hospital.consulta(dados_paciente))

            
            if random.random() < 0.3:
                
                with hospital.sala_exames.request(priority=dados_paciente['Prioridade']) as request_exames:
                    yield request_exames
                    yield env.process(hospital.exames(dados_paciente))

            if random.random() < 0.2:
               
                yield env.process(hospital.tratamento(dados_paciente))

            if random.random() < 0.1:
                
                with hospital.sala_cirurgia.request(priority=dados_paciente['Prioridade']) as request_cirurgia:
                    yield request_cirurgia
                    yield env.process(hospital.cirurgia(dados_paciente))
                    yield env.process(hospital.limpeza_sala())
                    if random.random() < 0.2:
                        yield env.process(hospital.observacao(dados_paciente))
                    else:
                        yield env.process(hospital.plano_alta(dados_paciente))
            else:
                
                yield env.process(hospital.plano_alta(dados_paciente))
                yield env.process(hospital.despedida(dados_paciente))  


    def gerar_pacientes(env, hospital):
        while True:
           
            yield env.timeout(random.expovariate(1/10))
            
            num_pacientes = random.randint(1, 3)  
            
            for _ in range(num_pacientes):
                dados_paciente = criar_paciente()
                #print(dados_paciente)
                patients_count[dados_paciente['Prioridade']] +=1
                env.process(paciente(env, dados_paciente, hospital))

    env = simpy.Environment()
    hospital = Hospital(env)
    env.process(gerar_pacientes(env, hospital))
    env.run(until=simulation_duration)
    file1.close()
    st.write("Simulation completed.")
    st.download_button("Download Output File", data=open(file_name, "r").read(), file_name=file_name, mime="text/plain")


    print(average_waiting_times)

    print(action_counts)

    print(patients_count)

    patients_count = {new_labels[key]: value for key, value in patients_count.items()}


avg_wait_df = pd.DataFrame(list(average_waiting_times.values()), columns=['Average Time', 'Count'], index=list(average_waiting_times.keys()))
avg_wait_df['average_wait'] = avg_wait_df['Average Time']/avg_wait_df['Count']
action_counts_df = pd.DataFrame(list(action_counts.items()), columns=['Action', 'Count'])
patients_count_df = pd.DataFrame(list(patients_count.items()), columns=['Priority Level', 'Count'])

st.title('Hospital Dashboard')

st.subheader('Average Waiting Times')
st.dataframe(avg_wait_df)

st.subheader('Average waiting Times')
st.bar_chart(avg_wait_df['average_wait'])

st.subheader('Action Counts')
st.dataframe(action_counts_df)

st.subheader('Patients Count by Priority Level')
st.bar_chart(patients_count_df.set_index('Priority Level'))


st.subheader('Action Counts Visualization')
fig_action_counts = px.line(action_counts_df, x='Action', y='Count', title='Action Counts')
st.plotly_chart(fig_action_counts)

status_labels = list(critical_patients_status.keys())
status_counts = list(critical_patients_status.values())

fig = px.pie(values=status_counts, names=status_labels, title='Critical Patients Status')

st.title('Critical Patients Status Visualization')
st.plotly_chart(fig)



