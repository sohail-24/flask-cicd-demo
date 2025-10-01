#!/bin/bash
set -e

echo "Pulling latest image..."
docker pull sohail28/flask-cicd-demo:latest

echo "Stopping old containers..."
docker-compose down

echo "Starting new containers..."
docker-compose up -d

echo "Deployment complete!"

