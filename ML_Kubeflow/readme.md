# Kubeflow on Azure Walkthrough

## Create AKS 
```
az group create --name <RESOURCE_GROUP_NAME> --location <LOCATION>
az aks create --node-vm-size Standard_NC6 --resource-group <RESOURCE_GROUP_NAME> --name <NAME> 
--node-count 3 --kubernetes-version 1.11.6 --location <LOCATION> --generate-ssh-keys
```

## Install ksonnet version 0.13.1 or later

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



