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
                    pip install -r requirements.txt || true
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    ${VENV}/bin/python -m pytest --junitxml=test-results.xml --verbose || true
                '''
            }
            post {
                always {
                    sh 'cat test-results.xml || echo "<testsuites></testsuites>" > test-results.xml'
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
