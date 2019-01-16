# Introduction to Azure Machine Learning service
This series of labs introduces core features of Azure Machine Learning service and demonstrates how AML service can be used to orchestrate machine learning workflows. The labs  walk you through the key phases of a machine learning workflow: from data preparation, through model selection and tuning, to model operationalization.


## Lab environment set up

The Azure Machine Learning service is platform agnostic. The only requirements for your development environment are Python 3, Conda (for isolated environments), and a configuration file that contains your Azure Machine Learning workspace information.

The following development environments are supported: 
- **Azure Notebooks**
- **The Data Science Virtual Machine**
- **Jupyter Notebooks**
- **Visual Studio Code**
- **Visual Studio**
- **PyCharm**
- **Azure Databricks**

In this workshop we will use Linux (Ubuntu) **Azure Data Science Virtual Machine** as the lab environment.

The DSVM comes with all the pre-requisities pre-installed. No additional configuration is required.

### To provision Azure Data Science Virtual Machine

1. Follow the instructions at

https://ms.portal.azure.com/#create/microsoft-ads.linux-data-science-vm-ubuntulinuxdsvmubuntu


1. After the DSVM is provisioned connect to the pre-installed Jupyter server at:

`https://<your IP address or DNS>:8000`
  
1. In Jupyter open a terminal and clone this repository under the `notebooks` folder.

1. If you need to update the DSVM to install/update Python libraries - E.g. Azure ML SDK.
```
sudo -i
source activate py36
# update packages
exit
```


1. Follow the instructor who will walk you through the labs.

