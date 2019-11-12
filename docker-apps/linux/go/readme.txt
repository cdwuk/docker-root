# create the local image
docker image build -t cdwuk/go:mike .

# run the local image
docker container run --name go-mike --rm -i -t -p 8081:8080 cdwuk/go:mike

# run in cli
curl localhost:5001

# run in browser
http://localhost:8081

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-standard:v1.0.0docker

docker stop go-mike

# Delete all containers
docker rm $(docker ps -a -q)

# Delete all images
docker rmi $(docker images -q)

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push go-mike

#login to azure container registry
docker login <myregistry>.azurecr.io

docker push <myregistry.azurecr.io>/samples/go-mike

kubectl apply -f go-kube-manifest.yaml

