# create the local image
docker image build -t cdwuk/go:latest .

# run the local image
docker container run --name go --rm -i -t -p 8081:80 cdwuk/go:latest

# run in cli
curl localhost:8081

# run in browser
http://localhost:8081

docker ps

docker stop go

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/go:latest

#login to azure container registry
docker login <myregistry>.azurecr.io

docker push <myregistry.azurecr.io>/samples/go-mike

kubectl apply -f go-kube-manifest.yaml

