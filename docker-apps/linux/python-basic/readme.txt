# prepare to build image
cd <this directory that contains Dockerfile>

# build and store a local copy of image including a tag with my own name. The cdwuk refers to the Docker Hub image repository that we will push this to.
# -t refers to tag and the . (dot) tells Docker where to find the files to build (current directory)
docker image build -t cdwuk/python-basic:my-name-here .

# add 2 additional tags to the same image. Note that we include the version as part of the tag
docker build -t cdwuk/python-basic:v1.0.0 -t cdwuk/python-basic:latest .

# run the local image in a Linux VM hosted on laptop
docker container run --name python_basic --rm -i -t cdwuk/python-basic:my-name-here

# show all containers running or not
docker ps -a

## show logs for this container
docker logs -f python_basic 

docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" cdwuk/python-basic:v1.0.0

docker stop python_basic 

#login to DockerHub using password: Qwerty===1
docker login --username cdwuk

# push the image to docker hub
docker push cdwuk/python-basic:my-name-here