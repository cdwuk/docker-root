
# This exercise shows how to containerise a very simple PHP football web application. 

# ************  Set your name in the image!!!

# create the local image
docker image build -t cdwuk/php-app:my-name-here .

# add additional tags to the same image by rebuilding image
docker build -t cdwuk/php-app -t cdwuk/php-app:liverpool -t cdwuk/php-app:latest .

# run the local image
docker run -it --rm  --name php-app -p 5002:80 cdwuk/php-app:liverpool

docker ps

curl localhost:5002

# run in browser
http://localhost:5002

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/cdwuk/php-app:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/php-app:v1.0.0

docker push cdwuk/php-app:latest


#login to azure container registry
docker login <myregistry>.azurecr.io

docker push <myregistry.azurecr.io>/samples/php-app:latest