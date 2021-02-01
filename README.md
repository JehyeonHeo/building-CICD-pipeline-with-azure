# Overview

Deploy Python machine learning app using Azure Cloud Shell, and Azure pipeline.

## Project Plan

* A link to a Trello board for the project
> [Trello board link](https://trello.com/b/OsHpFeHa/azure-ci-cd-pipeline-with-ml)

* A link to a spreadsheet that includes the original and final project plan
> [Project management spreadsheets link](https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/tree/main/Project%20management%20spreadsheets)

## Instructions

* Architectural Diagram of Continuous Integration
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/CI-architecture.png?raw=true" title="CI architecture diagram"></img>

* Architectural Diagram of Continuous Delivery
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/CD-architecture.png?raw=true" title="CD architecture diagram"></img>

### Instructions for running the Python project.

* Azure Cloud Shell Python version was 3.7.3 when this repo was made.

* Make virtual environment
> python3 -m venv ~/.myrepo

* Clone the project repo to Azure Cloud Shell
> git clone http://github.com/JehyeonHeo/building-CICD-pipeline-with-azure.git
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Github-repo-clone-to-Azure-cloud-shell.png?raw=true" title="Project cloned into Azure Cloud Shell"></img>

* Checkout 'CI-learning' branch to experience continuous integration using Github Actions.
> cd building-CICD-pipeline-with-azure
> git checkout CI-learning

* Run 'make all' command in virtual environment to install packages, lint and test hello.py.
> source ~/.myrepo/bin/activate
> make all
> 
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Local-test-passed.png?raw=true" title="Passing tests after running the `make all` command from the `Makefile`"></img>

* Checkout 'main' branch to experience continuous deployment using Azure pipeline.
> rm -r \_\_pycache__
>
> git checkout main

* Run python app in Cloud Shell to check whether the app shows normal prediction result.
> pip install -r requirements.txt
>
> export FLASK_APP=app.py
>
> flask run
> 
> \# You can check the app running in the terminal. Press 'paper + magnifier' icon as you can see below. And then configure port 5000 to see the app.
>
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
>
> cd building-CICD-pipeline-with-azure
>
> ./make_prediction.sh
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/App-result-checking-in-local.png?raw=true" title="App result checking in local"></img>

* Stop running app in original terminal.

* Deploy app using 'commands.sh' file which includes 'az webapp' command. This process can take some time. Press below code in the original terminal.
> ./commands.sh

* After deployment finishes, enter URL to browser to check the app running on Azure App Service. The result will be similar to below screenshot.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Azure-app-service-deploy-status.png?raw=true" title="Azure app service deploy status"></img>

* Check successful prediction from deployed flask app in Azure Cloud Shell. Use 'make-predict-azure-app.sh' file.
> ./make-predict-azure-app.sh
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Verify prediction.png?raw=true" title="Verify prediction"></img>

* Go to Azure DevOps Organizations to make pipeline.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Enter-to-devops-organizations.png?raw=true" title="Enter to devops organizations"></img>

* Click 'new project' and fill out project name and description.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Fill-project-name.png?raw=true" title="Fill project name"></img>

* After new project is made, click 'pipelines' to make pipeline for deployed app.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Create-pipeline.png?raw=true" title="Create pipeline"></img>

* Click 'New pipeline', connect Github, and select 'building-CICD-pipeline-with-azure' repo.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Select-repo.png?raw=true" title="Select repo"></img>

* Select 'Python to Linux Web App on Azure' in configure window, and then select 'boston-housing-prediction-flask' app and click validate&configure button.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Select-app.png?raw=true" title="Select app"></img>

* Click 'Save and run' button to run pipeline. After pipeline run successfully, you can see the result similar to below screenshot.
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Pipeline-success.png?raw=true" title="Successful deploy of the project in Azure Pipelines"></img>

* From now on, if you change something in app.py and push the change to Github, Azure pipeline will automatically deploy the revised app. Below screenshots are one of a example.
>  \# Revise webapp page header
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Revise-h3.png?raw=true" title="Revise h3 header"></img>
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Push-code-to-github.png?raw=true" title="Push code to Github"></img>
>
> \# Automatically deploy revised app
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Automatic-deploy.png?raw=true" title="Automatic deploy"></img>

* Run 'locustfile.py' in your local python environment to do load test for the deployed app.
> pip install locust
>
> locust -f locustfile.py
>
> \# Enter 'localhost:8089' in your browser to do load test. Below screenshot is the example test result.
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Load-test-using-locust.png?raw=true" title="Load test using locust"></img>

* You can see the output of streamed log files.
> Log stream address: https://boston-housing-prediction-flask.scm.azurewebsites.net/api/logstream
>
> <img src="https://github.com/JehyeonHeo/building-CICD-pipeline-with-azure/blob/main/Screenshots/Logstream-result.png?raw=true" title="Logstream result"></img>

## Enhancements

1. Change app to voice or image recognition app or other prediction app.
2. Use Github Actions instead of Azure pipeline for Continuous Delivery. 

## Demo 

<TODO: Add link Screencast on YouTube>


