
# create the local image
docker image build  -t  aspnetcorelinuxfrontend:latest .

# run the local image
docker container run --name asp_net_core --rm -it -p:5003:80 aspnetcorelinuxfrontend:latest

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/aspnetcorelinuxfrontend:latest
