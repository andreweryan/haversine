//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    
    environment {
        // Use Python virtual environment
        VENV = 'base'
    }
    
    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python -m unittest discover -s <test_folder_name> -p "test_*.py" --junitxml=test-results/junit.xml
                '''
            }
            post {
                always {
                    // Publish test results
                    junit 'test-results/junit.xml'
                }
                failure {
                    error 'Unit tests failed!'
                }
            }
        }
    }
    
    post {
        always {
            // Clean up virtual environment
            cleanWs()
        }
    }
}