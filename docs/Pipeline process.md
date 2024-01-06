## Pipeline Process Documentation:

#### Documentation of the pipeline:
    - Circleci is triggered once a new commit is pushed to Github and starts the pipeline process
    - Spin up the environment and setup environment variables
    - Deploy backend:
        - Deploy backend to EC2 using SSH
        - Spin Pytorch Docker image
        - Install Server Dependencies
        - Run Builds
        - Run deploy.sh
    - Set All backend environment variables
