pipeline {
    agent any

    environment {
        VENV = 'dev'
        PYTHON = '/usr/local/bin/python3'  // Update with your Python path
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate
                    ${PYTHON} -m pip install --upgrade pip
                    ${PYTHON} -m pip install pytest pytest-cov
                    ${PYTHON} -m pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    ${PYTHON} -m pytest --junitxml=$WORKSPACE/test-results.xml --verbose > pytest.log 2>&1 || true
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
