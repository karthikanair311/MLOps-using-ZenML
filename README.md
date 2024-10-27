# Introduction to ZenML

pip install zenml["server"]
zenml init
zenml up --blocking  (in windows)

Zenml has a feature, that is it uses the cached version, if there is no changes in the code or there is no change in the step then it will use the step from the previous run.

# Experiment Tracker

When you do data science engineering on real world data, you want to track every runs because you need to tweak the parameters then check it re run, compare with the metrices performing in the 38th run or in the 1st run. It will be implemented on the trained model.

zenml integration install mlflow -y
zenml stack list 
zenml stack describe                                
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow --flavor=mlflow
zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
zenml stack delete -y mlflow_stack

# UI for experiment tracker

mlflow ui --backend-store-uri "PATH"


