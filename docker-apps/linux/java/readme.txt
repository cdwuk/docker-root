# ************  Set your name in the image!!! ******************

# create the local image which is stored on your laptop 
docker image build -t cdwuk/java-my-name-here .

# run the local image in a container hosted in a Linux VM hosted on your laptop
docker run -it --rm  --name java-hw cdwuk/java-my-name-here

docker ps

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/java-my-name-here
