# This exercise shows how to containerise a very simple bit of code that runs in ASP.NET Core. 

# ** Important - VS code folder on LHS must be set to ASP-NET-CORE and set your name in the image below!!! ******************


# open a new terminal and paste
docker image build -t cdwuk/aspnetapp:v3 -f ./aspnetapp/Dockerfile . 

docker run -it --rm -p 80:8080 --name aspnetapp cdwuk/aspnetapp:v3

docker stop aspnetapp

docker ps

# run in browser
http://localhost:5014

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/aspnetapp:v3

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/aspnetapp:v3

