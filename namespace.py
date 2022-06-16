import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes import client, config
from kubernetes.client import ApiClient

def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = kubernetes.client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
            api_instance1 = kubernetes.client.CoreV1Api(api_client)
        return api_instance1

    except ApiException as e:
        print("Error getting kubernetes client:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))
        return None

def __format_data_for_create_ns(client_output):
        temp_dict={}
        temp_list=[]
        json_data=ApiClient().sanitize_for_serialization(client_output)
        #print("JSON_DATA OF KUBERNETES OBJECT:{}".format(json_data))
        
        if type(json_data) is str:
            print("FORMAT_DATA :{}".format(type(json_data)))
            json_data = json.loads(json_data)
        temp_list.append(json_data)
        return temp_list


def get_namespace(cluster_details):

    try:
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
            )
        res=client_api.list_namespace()

        data=__format_data_for_create_ns(res)
        print(data) 
        # print("list of all namespaces :{}".format(res))
    except ApiException as e:
        print("ERROR IN getting_namespace:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))


def create_namespace(cluster_details,namespace):

    try:
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
            )
        res=client_api.create_namespace(
            client.V1Namespace(
                metadata=client.V1ObjectMeta(name=namespace)
        
            ))

        print("namespace created. status='%s'" % str(res.status))

    except ApiException as e:
        print("ERROR IN creating_namespace:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))


def delete_namespace(cluster_details,namespace):

    try:
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
            )

        res=client_api.delete_namespace(namespace)
        print(res)

    except ApiException as e:
        print("ERROR IN deleting_namespace:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))


if __name__ == '__main__':
    cluster_details={
        "bearer_token":"GKE-Bearer-Token",
        "api_server_endpoint":"Ip-k8s-control-plane"
    }
    
    create_namespace(cluster_details,"n1")
    # delete_namespace(cluster_details, "n1")
    # get_namespace(cluster_details)
