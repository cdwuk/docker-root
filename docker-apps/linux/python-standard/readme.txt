
# This exercise shows how to containerise a very simple Python web application. 

# ********** Important - VS code folder on LHS must be set to PYTHON-STANDARD and set your name in the app.py and image below!!! *******

# open the Dockerfile on LHS and try to work out what is does

# open app.py and overwrite you name - save file

# create the local image. cdwuk refers to the repository, python-standard refers to the application and my-name-here is the tag for this application 
docker image build -t cdwuk/python-standard:my-name-here .

# add 3 additional tags to the same image by rebuilding image. Note we add a version.
docker build -t cdwuk/python-standard:v1.0.0 -t cdwuk/python-standard -t cdwuk/python-standard:latest .

# run the local image in a container hosted in a Linux VM hosted on your laptop
docker container run --name python-web-app --rm -i -t -p 5001:5000 cdwuk/python-standard:my-name-here

# view html returned from the web app in the command line window
curl localhost:5001

# run in browser
http://localhost:5001

# open a new terminal window and run docker ps
docker ps

# use CTL -c to stop the container

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to DockerHub - make sure you have built this image with the tag specified below

docker push cdwuk/python-standard:v1.0.0

# *********** CONGRATULATIONS - you now know how to containerise a PYthon web app application. ****************

# list all running containers
docker container ls -aq

# Stop all containers
docker container stop $(docker container ls -aq)

# Delete all containers
docker rm $(docker ps -a -q)

# Delete all images
docker rmi $(docker images -q)

# ==========Kubernetes ======== you will need an Azure subscription to do this ===================
# You are now going to use the Azure 'az' command to perform tasks in Azure

# create a new resource group in your Azure subscription 
az group create -l westeurope -n myrg

# create AKS cluster using your unique name
az aks create -g myrg -n aks-my-name

# download credentials into local file
az aks get-credentials --name aks-my-name --resource-group myrg

#test that credentials work ok
kubectl get all

# deploy nginx web server image from Docker Hub to your kubernetes cluster
kubectl run  –n nginx --image=nginx  
kubectl expose deployment nginx --name=nginx

# deploy python app to your kubernetes using the YAML file
kubectl apply -f python-kube-manifest.yaml

# ========== Azure Container Registry below ============
# create an Azure Container Registry
az acr create -n acr-my-name -g myrg --sku Standard

# login to azure and then to Azure Container Registry
az login
az acr login --name acr-my-name.azurecr.io

docker push acr-my-name.azurecr.io/samples/python-standard:v1.0.0




