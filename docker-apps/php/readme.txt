
# create the local image
docker image build -t cdwuk/php-app:v1.0.0 .

# run the local image
docker run -it --rm  --name php-app -p 5002:80 cdwuk/php-app

docker run --rm -p 8000:80 php:apache

php:apache

docker ps

curl localhost:5002

# run in browser
http://localhost:5002

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/cdwuk/php-app:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/cdwuk/php-app:v1.0.0