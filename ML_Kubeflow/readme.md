# Kubeflow on Azure Walkthrough

Use Azure Cloud Shell to execute the following commands.

## Create AKS 
Create a resource group to host AKS.
```
az group create --name <RESOURCE_GROUP_NAME> --location <LOCATION>
```

Create the GPU AKS cluster
```
az aks create --node-vm-size Standard_NC6 --resource-group <RESOURCE_GROUP_NAME> --name <NAME> 
--node-count 3 --kubernetes-version 1.11.6 --location <LOCATION> --generate-ssh-keys
```
Get the `kubeconfig` file.
```
az aks get-credentials --name <NAME> --resource-group <RESOURCE_GROUP_NAME>
```

## Install ksonnet version 0.13.1 or later
```
cd
mkdir ksonnet
cd ksonnet
wget https://github.com/ksonnet/ksonnet/releases/download/v0.13.1/ks_0.13.1_linux_amd64.tar.gz
tar -xvf ks_0.13.1_linux_amd64.tar.gz
export PATH=$PATH:~/ksonnet/ks_0.13.1_linux_amd64/
```

## Install Kubeflow
1. Download Kubeflow CLI utility - `kfctl.sh`.
```
KUBEFLOW_SRC=~/kubeflowlabs
mkdir ${KUBEFLOW_SRC}
cd ${KUBEFLOW_SRC}
export KUBEFLOW_TAG=v0.4.1

curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/scripts/download.sh | bash
```

2. Set up and deploy Kubeflow
```
KFAPP=my-kubeflow
${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform none
cd ${KFAPP}
${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s
${KUBEFLOW_SRC}/scripts/kfctl.sh apply k8s
```



