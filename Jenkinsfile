pipeline {

	agent any
		
	stages {

		stage('Build'){

			steps {

				sh '''virtualenv -p python3.6 pyenv
				source pyenv/bin/activate
				pip install -r requirements.txt
				'''

			}
		}

		stage('Test'){

			steps {
				sh '''source pyenv/bin/activate
				python test_get_recommendations.py'''

			}
		}

		stage('Deploy'){

			steps {
				sh '''docker build -t abhiramon/movie-recommender .
				docker push abhiramon/movie-recommender
				'''
				build "Rundeck_deploy"
			}
		}

	}

}