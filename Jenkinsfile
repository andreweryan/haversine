pipeline {
    agent any
    
       environment {
        PATH = "/Users/andrewryan/venvs/dev/bin/python3.exe;$PATH"
        }
    
    stages {   
        stage('Run Tests') {
            steps {
                sh '''
                    $python -m pytest --junitxml=test-results.xml --verbose || true
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
