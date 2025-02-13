pipeline {
    agent any
    triggers {
        pollSCM 'H/5 * * * *'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/andreweryan/haversine.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url:'https://github.com/andreweryan/haversine.git'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                which python3
                venv/bin/pip install pytest
                venv/bin/pip install .
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    venv/bin/python -m pytest --junit-xml test-reports/results.xml
                    venv/bin/haversine --coordinates 38.89220430021896 -77.05003345757281 38.892175669253966 -77.02004891843859 --unit kilometers
                '''
                }
                post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
