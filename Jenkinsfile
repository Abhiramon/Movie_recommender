pipeline {

	agent any
		
	stages {

		stage('Build'){

			steps {

				sh 'virtualenv -p pyhton3 pyenv'
				sh 'source pyenv/bin/activate'
				sh 'pip install -r requirements.txt'

			}
		}

		stage('Test'){

			steps {
				sh 'source pyenv/bin/activate'
				sh 'python test_get_recommendations.py'

			}
		}

		stage('Deploy'){

			steps {
				echo "Deploying"

			}
		}

	}

}