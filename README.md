# Movie_recommender

## About

Often we try to look for movies similar to a movie that we liked. This web app gives you movie suggestions when you enter a movie name using content-based recommendation system. We use the movie database from Movielens (http://movielens.org/). 

-developed by Abhiramon, Aadhithya


## Usage instructions

To deploy the application locally, use the following instructions:
* Install docker. (Instructions for installation on Ubuntu can be found at https://docs.docker.com/install/linux/docker-ce/ubuntu/ )
* Pull the latest image using: sudo docker pull abhiramon/movie-recommender
* Run the container using: sudo docker run -p 5001:5001 abhiramon/movie-recommender

That's it! The app is now hosted locally on your browser at localhost:5001

## Project CI/CD setup

The project is set up with continuous integration and deployment (using Jenkins, Docker and Rundeck). We also monitor the app after it is deployed onto the server (using Elasticsearch-Logstash-Kibana stack). The pipeline is described in the diagram below:

![Alt text](images/Software_life_cycle.jpg?raw=true "Project pipeline")