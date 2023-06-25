# minikube-docker-flask-mysql

Minikube/Docker/Flask/MySQL  
setup  
1.install minikube  
2.start the minikube cluster with driver by your choosing,  
mine is docker  
`minikube start --driver=docker`  
you can check whether everything is okay by running   
`minikube profile list `

results:
| Profile  | VM Driver | Runtime | IP            | Port | Version  | Status   | Nodes | Active |
|----------|-----------|---------|---------------|------|----------|----------|-------|--------|
| minikube | docker    | docker  | 192.168.49.2  | 8443 | v1.26.1  | Running  | 1     | *      |


use `minikube ssh ` to connect to your local cluster  

install kubectl inside the minikube

`curl -LO https://dl.k8s.io/release/v1.27.0/bin/linux/amd64/kubectl  
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl  
chmod +x kubectl  
mkdir -p ~/.local/bin  
mv ./kubectl ~/.local/bin/kubectl  
echo $PATH  
export PATH=$PATH:\~/.local/bin  
echo $PATH  

sudo cp /etc/kubernetes/admin.conf /home/docker/config  
mkdir .kube  
mv config .kube/  
sudo chown $(id -u):$(id -g ) $HOME/.kube/config  

kubectl version --client`  

using the docker cp command copy the project files from the local machine to the minikube cluster
example:  
`docker cp /home/user/path/to/project
minikube:/home/docker/project`

Now that you have kubectl installed and the files copied to the cluster, you can use the Dockerfile + yaml to setup everything else.
For flask use `docker build -t flaski .` and inside the db directory use `docker build -t mysql` .
After that go inside the yamlKubes directory and run `kubectl apply -f banan_flask.yaml` and ` kubectl apply -f sql.yaml `

Using `kubectl get pods` and `kubectl get services` you can check whether everything is OK.
Outside of the cluster run "minikube service {name of the service}" in this case `minikube service flask-banan-service`
and you should get a link to the website.

https://github.com/kaloyanN01/minikube-docker-flask-mysql/assets/96145723/64b970e8-1a56-49af-81ee-34a4a70ed269

