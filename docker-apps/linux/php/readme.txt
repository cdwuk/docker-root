
# This exercise shows how to containerise a very simple PHP Apache football web application. 
# ******* Important - VS code folder on LHS must be set to PHP and set your name in the index.php file and image below!!! *****
# e.g docker image build -t cdwuk/php-app:fred-bloggs .
#
#

# create the local image by OPENING a NEW TERMINAL WINDOW and paste in the docker image build code below. 
# Note: cdwuk refers to the repository, php-app refers to the application and my-name-here is the tag for this application. 
# the dot refers to the current directory

docker image build -t cdwuk/php-app:my-name-here .

# add additional tags to the same image by rebuilding image
docker build -t cdwuk/php-app -t cdwuk/php-app:liverpool -t cdwuk/php-app:latest .

# run the local image
docker run -it --rm  --name php-app -p 5002:80 cdwuk/php-app:liverpool

# run in browser
http://localhost:5002

#login to docker hub
#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/php-app:latest
docker push cdwuk/php-app:my-name-here
docker push cdwuk/php-app:liverpool

# why does it take so very little time to upload to DockerHub?

# ========== Azure Container Registry and Kubernetes below ============

#login to azure container registry
docker login <myregistry>.azurecr.io

docker push <myregistry>.azurecr.io/cdwuk/php-app:latest

# deploy to Kubernetes using YAML file
kubectl create -f php-k8s-manifest.yaml

# ============================================

# Delete all containers
docker rm $(docker ps -a -q)

# Delete all images
docker rmi $(docker images -q)

