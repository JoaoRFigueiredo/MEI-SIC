package org.sibac.model;

import org.sibac.haemorrhage.Haemorrhage;

public class Conclusion extends Fact{
    public static final String BEBER_AGUA = "Deve beber água";
    public static final String TOMAR_MEDICAMENTO = "Deve tomar medicamento";
    public static final String REALIZAR_CIRURGIA = "Deve realizar cirurgia";
    public static final String NAO_HA_TRATAMENTO = "Não hã lugar a tratamento";
    public static final String TRATAMENTO_HBP = "Terapia com farmacos|Redução do volume prostatico através de cirurgia|Redução do volume prostatico por vapor de água|Aquabalação";
    public static final String CANCRO_PROSTATA = "Detetado cancro da próstata";
    public static final String PEDRAS_RINS = "Detetadas pedras nos rins";
    public static final String HBP_ANORMAL = "Presença de HBP anormal";
    public static final String HBP_NORMAL = "Presença de HBP normal";

    public static final String CANCRO_VIAS = "Presença de cancro nas vias urinárias";

    public static final String VIGILANCIA_ATIVA = "Paciente será posto em vigilancia";

    public static final String UNKNOWN   = "Não sabemos";

    public static final String PALEATIVO = "Tratamento paleativo";

    public static final String MEDIO = "Prostatectomia|Radioterapia + Deprivação hormonal (4 -6 meses)|Braquiterapia baixa-dosagem|Braquiterapia alta-dosagem + Deprivação hormonal (4 -6 meses) + radioterapia";
    public static final String ALTO = "Prostatectomia|Radioterapia + Deprivação hormonal (2 -3 anos) + Braquiterapia alta-dosagem|Braquiterapia baixa-dosagem|Radioterapia + deprivação hormonal (3 anos)  +Abiraterone /2anos";

    public static final String AVANCADO = "Prostatectomia|Radioterapia + deprivação hormonal (3 anos)  +Abiraterone /2anos|Radioterapia + deprivação hormonal (3 anos)  +Abiraterone /2anos|Braquiterapia baixa-dosagem";
    private String description;

    public Conclusion(String description) {
        this.description = description;
        Haemorrhage.agendaEventListener.addRhs(this);
    }



    public String getDescription() {
        return description;
    }

    public String toString() {
        return ("Conclusion: " + description);
    }

}
