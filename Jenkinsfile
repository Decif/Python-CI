
pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Starting Python CI Pipeline'
                echo 'Source code is ready'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    python3 --version

                    python3 -m venv venv

                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Validation') {
            steps {
                sh '''
                    venv/bin/python scripts/validate.py

                    venv/bin/flake8 src tests
                '''
            }
        }

        stage('Testing') {
            steps {
                sh '''
                    venv/bin/python -m pytest -v \
                        --junitxml=reports/junit.xml \
                        --cov=src \
                        --cov-report=term-missing \
                        --cov-report=xml:reports/coverage.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/junit.xml'
            archiveArtifacts artifacts: 'reports/*.xml',
                             allowEmptyArchive: true
        }

        success {
            echo 'CI Pipeline completed successfully!'
        }

        failure {
            echo 'CI Pipeline FAILED!'
        }
    }
}
