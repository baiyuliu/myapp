# Trigger pipline
Upate any file under "server/swagger_server/".
That is the app foler.

# How to access the serivce 
It running as "NodePort" service.
Access it by your k8s node IP and port map to 300
From my side use "http://192.168.0.252:3087"
```
[root@k8s-master1 server]# kubectl get service
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
database-service   ClusterIP   10.109.78.184    <none>        3306/TCP         23h
kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP          3d22h
web-service        NodePort    10.110.192.218   <none>        3000:30872/TCP   23h
[root@k8s-master1 server]#
[root@k8s-master1 server]# kubectl get node -o wide
NAME          STATUS   ROLES                  AGE     VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE                KERNEL-VERSION           CONTAINER-RUNTIME
k8s-master1   Ready    control-plane,master   3d22h   v1.21.0   192.168.0.251   <none>        CentOS Linux 7 (Core)   3.10.0-1160.el7.x86_64   docker://24.0.2
k8s-node1     Ready    <none>                 3d21h   v1.21.0   192.168.0.252   <none>        CentOS Linux 7 (Core)   3.10.0-1160.el7.x86_64   docker://24.0.2
[root@k8s-master1 server]# kubectl get pod -o wide
NAME                                  READY   STATUS    RESTARTS   AGE   IP            NODE        NOMINATED NODE   READINESS GATES
database-deployment-876c89b5c-546gm   1/1     Running   0          23h   10.244.1.10   k8s-node1   <none>           <none>
web-deployment-f764b4b6c-mpp5d        1/1     Running   0          23h   10.244.1.9    k8s-node1   <none>           <none>

```

## TEST the interface
swagger_ui with the path "/ui"
form my side:
"http://192.168.0.252:3087/ui"

# test on local for developer 
just run:
docker-compose up -d --build


# Deploy the app
The helmchart file under "mychart" folder.
```
helm install my-release mychart  #for install
helm upgrade my-release mychart  #for update
```
you also can apply the k8s yaml files.
they are under "k8s"


# structure
├── database.Dockerfile
├── docker-compose.yaml
├── k8s
│   ├── database-deployment.yaml
│   ├── mysql-secret.yaml
│   └── web-deployment.yaml
├── mychart
│   ├── Chart.yaml
│   ├── templates
│   │   ├── database-deployment.yaml
│   │   ├── _helpers.tpl
│   │   ├── mysql-secret.yaml
│   │   └── web-deployment.yaml
│   └── values.yaml
├── mysql
│   └── init.sql
├── readme.md
├── requirements2.txt
├── requirements.txt
├── swagger_server
│   ├── controllers
│   │   ├── authorization_controller.py
│   │   ├── health_controller.py
│   │   ├── history_controller.py
│   │   ├── metrics_controller.py
│   │   ├── root_controller.py
│   │   └── tools_controller.py
│   ├── encoder.py
│   ├── __main__.py
│   ├── models
│   │   ├── base_model_.py
│   │   ├── handler_validate_ip_request.py
│   │   ├── handler_validate_ip_response.py
│   │   ├── __init__.py
│   │   ├── model_address.py
│   │   ├── model_query.py
│   │   └── utils_http_error.py
│   ├── swagger
│   │   ├── swagger.json
│   │   └── swagger.yaml
│   ├── test
│   │   ├── __init__.py
│   │   ├── test_health.py
│   │   ├── test_history_controller.py
│   │   └── test_tools_controller.py
│   ├── type_util.py
│   └── util.py
├── test.Dockerfile
└── web.Dockerfile
