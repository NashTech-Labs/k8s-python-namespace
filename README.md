# namespace

#### Python client for the kubernetes API

we can use the client module to interact with the resources. 

`Resources:` kubectl get commands are used to create namespaces using yaml files or ad-hoc command in a cluster for eg:

To create the namespaces in the cluster, we fire following kubectl command:

```kubectl apply -f namespace.yaml``` 

or we can create by adhoc command

`kubectl create namespace namespace1`

Get the list of all namespace

`kubectl get namespace`

`kubectl get ns`

But In Python, we instantiate CoreV1Api class from client module:

`client_api = client.CoreV1Api()`

Here I've created the client with it's respective class CoreV1Api
and storing in a var named as client_api. so furture we can use it.

`KubeConfig:` to pass the on local cluster e.g minikube we use bellowcommand: 

`config. load_kube_config()`

#### Authenticating to the Kubernetes API server

But what if you want to list all the automated cronjobs of a GKE Cluster, you must need to authenticate the configuration

`configuration.api_key = {"authorization": "Bearer" + bearer_token}` 

I've used Bearer Token which enable requests to authenticate using an access key.

#### Creating namespaces:

Call the funcation create_namespace(cluster_details,"n1")

And replace n1 with any name of the namespace you want to create.

And run following command:

`python3 namespace.py`

#### get the list of all namespaces:

call the funcation  get_namespace(cluster_details)

`python3 namespace.py`

#### delete namespace:

call the funcation  delete_namespace(cluster_details, "n1")

And replace n1 with any name of the namespace you want to delete.

`python3 namespace.py`
