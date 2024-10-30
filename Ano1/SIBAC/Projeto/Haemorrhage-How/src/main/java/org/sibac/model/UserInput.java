package org.sibac.model;

public class UserInput {
    private String age;
    private String physicalCondition;

    public UserInput(String age, String physicalCondition){
        this.age = age;
        this.physicalCondition = physicalCondition;
    }

    // Getters and setters
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getPhysicalCondition() {
        return physicalCondition;
    }

    public void setPhysicalCondition(String physicalCondition) {
        this.physicalCondition = physicalCondition;
    }
}