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
                sh 'ls'
                sh 'tail -c +1 test-results.xml > test-results_clean.xml && mv test-results_clean.xml test-results.xml'
                sh 'cat -A test-results.xml'  // Debugging step to check for hidden characters
            }
            // post {
            //     always {
            //         script {
            //             if (fileExists('test-results.xml')) {
            //                 junit 'test-results.xml'
            //             } else {
            //                 echo "Warning: test-results.xml not found! Check pytest.log for details."
            //                 sh 'cat pytest.log'
            //             }
            //         }
            //     }
            // }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
