package org.sibac.fcl;

import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.rule.Variable;
import org.sibac.model.Conclusion;
import org.sibac.model.Hypothesis;

import java.io.File;
import java.io.InputStream;

public class FuzzyLogicHelper {
    private FIS fis;

    public FuzzyLogicHelper(String fclFileName) {
        // Print the current working directory
        //String currentWorkingDir = System.getProperty("user.dir");
        //System.out.println("Current Working Directory: " + currentWorkingDir);

        // Load the FCL file using the FIS.load() method
        this.fis = FIS.load(fclFileName,true);
        if( fis == null ) {
            System.err.println("Can't load file: '" + fclFileName + "'");
        }
    }

        public double getViability(double age, double physicalCondition) {

        fis.setVariable("age", age);
        fis.setVariable("physicalCondition", physicalCondition);
        fis.evaluate();
        Variable viability = fis.getVariable("risk");
        return viability.getValue();
    }

    public Hypothesis returnconclusion(double viability){
        Hypothesis c;
        System.out.print(viability);
        if (viability < 50.0) {
            c = new Hypothesis("Prosseguir tratamento", "apto");
        } else {
            c = new Hypothesis("Prosseguir tratamento", "nao apto");
        }

        return c;
    }

    public Hypothesis returnconclusion_uro(double viability){
        Hypothesis c;
        System.out.print(viability);
        if (viability < 50.0) {
            c = new Hypothesis("Prosseguir tratamento-uro", "apto-uro");
        } else {
            c = new Hypothesis("Prosseguir tratamento-uro", "nao apto-uro");
        }

        return c;
    }
}
