
# create the local image
docker image build -t cdwuk/java-hw .

# run the local image
docker run -it --rm  --name java-hw cdwuk/java-hw

docker ps

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/java-hw
