
# create the local image
docker build -t cdwuk/php-app .

# run the local image
docker run -it --rm  --name my-running-app cdwuk/php-app

docker ps

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-standard:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/php-app