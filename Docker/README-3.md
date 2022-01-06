
# Docker

Q1. Compare different kinds of docker image families. Alpine, Slim, Stretch, Buster, Jessie, Bullseye. What does this mean? How are they different? What advantage do they provide over the others?
```
* stretch/buster/jessie/Bullseye - We use these if our code uses Debian operating system.
* Alpine - It is used where there are space concerns as Alpine has small size. It uses linux. It is considered to be more secure and fast.

```

Q2. Difference between Entrypoint and CMD directive in a Dockerfile?
```
CMD - Used for runing commands in a container. e.g run script abc
Entrypoint - Command that runs when a container starts.
RUN -  Used for creating new layers in images. e.g Install python
```

Q3. Explain this command written inside a Dockerfile:RUN mkdir /app/django/helloworld
```
Make a directory named helloworld, insie django which is inside app which is inside the current working directory.

```

Q4. Explain the concept of layering in Docker images/containers?
```
Images are made up of layers. Each set of instruction makes up a layer in the image.
The first time we build our image, layers of the image gets constructed on top of each other. When we build the image a second time, docker uses cache to get the layers if no files have been changed. 
If layer 4 has been changed, everything above will be re-evaluated. The top most layer is the writeable layer.
```