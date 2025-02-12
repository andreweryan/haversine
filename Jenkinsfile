//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    environment {
        PATH = "/Users/andrewryan/venvs/dev/bin/python3.exe;$PATH"
        }
    stages {
        stage('Build') { 
            steps {
                echo 'Starting the build Stage'
                echo 'Build Stage completed successfully'
            }
        }
        stage('Test') { 
            steps {
                echo 'Starting the Test Stage'
                sh 'python -m unittest tests/test_haversine.py'
                echo 'Test Stage completed successfully'
            }
        }
        stage('Deploy') { 
            steps {
                echo 'Starting the Deploy Stage'
                echo 'Deploy Stage completed successfully'
            }
        }
    }
}