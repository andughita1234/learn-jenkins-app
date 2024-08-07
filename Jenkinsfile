pipeline {
    agent any

    stages {
        stage('Setup') {
            agent {
                docker {
                    image 'python:3.10-slim'
                    reuseNode true
                }
            }
            steps {
                // Set up Python environment
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m venv venv
                    virtualenv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            agent {
                docker {
                    image 'python:3.10-slim'
                    reuseNode true
                }
            }
            steps {
                // Run Pylint to check code quality
                sh '''
                    . venv/bin/activate
                    pylint test_sample.py
                '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'selenium/standalone-chrome'
                    reuseNode true
                }
            }
            steps {
                // Run pytest to execute Selenium tests
                sh '''
                    . venv/bin/activate
                    pytest test_sample.py --headless --browser chrome --html=report.html --self-contained-html
                '''
            }
            post {
                always {
                    // Archive the test report as a build artifact
                    archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
                    // Publish the HTML report in Jenkins
                    publishHTML(target: [
                        reportName: 'Test Report',
                        reportDir: '.',
                        reportFiles: 'report.html',
                        alwaysLinkToLastBuild: true,
                        keepAll: true
                    ])
                }
            }
        }

        stage('Deploy') {
            steps {
                // Placeholder for deployment logic
                sh '''
                    echo "Deploying to production"
                '''
            }
        }
    }

    post {
        always {
            cleanWs() // Clean up the workspace after the build
        }
    }
}
