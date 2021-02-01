# Overview

Deploy Python machine learning app using Azure Cloud Shell, and Azure pipeline.

## Project Plan

* A link to a Trello board for the project
> [Trello board link](https://trello.com/b/OsHpFeHa/azure-ci-cd-pipeline-with-ml)

* A link to a spreadsheet that includes the original and final project plan
> [Project management spreadsheets link](https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/tree/main/Project%20management%20spreadsheets)

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

### Instructions for running the Python project.

* Azure Cloud Shell Python version was 3.7.3 when this repo was made.

* Clone the project repo to Azure Cloud Shell
> git clone http://github.com/JehyeonHeo/building-CICD-pipeline-with-azure.git

<img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Github-repo-clone-to-Azure-cloud-shell.png?raw=true" title="Project cloned into Azure Cloud Shell"></img><br/>

* Checkout 'CI-learning' branch to experience continuous integration using Github Actions.
> cd building-CICD-pipeline-with-azure
> git checkout CI-learning

* Run 'make all' command to install packages, lint and test hello.py.
> make all

<img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Local-test-passed.png?raw=true" title="Passing tests after running the `make all` command from the `Makefile`"></img><br/>

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Project running on Azure App Service

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.

* Output of streamed log files from deployed application

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


