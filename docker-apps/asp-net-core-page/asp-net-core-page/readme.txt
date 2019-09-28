
# create the local image
docker image build  -t  cdwuk/asp-net-core-page:v1.0.0 .

# run the local image
docker container run --name asp_net_core --rm -i -t cdwuk/asp-net-core-page:v1.0.0 -p:81

#login to docker hub
docker login --username cdwuk
#Password: Qwerty===1

# push the image to docker hub
docker push cdwuk/asp-net-core-page:v1.0.0

