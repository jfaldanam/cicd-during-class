# mlops-cicd-ml

A minimal CI/CD pipeline for machine learning: train a model, store it as an artifact, and ship it as a Docker image — all automated with GitHub Actions.

This repo is part of the contents of the MLOps module of the second edition of the Master's in Big Data, Artificial Intelligence, and Data Engineering at the University of Málaga.

## Pipeline

| Step | Workflow | What it does |
|------|----------|--------------|
| Train | `train.yml` | Trains a RandomForest on Iris, saves `model.pkl` as a pipeline artifact |
| Build | `build.yml` | Downloads the artifact, builds a Docker image, pushes it to GHCR |

## Run inference locally

```bash
docker pull ghcr.io/jfaldanam/mlops-cicd-ml:latest

docker run --rm ghcr.io/jfaldanam/mlops-cicd-ml:latest predict --features 5.1 3.5 1.4 0.2
```
