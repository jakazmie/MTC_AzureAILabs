# Kubeflow on Azure Walkthrough

## Create AKS 
## Install ksonnet version 0.13.1 or later

## Install Kubeflow
1. Download `kfctl.sh`
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



