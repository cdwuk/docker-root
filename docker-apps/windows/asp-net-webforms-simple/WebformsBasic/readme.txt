
# change Docker to run a windows VM 

# create the local image
docker image build -t cdwuk/webforms:my-name-here .

# run the local image
docker run -it --rm  --name webforms -p 80:80 cdwuk/webforms:my-name-here

docker ps


#login to docker hub
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/webforms:my-name-here