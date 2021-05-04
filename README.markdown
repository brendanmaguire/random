# Random
This service provides a RESTful API which provides random functionality. It is written in Python using Flask.

## Running Locally
The service can be run as a Docker container or as a Python process.

### Docker Container
```
docker run -p 5000:5000 maguirebrendan/random:0.0.1
```

### Python Process
Install libraries:
```
pip3 install -r requirements.txt
```

Run:
```
python3 -m flask run app.py
```

## Query
```
curl 'http://localhost:5000/random/333/choice?value=3&value=5&value=7'

{"value":"7"}
```

## Publishing the Docker Image
```
docker build -t maguirebrendan/random:0.0.1 .
docker push maguirebrendan/random:0.0.1
```
