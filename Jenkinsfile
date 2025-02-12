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
                    pip install xmlrunner
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                // Ensure clean test results directory
                sh 'rm -rf test-results && mkdir -p test-results'
                
                // Create Python test runner script
                writeFile file: 'run_tests.py', text: '''
import unittest
import xmlrunner
import sys

# Discover and run tests
loader = unittest.TestLoader()
suite = loader.discover('tests')

runner = xmlrunner.XMLTestRunner(output='test-results')
result = runner.run(suite)

# Exit with error code if tests failed
sys.exit(not result.wasSuccessful())
'''
                
                // Run the tests
                sh '''#!/bin/bash
                    source ${VENV}/bin/activate
                    python run_tests.py
                '''
            }
            post {
                always {
                    // Publish test results
                    junit(
                        testResults: 'test-results/*.xml',
                        allowEmptyResults: true,
                        keepLongStdio: true
                    )
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