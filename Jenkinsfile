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
				sh '''docker login --username=_ --password=3a16c88c-279b-4ee2-80e6-b7252d1a857f registry.heroku.com
				docker build -t registry.heroku.com/similar-movie/web .
				docker push registry.heroku.com/similar-movie/web
				heroku container:release web --app similar-movie
				'''

			}
		}

	}

}