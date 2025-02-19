# bittext

Bittext is an object-storage-based text sharing application.
Creating a bittext stores its content into an S3-compatible object-storage backend, attributing it a unique hash that is also used as its URI.

In a future release, we'll add a cron for Bittexts to be automatically deleted after one week.

## Running locally

At the moment the app is a simple Flask application. You can install dependencies, populate secrets and be good to go

```bash

# Install deps
$ pip install -r requirements.txt

# Copy .env.dist and populate values with your secrets
$ cp .env.dist .env

# Run the app using Flask development server
$ flask --app=bittext run
```

## Packaging for production

Bittext was created to demo an application deployment for Kubernetes.
The application comes with a ready-to-run uwsgi setup. You'll be able to expose it behind a reverse proxy as-is.

To build the docker image, use
```bash

$ docker build -t bittext:latest ./
```

*The default uWSGI configuration for this application listens on port 5000*
