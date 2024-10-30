package org.sibac.model;

import java.util.ArrayList;

public class Information {
    private ArrayList<String> cisto_facts;
    private ArrayList<String> uro_facts;


    public Information(){
        this.cisto_facts = new ArrayList<>();
        this.uro_facts = new ArrayList<>();
    }

    public void addCistoInfo(String info){
        cisto_facts.add(info);
    }

    public void addUroInfo(String info){
        uro_facts.add(info);
    }


    public ArrayList<String> getCisto_facts(){
        return cisto_facts;
    }

    public ArrayList<String> getUro_facts(){
        return uro_facts;
    }

    // public processInformation(){
    //     return explicacao;
    // }





}


