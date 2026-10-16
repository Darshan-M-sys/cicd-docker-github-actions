# CI/CD Pipeline with GitHub Actions and Docker

## Project Overview

This project demonstrates a Continuous Integration and Continuous Delivery (CI/CD) pipeline for a Python Flask application using GitHub Actions, Docker, and Docker Hub.

Whenever code is pushed to the `dev` branch, GitHub Actions automatically runs application tests. If the tests pass, the workflow builds a Docker image and publishes it to Docker Hub.

The published image can then be pulled and run locally using Docker Compose.

## Technologies Used

* Python
* Flask
* pytest
* Docker
* Docker Compose
* GitHub Actions
* Docker Hub
* Git and GitHub

## Architecture

```text
Developer
    |
    | Push code to dev
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    v
Run pytest tests
    |
    v
Build Docker Image
    |
    v
Publish Image to Docker Hub
    |
    v
Pull Image with Docker Compose
    |
    v
Run Flask Container
```

## Features

* Automated testing with pytest
* CI workflow triggered by pushes and pull requests targeting `dev`
* Docker image build after successful tests
* Automated Docker Hub publishing on pushes to `dev`
* Flask health-check endpoint
* Local container execution using Docker Compose
* Container restart policy

## Application Endpoints

| Endpoint  | Description                           |
| --------- | ------------------------------------- |
| `/`       | Returns a welcome message             |
| `/health` | Reports the application health status |

The application runs on port `5000`.

## Run Locally

### 1. Clone the repository

```bash
git clone `https://github.com/Darshan-M-sys/cicd-docker-github-actions`
cd cicd-docker-project
```

Replace `https://github.com/Darshan-M-sys/cicd-docker-github-actions/actions` with your actual repository URL.

### 2. Build and start the application

```bash
docker compose up -d --build
```

### 3. Verify the application

Open these endpoints in your browser:

* Homepage: `http://localhost:5000/`
* Health check: `http://localhost:5000/health`

### 4. View container status

```bash
docker compose ps
```

### 5. View application logs

```bash
docker compose logs web
```

### 6. Stop the application

```bash
docker compose down
```

## Run Automated Tests

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v
```

## CI/CD Workflow

The GitHub Actions workflow is defined in:

`.github/workflows/ci-cd.yml`

The workflow performs these steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs automated tests.
5. Builds the Docker image after successful tests.
6. Logs in to Docker Hub using GitHub Actions secrets.
7. Publishes the image to Docker Hub.

Pull requests targeting `dev` run the test job. The image publishing job runs only for pushes to `dev`.

## Docker Hub

**Docker Hub repository:** `darshantechinnovations2006/cicd-flask-app`

The published image can be pulled with:

```bash
docker pull darshantechinnovations2006/cicd-flask-app:latest
```

## GitHub Actions Secrets

Configure these repository secrets under **Settings → Secrets and variables → Actions**:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`

Never commit credentials or access tokens to the repository.

## Future Improvements

* Add automatic deployment after publishing the Docker image.
* Use unique image tags based on Git commit SHAs.
* Add code coverage reporting.
* Add container vulnerability scanning.
* Add a deployment environment with health checks.

## Learning Outcomes

This project demonstrates practical experience with automated testing, CI/CD workflow configuration, Docker image creation, container registries, secrets management, and container orchestration using Docker Compose.
