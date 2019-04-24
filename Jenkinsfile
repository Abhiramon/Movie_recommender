pipeline {

	agent any
		
	stages {

		stage('Build'){

			steps {

				sh '''virtualenv -p python3.6 pyenv
				source pyenv/bin/activate
				pip install -r requirements.txt
				pip install requests
				docker build -t abhiramon/movie-recommender .
				docker run -d -p 5001:5001 --name movie-recommender-container abhiramon/movie-recommender:latest
				'''
			}
		}

		stage('Test'){

			steps {
				sh '''source pyenv/bin/activate
				python run_tests.py'''

			}
		}

		stage('Deploy'){

			steps {
				sh '''
				docker stop movie-recommender-container
				docker rm movie-recommender-container
				docker push abhiramon/movie-recommender
				'''
				build "Rundeck_deploy"
			}
		}

	}

}