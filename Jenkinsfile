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
				sh '''docker login --username=_ --password=b11a33c7-77fc-461f-875b-5b79bcf72221 registry.heroku.com
				docker build -t registry.heroku.com/similar-movie/web .
				docker push registry.heroku.com/similar-movie/web
				heroku container:release web
				'''

			}
		}

	}

}