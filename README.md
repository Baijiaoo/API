# Real-Estate-Agent-Scoring-System
This project aims to design Agent Scoring System which combines Machine Learning & Full Stack Design

## Requirment
* Installing evritual enviroment on your PC to avoid Python libirary version confliction:
  * $ pip install virtualenv
* Setting up vitual enviroment:
  * $ virtualenv venv
* Pointing to which version of python you want to use under virtual enviroment:
  * $ virtualenv -p c:\python3\python.exe venv
* Activating virtual enviroment:
  * $ activate venv
* Deactivating virtual enviroment:
  * $ deactivate venv

## Enviroment:
* Python 3.x (skicit-learn, Tensorflow, Django)
* SQL
* Pycharm / JupyterNotebook / Spider

## Project Process:
* Prediction Model:
  * Data Input
    * Checking whether data existing in current file **_data.csv_**
    * Running **_Data_Input.py_** to import data to memory
  * Data Cleaning & Wrangling
    * Running **_Data_Processing.py_** to achieve six functions to clean our raw data
  * Data Merging & Motification
    * Running **_Data_Merging.py_** & **_Data_Motification_.py** to prepare data we will input to our model
  * PCA (Designing Agent Scoring Criterion)
    * Running **_PCA_.py** to create a class which can achieve agent_scoring_criterion
  * LSTM Modeling design
    * Running **_LSTM_.py** to create a class which can achieve RNN based on Tensorflow
  * Hybrid LSTM & TimeSeries
    * Running **_Model_Hybrid.py_** to combine RNN with TimeSeries and get prediction result saved in **_.json_**    
* Application to Connect with Model Output:
  * Running Application:
    * $ cd :/Agent_Scoring
    * $ activate venv
    * $ python run **_manage.py_** runserver
