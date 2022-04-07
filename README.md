# CICD-with-ECR

## Assignment tasks:
### Stage 1: Dockerization

- Dockerize a simple Hello World Flask Application which responds with a message that is set up as an environment variable and deploy the docker image to AWS ECR.
Dockerfile is created with ports exposed and configured to install dependencies immediately. Also runs the flask app. A workflow is set up to push the image automatically to AWS ECR

[Dockerfile](https://github.com/utkarsh348/CICD-with-ECR/blob/main/Dockerfile)
### Stage 2: CI/CD Pipeline

- Develop a CI/CD pipeline(Github Actions/Jenkins or your own choice) which would lint the python code and push the updated image to ECR.
The workflow to lint the python code is set up which does not approve changes unless the score is a 10/10. The workflow created in the previous step enables the push of the updated image to the ECR repo

[AWS workflow](https://github.com/utkarsh348/CICD-with-ECR/blob/main/.github/workflows/aws.yml)

[Linting workflow](https://github.com/utkarsh348/CICD-with-ECR/blob/main/.github/workflows/pylint.yml)
### Stage 3: Deployment to ECS

- Setup a workflow which would deploy the given ECR image to ECS on EC2 instance or Fargate.
The given workflow will also deploy the ECR image to ECS, once the secrets for the ECS instance are configured in GitHub action secrets and the instance details are provided. 

### Bonus

- ECS could be configured for autoscaling and/or load-balancing.
- CI pipeline could check the code quality or are there any secrets in the code.

CI pipeline for linting will check the code quality
A seperate workflow has been set up in GitHub actions to check for secrets in the python files that are pushed to the main branch. Both, the pylint and secrets workflows work with python versions >=3.8. Secrets are checked for using a regex. 

[secrets-workflow](https://github.com/utkarsh348/CICD-with-ECR/blob/main/.github/workflows/pysecret.yml)
