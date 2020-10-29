![Udacity Flask ML CI/CD](https://github.com/femog008/UdacityFlaskMLProject/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# Overview

This is and End-To-End Project that illustrates building a CI/CD for your development tasks.

A successfully implementation and deployment of the CI/CD should eliminate manual testing, building and deployment of source code.

The following sections will be address in this project:

* Setup and configure Continous Integration
    --Add Github Repository
    --Add Github Actions to Repository
    --Add Test/Lint to the code base
    --Deploy and Test CI functionality

* Setup and configure Continous Delivery
    --Add/Create a project to Azure DevOps
    --Setup Virtual environment
    --Configure a Pipeline
    --Test CD functionality on Azure PipeLine


## Project Plan

Find links to the Project Plan/Board below:

* [Project Plan Google Sheets](https://trello.com/b/9fkfM44w/udacity-flaskml-cicd).
* [Project Plan Trello Board](https://docs.google.com/spreadsheets/d/1SjQ7rr3Z2w4xwnkOLhOgVUFBdpgUWeWlp3MD_4WFXwU/edit#gid=311255061).

## Instructions

![CD/CI Arquitecture](images/Screenshot_1.png?raw=true "CD/CI Arquitecture")

Create a Repository

* Log into your Github account and create a repostory.

![Repository](images/Screenshot_2.png?raw=true "New Repo")

* Log into Azure Cloud Shell and create a webapp
    `az webapp up -n projectName`
    
* Create ssh-keys in Azure Cloud Shell
    Run the command: `ssh-keygen -t rsa"`
    ![Alt text](images/Screenshot_4.png?raw=true "Generate SSH Key")
        
* Upload ssh-keys to Github
    Under Profile settings, click on "SSH and GPG Keys" and add the generated SSH Key
    ![Alt text](images/Screenshot_5.png?raw=true "Add SSH Key")
    
* Clone Github repo on cloud shell
    Run the command: `git clone "{Link to Github Repository}"`
    ![Alt text](images/Screenshot_6.png?raw=true "Clone repo")   
    
* Add your python code/source files

* Add a Makefile and define test file. Create a Makefile and define the following section as show below:
    ![Alt text](images/Screenshot_7.png?raw=true "Add Makefile")    
    ![Alt text](images/Screenshot_8.png?raw=true "Add test file")    
    
* Run a local test to ensure the test with pylint is working 
    Run the command: `make all` and confirm all tests pass
    ![Alt text](images/Screenshot_9.png?raw=true "Run make all")

To configure Continous Delivery

* Login to [Azure DevOps](https://dev.azure.com)
* Add a Project
* Add a Pipeline
* Select Github under `Where is your code?`
    ![Alt text](images/Screenshot_10.png?raw=true "Add pipeline")
    
* Select the right repository
    ![Alt text](images/Screenshot_11.png?raw=true "choose repository")
    
* Select the option as shown below:
    ![Alt text](images/Screenshot_12.png?raw=true "choose Python To Linux")
    
* Select your subscription and login:
    ![Alt text](images/Screenshot_13.png?raw=true "Choose subscription")
    
* Select your wepapp name, validate and configure:
    ![Alt text](images/Screenshot_14.png?raw=true "choose webapp")
    
* A succesfull deployment will be similar to the screenshot below:
    ![Alt text](images/Screenshot_15.png?raw=true "Add pipeline")
    
* Running Azure App Service from Azure Pipelines automatic deployment 
    `The webapp is successfully deployed and running`
    ![Alt text](images/Screenshot_3.png?raw=true "Running WebApp")
    ![Alt text](images/Screenshot_16.png?raw=true "App via browser")
    
* Test the Deployed Service.
    `Run the following script from the deployment folder in cloud shell:`
    ```bash
    udacity@Azure:~$ ./make_predict_azure_app.sh
    Port: 443
    {"prediction":[20.35373177134412]}
    ```
    
    A similar result is expected as shown above:
    ![Alt text](images/Screenshot_17.png?raw=true "Prediction Result")
    
* Output from streamed Log File shows activity confirming the previous test:
    ![Alt text](images/Screenshot_18.png?raw=true "Log ")

## Enhancements

There is still room for improvement:

* Configure Release for Flask ML API
* Enhance the Frontend to include a User-Friendly interface to make predictions.

## Demo 

<TODO: Add link Screencast on YouTube>


