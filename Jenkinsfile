pipeline {
    agent any
    triggers {
        pollSCM '* * * * *'
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
            }
        }
        stage('Test') {
            steps {
                sh '/venv/bin/python3 -m pytest'
            }
        }
    }
}
