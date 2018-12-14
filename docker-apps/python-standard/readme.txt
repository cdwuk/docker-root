
# create the local image
docker image build -t cdwuk/python-standard:v1.0.0 .

# run the local image
docker container run --name python-standard --rm -i -t -p 5001:5000 cdwuk/python-standard:v1.0.0

# 
curl localhost:5001

# run in browser
http://localhost:5001

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-standard:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/python-standard:v1.0.0

kubectl create -f service.yaml