
# create the local image
docker image build -t cdwuk/python-standard:v1.0.0 .

# run the local image
docker container run --name python-standard --rm -i -t -p 5000:5000 cdwuk/python-standard:v1.0.0

# run in cli
curl localhost:5001

# run in browser
http://localhost:5001

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-standard:v1.0.0docker

docker stop python-standard

# Delete all containers
docker rm $(docker ps -a -q)

# Delete all images
docker rmi $(docker images -q)

#login to docker hub
docker login --username cdwuk

#login to azure container registry
docker login <myregistry>.azurecr.io

# push the image to docker hub
docker push cdwuk/python-standard:v1.0.0

docker push <myregistry.azurecr.io>/samples/nginx

# login to azure container registry
az acr login --name <myregistry>

kubectl create -f deploy.yaml