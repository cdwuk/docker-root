
docker image build -t cdwuk/aspnetapp:v3 .

docker run -it --rm -p 5014:80 --name aspnetapp cdwuk/aspnetapp:v3

docker stop aspnetapp

docker ps

# run in browser
http://localhost:5012

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/aspnetapp:v3

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/aspnetapp:v3

