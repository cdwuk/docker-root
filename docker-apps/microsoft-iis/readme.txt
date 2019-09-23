# Important!... requires Docker VM to be running Windows

# create the local image
docker image build -t cdwuk/iis:v1.0.0 .

# run the local image
docker container run --name iis --rm -i -t cdwuk/iis:v1.0.0

# show all containers running or not
docker ps -a

## show logs for this container
docker logs -f cdwuk/iis:v1.0.0 

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/iis:v1.0.0

docker stop cdwuk/iis:v1.0.0 

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/iis:v1.0.0