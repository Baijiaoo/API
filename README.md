# Real-Estate-Agent-Scoring-System
This project aims to design Agent Scoring System which combines Machine Learning & Full Stack Design

## Requirment
* Installing evritual enviroment on your PC to avoid Python libirary version confliction:
  * **$ pip install virtualenv**
* Setting up vitual enviroment:
  * **$ virtualenv venv**
* Pointing to which version of python you want to use under virtual enviroment:
  * **$ virtualenv -p c:\python3\python.exe venv**
* Activating virtual enviroment:
  * **$ activate venv**
* Deactivating virtual enviroment:
  * **$ deactivate venv**

## Enviroment:
* Python 3.x (skicit-learn, Tensorflow, Django, pyecharts)
* SQL
* Pycharm / JupyterNotebook / Spider

## Project Process:
* Setting Enviroment:
  * **$ cd :/mysite**
  * **$ activate venv**
* Prediction Model:
  * Confirm current location:
    * **$ cd :/mysite/model**
  * Data Input
    * Checking whether data existing in current file **data.csv_**
    * **$ python Data_Input.py** to import data to memory
  * Data Cleaning & Wrangling
    * **$ python Data_Processing.py** to achieve six functions to clean our raw data
  * Data Merging & Motification
    * **$ python Data_Merging.py** & **$ Data_Merging.py** to prepare data we will input to our model
  * PCA (Designing Agent Scoring Criterion)
    * **$ python PCA.py** to create a class which can achieve agent_scoring_criterion
  * LSTM Modeling design
    * **$ python LSTM.py** to create a class which can achieve RNN based on Tensorflow
  * Hybrid LSTM & TimeSeries
    * **$ python Model_Hybrid.py** to combine RNN with TimeSeries and get prediction result saved in **_.json_** form   
* Application to Connect with Model Output:
  * Import model output to database:
    * **$ python test.py**
  * Running application:
    * **$ python manage.py runserver**
