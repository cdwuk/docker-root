# This exercise shows how to containerise a very simple bit of code that runs in ASP.NET Core. 

# ** Important - VS code folder on LHS must be set to WebformsBasic and set your name in the image below!!! ******************


# open a new terminal and paste
docker image build -t cdwuk/webforms:my-name-here -f ./webformsbasic/Dockerfile . 

docker run -it --rm -p 5014:80 --name aspnetapp cdwuk/webforms:my-name-here

docker stop aspnetapp

docker ps

# run in browser
http://localhost:5014

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/aspnetapp:v3

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/aspnetapp:v3

