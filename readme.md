# Identifying-Egyptian-Artifacts-Landmarks-API



### Project Idea
An API utilizing Siamese Network Architecture (SNN) with Knowledge Transfer (KT) to identify Egyptian monuments/Landmarks and provide relevant information. The API aims to enhance tourists' experience by providing historical context and relevant information about the rich cultural heritage of Egypt.
<br>


<!-- #### [Frontend Application Link](https://university-schedule-generator.vercel.app) -->


> Note: API may stop working after AWS free tier ends for my account


> #### GET All Classes [GET]: https://identifying-egyptian-artifacts-landmarks.publicvm.com/classes/
> #### Prediction Endpoint [POST]: https://identifying-egyptian-artifacts-landmarks.publicvm.com/predict/ 
> #### GET Specific Classe using class id: [GET]: https://identifying-egyptian-artifacts-landmarks.publicvm.com/classes/:id/
> #### Search Using Class Name [GET]: https://identifying-egyptian-artifacts-landmarks.publicvm.com/classes/?q='search_keyword_without_quotes'
> #### Dataset: https://www.kaggle.com/datasets/hossamhamza/egyptian-monuments-and-landmarks/data
<br>

### Main objectives
    - Robust AI-powered image classification API capable of accurately classifying Egyptian artifacts and landmarks.
    - List classes availabe in the database with relevant information



### Technologies used in this project:
    - AWS (EC2)
    - Circleci
    - Docker
    - Python
    - Pytorch 
    - Flask
    - PostgreSQL


### To be added:
    - Unit Testing
    - Linting/Prettier module



<br>

> Note: No sensitive data are hardcoded in the code, instead it is passed through the environment variables in both amazon EC2 and CircleCI

<br>

#### Database schemas ERD 
[![architecture diagram](https://raw.githubusercontent.com/hossamhamzahm/identifying-egyptian-artifacts-landmarks-api/main/docs/db_schema.png)]()



#### Documentation of all dependencies is found in the [App dependencies.md](https://github.com/hossamhamzahm/identifying-egyptian-artifacts-landmarks-api/blob/main/docs/App%20dependencies.md) file in the docs directory


#### A screenshot of the last build is found the [docs directory](https://github.com/hossamhamzahm/identifying-egyptian-artifacts-landmarks-api/blob/main/docs) in the Github repository 


#### Documentation of the pipeline is found in the [Pipeline process.md](https://github.com/hossamhamzahm/identifying-egyptian-artifacts-landmarks-api/blob/main/docs/Pipeline%20process.md) file in the docs directory


> Click on the status icon to view the pipeline
[![Status Badge](https://circleci.com/gh/hossamhamzahm/fwd-circleci-training.svg?style=svg)](https://app.circleci.com/pipelines/github/hossamhamzahm/University_Schedule_Generator/19/workflows/b108f94f-fdc1-4481-8fba-52e3439ce6ea/jobs/13)


#### Architecture diagram for an overview of the infrastructure and the pipeline
[![architecture diagram](https://raw.githubusercontent.com/hossamhamzahm/identifying-egyptian-artifacts-landmarks-api/main/docs/architecture_diagram.png)]() 