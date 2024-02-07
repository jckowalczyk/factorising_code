# Factorising Code 

The following repository contains a worked example from the ONS Data Science Graduate Programme of turning an analysis script into functionalised and modular scripts, grouped by functionality. 

## Introduction 

Working with the United Nations (UN), you have been tasked with obtaining population densities for each Sustainable develop Goal region. A colleague of yours has written some code to complete this task, where the data is cleaned, formatted and analysed. Our goal here is to restructure this code into a reproducible  workflow, using concepts from modular programming.

Modular programming can turn larger scripts into smaller, stand alone isolated modules. This approach can help promote maintainability, flexibility, and while has an initial time cost, can help reduce the amount of time needed for development. It can also be reused in other projects.

The following repository contains a worked example from the ONS Data Science Graduate Programme of turning an analysis script into functionalised and modular scripts, grouped by functionality. 

## Key Concepts

 - Single purpose functions 
 - Reducing repetition 
 - Scope of a function (Global vs Local)
 - Creating pure functions 

## Order 

The data can be found in the data folder. 

In the scripts folder, there are 5 scripts. 

- 0_starting_script.py refers to the initial script to be restructured
- data_read.py, manipulation.py, and analysis.py are restructured modules containing the neccasary functiosn to complete the same task, but in a way that uses modular programming concepts 
- the main.py script runs all of these, and produces the output. 
- the output "mean_population_density_output.csv", can be found in the outputs folder. 