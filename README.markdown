# Random
This service provides a RESTful API which provides random functionality. It is written in Python using Flask.

The [Swagger Spec](static/swagger.yaml) defines the interface of the service.

## Running Locally
The service can be run as a Docker container or as a Python process.

### Docker Container
Run the latest [Docker image](https://hub.docker.com/r/maguirebrendan/random/tags):
```
docker run --pull always --publish 5000:5000 maguirebrendan/random:latest
```

### Python Process
Install requirements:
```
poetry install
```

Run:
```
poetry run python -m flask run
```

## Query
```
curl 'http://localhost:5000/random/default/choice?value=3&value=5&value=7'

{"value":"7"}
```

## Publishing the Docker Image
1. Publish a [new release](https://github.com/brendanmaguire/random/releases/new) on Github
1. Bump the tag used from the last release
1. The Docker image will be built and pushed as defined in [the Github workflow](https://github.com/brendanmaguire/random/blob/main/.github/workflows/build.yml)
