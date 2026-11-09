
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

                    venv/bin/python -m pip install --upgrade pip

                    venv/bin/python -m pip install -r requirements.txt
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
                    mkdir -p reports

                    venv/bin/python -m pytest \
                        tests/ \
                        --junitxml=reports/test-results.xml \
                        -v
                '''
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('reports')) {
                    junit(
                        testResults: 'reports/*.xml',
                        allowEmptyResults: true
                    )
                }
            }

            echo 'CI Pipeline finished'
        }

        success {
            echo 'CI Pipeline SUCCESS!'
        }

        failure {
            echo 'CI Pipeline FAILED!'
        }
    }
}
