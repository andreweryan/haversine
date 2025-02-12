pipeline {
    agent any
    
    environment {
        VENV = 'dev'
    }
    
    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install pytest pytest-cov
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pytest --junitxml=test-results.xml --verbose
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}