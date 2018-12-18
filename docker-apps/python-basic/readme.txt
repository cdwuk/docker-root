
# create the local image
docker image build -t cdwuk/python-basic .

$ docker build -t cdwuk/python-basic:v1.0.0 -t cdwuk/python-basic:latest .

# run the local image
docker container run --name python_basic --rm -i -t cdwuk/python-basic:v1.0.0

# show all containers running or not
docker ps -a

## show logs for this container
docker logs -f python_basic 

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-basic:v1.0.0

docker stop python_basic 

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/python-basic:v1.0.0