
# create the local image
docker image build -t cdwuk/webforms-basic:v1.0.0 .

# run the local image
docker run -it --rm  --name webforms-basic -p 80:80 webforms-basic:v1.0.0

docker ps


docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/cdwuk/php-app:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/webforms-basic:v1.0.0