//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
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
                sh 'which python3'
                // sh 'python -m unittest tests/test_haversine.py'
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