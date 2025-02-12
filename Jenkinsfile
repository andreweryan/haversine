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
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'which python3'
                sh 'pip install --upgrade pip'
                sh 'pip install pytest'
                sh 'pip install .'
                sh 'python3 -m pytest'
                sh 'haversine --coordinates 38.89220430021896 -77.05003345757281 38.892175669253966 -77.02004891843859 --unit kilometers'
            }
        }
    }
}
