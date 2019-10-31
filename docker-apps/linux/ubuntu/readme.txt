# This exercise shows how to containerise a very simple bit of code that runs in Ubuntu Linux. 

# ************  Set your name in the image!!! ******************

# prepare to build image
cd <this directory that contains Dockerfile>

# have a look at the Dockerfile and try and understand what it is doing

# create the local image
docker image build -t cdwuk/ubuntu-test:my-name-here .

# run the local image in a container hosted in a Linux VM hosted on your laptop
docker container run --name ubuntu-container --rm -i -t cdwuk/ubuntu-test:my-name-here

# show all containers running or not
docker ps -a

docker stop ubuntu-container 

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/ubuntu-test:my-name-here