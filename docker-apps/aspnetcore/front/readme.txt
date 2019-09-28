# prepare to build image
cd <this directory that contains Dockerfile>

# create the local copy of image
docker image build -t cdwuk/aspnetcorefront .

# run the local image
docker container run --name asp_net_core_front_end --rm -i -t cdwuk/asp-net-core-front-end:0.1

docker run -d -p 5005:80 -it --rm  cdwuk/aspnetcorefront

# show all containers running or not
docker ps -a

## show logs for this container
docker logs -f asp_net_core_front_end 

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/asp-net-core-front-end:0.1

docker stop asp_net_core_front_end 

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/asp-net-core-front-end:0.1