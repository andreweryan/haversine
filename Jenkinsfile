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
                    ${VENV}/bin/pip install --upgrade pip
                    ${VENV}/bin/pip install pytest pytest-cov
                    ${VENV}/bin/pip install -r requirements.txt || true
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    ${VENV}/bin/python -m pytest --junitxml=test-results.xml --verbose > pytest.log 2>&1 || true
                '''
            }
            sh 'cat -A test-results.xml'
            post {
                always {
    
