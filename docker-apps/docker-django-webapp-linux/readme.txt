docker stop $(docker ps -aq)

docker rm $(docker ps -aq)

docker ps -aq

# create the local image
docker image build -t cdwuk/python-django:v1.0.0 .

# run the local image
docker container run -it --rm  cdwuk/python-django:v1.0.0

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-standard:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/python-django:v1.0.0