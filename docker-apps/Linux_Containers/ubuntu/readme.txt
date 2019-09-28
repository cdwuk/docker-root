# prepare to build image
cd <this directory that contains Dockerfile>

# create the local copy of image
docker image build -t cdwuk/ubuntu-test .

# run the local image
docker container run --name ubuntu-test --rm -i -t cdwuk/ubuntu-test

# show all containers running or not
docker ps -a

## show logs for this container
docker logs -f ubuntu-test 

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/ubuntu-test

docker stop ubuntu-test 

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/ubuntu-test