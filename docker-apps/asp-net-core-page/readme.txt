
# create the local image
docker image build -t cdwuk/asp-net-core-page:v1.0.0 .

# run the local image
docker container run cdwuk/asp-net-core-page:v1.0.0

#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/asp-net-core-page:v1.0.0