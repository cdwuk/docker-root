
# create the local image
docker image build -t cdwuk/python-basic:v1.0.0 .

# run the local image
docker container run --rm -i -t cdwuk/python-basic:v1.0.0

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-basic:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/python-basic:v1.0.0