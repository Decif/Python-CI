
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
                    echo "Checking Python version"
                    python3 --version

                    echo "Removing previous virtual environment"
                    rm -rf venv

                    echo "Creating clean virtual environment"
                    python3 -m venv venv

                    echo "Initializing pip"
                    venv/bin/python -m ensurepip --upgrade

                    echo "Installing dependencies"
                    venv/bin/python -m pip install --no-cache-dir -r requirements.txt

                    echo "Setup completed successfully"
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

                    echo "Running tests with code coverage"

                    venv/bin/python -m pytest tests/ \
                        -v \
                        --junitxml=reports/test-results.xml \
                        --cov=src \
                        --cov-report=term-missing \
                        --cov-report=xml:reports/coverage.xml \
                        --cov-report=html:reports/coverage-html \
                        --cov-fail-under=80
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

                    archiveArtifacts(
                        artifacts: 'reports/**',
                        allowEmptyArchive: true
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
