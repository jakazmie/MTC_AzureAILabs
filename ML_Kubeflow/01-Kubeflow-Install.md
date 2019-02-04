# Installing Kubeflow on Azure Kubernetes Service.

## Create AKS 
Create a resource group to host AKS.
```
az group create --name <RESOURCE_GROUP_NAME> --location <LOCATION>
```

Create the GPU AKS cluster
```
az aks create --node-vm-size Standard_DS4_v2 --resource-group <RESOURCE_GROUP_NAME> --name <NAME> 
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

## Validate installation
```
kubectl get pods -n kubeflow
```

You should see something like this:

```
NAME                                                      READY     STATUS    RESTARTS   AGE
ambassador-5cf8cd97d5-5mw2v                               1/1       Running   0          3m
ambassador-5cf8cd97d5-9brlr                               1/1       Running   0          3m
ambassador-5cf8cd97d5-fw8dq                               1/1       Running   0          3m
argo-ui-7c9c69d464-cwvms                                  1/1       Running   0          2m
centraldashboard-6f47d694bd-khthp                         1/1       Running   0          3m
jupyter-0                                                 1/1       Running   0          3m
katib-ui-6bdb7d76cc-4hx8c                                 1/1       Running   0          2m
metacontroller-0                                          1/1       Running   0          2m
minio-7bfcc6c7b9-l24zw                                    1/1       Running   0          2m
ml-pipeline-6fdd759597-mvmf6                              1/1       Running   0          2m
ml-pipeline-persistenceagent-5669f69cdd-bsntj             1/1       Running   0          2m
ml-pipeline-scheduledworkflow-9f6d5d5b6-q7c52             1/1       Running   0          2m
ml-pipeline-ui-67f79b964d-g2sxb                           1/1       Running   0          2m
mysql-6f6b5f7b64-j5pwb                                    1/1       Running   0          2m
pytorch-operator-6f87db67b7-52ttv                         1/1       Running   0          3m
spartakus-volunteer-759df9954-8q9dt                       1/1       Running   0          2m
studyjob-controller-774d45f695-q7n6p                      1/1       Running   0          2m
tf-job-dashboard-5f986cf99d-8ggm5                         1/1       Running   0          3m
tf-job-operator-v1beta1-5876c48976-jh992                  1/1       Running   0          3m
vizier-core-fc7969897-wq587                               0/1       Running   1          2m
vizier-core-rest-6fcd4665d9-nx97x                         1/1       Running   0          2m
vizier-db-777675b958-gm76b                                1/1       Running   0          2m
vizier-suggestion-bayesianoptimization-54db8d594f-krqc4   1/1       Running   0          2m
vizier-suggestion-grid-6f5d9d647f-jjqf2                   1/1       Running   0          2m
vizier-suggestion-hyperband-59dd9bb9bc-bf6vm              1/1       Running   0          2m
vizier-suggestion-random-6dd597c997-4h9zs                 1/1       Running   0          2m
workflow-controller-5c95f95f58-nbt2z                      1/1       Running   0          2m
```


