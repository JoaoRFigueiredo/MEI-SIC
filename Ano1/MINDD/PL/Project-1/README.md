# Project Number 1

## External packages/libraries

Some packages/libraries used in this project are not included in anaconda, so one must manually add them to the environment.

I will provide a file, "imports.txt", which will have the name of all packages outside of the conda environment and a way to install them.

Open a console on the project directory and type these commands.
```
conda activate
pip install -r imports.txt
conda deactivate
```


## Introduction

We were a given a dataset, with 35 columns and ~70k rows. It is related to bank and it's clients, more specificaly, clients with loans. On top of the many features present (variables/labels), there is one that identifies a client as defaulter or non-defaulter regarding to their loan. Pretty much, this indicates wether the client is going to pay his monthly amount on time or not. The goal is to build models that predict such matter. To achieve this goal, there 4 essential steps that one must follow.

## Methodology

Like it was said previously, we must follow these 4 steps to ensure that the models work as intended:

- Data Exploration
- Data Preprocessing
- Model Classifications
- Model Evaluation
