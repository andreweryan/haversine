pipeline {
    agent {
        docker { image 'python:3' }
    }

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
                    ${VENV}/bin/python -m pytest --junitxml=$WORKSPACE/test-results.xml --verbose > pytest.log 2>&1 || true
                '''
                sh 'ls -l $WORKSPACE/test-results.xml || echo "test-results.xml not found!"'
            }
            post {
                always {
                    script {
                        if (fileExists("$WORKSPACE/test-results.xml")) {
                            echo "✅ test-results.xml found!"
                            junit "$WORKSPACE/test-results.xml"
                        } else {
                            echo "❌ test-results.xml not found! Check pytest.log for details."
                            sh 'cat pytest.log'
                        }
                    }
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
