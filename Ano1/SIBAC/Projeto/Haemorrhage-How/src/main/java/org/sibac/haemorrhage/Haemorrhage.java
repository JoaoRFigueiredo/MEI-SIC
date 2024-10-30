package org.sibac.haemorrhage;

import java.io.BufferedReader;
import java.util.Map;
import java.util.TreeMap;

import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;
import org.kie.api.runtime.rule.LiveQuery;
import org.kie.api.runtime.rule.Row;
import org.kie.api.runtime.rule.ViewChangedEventListener;

import org.sibac.model.Conclusion;
import org.sibac.model.Justification;
import org.sibac.model.Information;
import org.sibac.model.Hypothesis;
import org.sibac.view.UI;
import org.sibac.model.UserInput;

import java.util.ArrayList;

import java.util.Scanner;


public class Haemorrhage {
    public static KieSession KS;
    public static BufferedReader BR;
    public static TrackingAgendaEventListener agendaEventListener;
    public static Map<Integer, Justification> justifications;



    public static final void main(String[] args) {
        UI.uiInit();
        runEngine();
        UI.uiClose();
    }

    private static void runEngine() {
        Information info = new Information();
        try {
            Haemorrhage.justifications = new TreeMap<Integer, Justification>();

            // load up the knowledge base
            KieServices ks = KieServices.Factory.get();
            KieContainer kContainer = ks.getKieClasspathContainer();
            final KieSession kSession = kContainer.newKieSession("ksession-rules");
            Haemorrhage.KS = kSession;
            Haemorrhage.agendaEventListener = new TrackingAgendaEventListener();
            kSession.addEventListener(agendaEventListener);

            kSession.setGlobal("info", info);

            // Prompt user for input
            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter age:");
            String age = scanner.nextLine();
            System.out.println("Enter physical condition (0-10):");
            String physicalCondition = scanner.nextLine();

            // Create UserInput object and set the inputs
            UserInput input = new UserInput(age, physicalCondition);

            // Insert facts into session
            kSession.insert(input);
            kSession.insert(new Hypothesis("Analisar paciente", "idade"));

            // Query listener
            ViewChangedEventListener listener = new ViewChangedEventListener() {
                @Override
                public void rowDeleted(Row row) {}

                @Override
                public void rowInserted(Row row) {
                    Conclusion conclusion = (Conclusion) row.get("$conclusion");
                    System.out.println(">>>" + conclusion.toString());

                    How how = new How(Haemorrhage.justifications);
                    System.out.println(how.getHowExplanation(conclusion.getId()));

                    // stop inference engine as soon as got a conclusion
                    kSession.halt();
                }

                @Override
                public void rowUpdated(Row row) {}
            };

            LiveQuery query = kSession.openLiveQuery("Conclusions", null, listener);

            kSession.fireAllRules();

            query.close();

            // Get the processed information
            ArrayList<String> cistoFacts = info.getCisto_facts();
            ArrayList<String> uroFacts = info.getUro_facts();

// Process or display the information as needed
            for (String fact : cistoFacts) {
                System.out.println(fact);
            }
            for (String fact : uroFacts) {
                System.out.println(fact);
            }

        } catch (Throwable t) {
            t.printStackTrace();
        }
    }

}

