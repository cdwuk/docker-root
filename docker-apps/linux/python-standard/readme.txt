
# This exercise shows how to containerise a very simple Python web application. 

# ************  Set your name in the image!!!

# create the local image which is stored on your laptop 
docker image build -t cdwuk/python-standard:my-name-here .

# add 3 additional tags to the same image by rebuilding image. Note we add a version.
docker build -t cdwuk/python-standard:v1.0.0 -t cdwuk/python-standard -t cdwuk/python-standard:latest .

# run the local image in a container hosted in a Linux VM hosted on your laptop
docker container run --name python-web-app --rm -i -t -p 5001:5000 cdwuk/python-standard:my-name-here

# view html returned from the web app in the command line window
curl localhost:5001

# run in browser
http://localhost:5001

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-standard:my-name-here

docker stop python-web-app

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to DockerHub - make sure you have built this image with the tag specified below
docker push cdwuk/python-standard:v1.0.0

# *********** congratulations!!  - you now know how to containerise an application.

# ========== Azure Container Registry and Kubernetes below ============

#login to azure container registry
docker login <myregistry>.azurecr.io

docker push <myregistry.azurecr.io>/samples/nginx

# login to azure container registry
az acr login --name <myregistry>

kubectl create -f deploy.yaml

# Delete all containers
docker rm $(docker ps -a -q)

# Delete all images
docker rmi $(docker images -q)