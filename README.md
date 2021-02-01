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

* Make virtual environment
> python3 -m venv ~/.myrepo

* Clone the project repo to Azure Cloud Shell
> git clone http://github.com/JehyeonHeo/building-CICD-pipeline-with-azure.git

<img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Github-repo-clone-to-Azure-cloud-shell.png?raw=true" title="Project cloned into Azure Cloud Shell"></img>

* Checkout 'CI-learning' branch to experience continuous integration using Github Actions.
> cd building-CICD-pipeline-with-azure
> git checkout CI-learning

* Run 'make all' command in virtual environment to install packages, lint and test hello.py.
> source ~/.myrepo/bin/activate
> make all

<img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Local-test-passed.png?raw=true" title="Passing tests after running the `make all` command from the `Makefile`"></img>

* Checkout 'main' branch to experience continuous deployment using Azure pipeline.
> rm -r \__pycache__
>
> git checkout main

* Run python app locally to check whether the app shows normal prediction result.
> pip install -r requirements.txt
>
> export FLASK_APP=app.py
>
> flask run
> 
> \# You can check the app running in the terminal. Press 'paper + magnifier' icon as you can see below. And then configure port 5000 to see the app.
>  <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Web-preveal-button.png?raw=true" title="Web preveal button"></img>
>
>  <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Port-configuration.png?raw=true" title="Port configuration"></img>
>
> \# You can check the app. The result page will be similar to below picture.
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/App-checking-in-local.png?raw=true" title="App checking in local"></img>
>
> \# Open another Azure Cloud Shell by clicking 'New session' icon.
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/New-session-icon.png?raw=true" title="New session icon"></img>
>
> \# Run 'make_prediction.sh' in another Cloud Shell to check the prediction result.
> cd building-CICD-pipeline-with-azure
>
> ./make_prediction.sh
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/App-result-checking-in-local.png?raw=true" title="App result checking in local"></img>

* 

* Successful deploy of the project in Azure Pipelines.

* Project running on Azure App Service

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.

* Output of streamed log files from deployed application

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


