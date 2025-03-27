pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
        VENV_DIR = 'venv'
        TEST_REPORT_DIR = 'reports'
    }

    stages {
        stage('Checkout Code') {
            steps {
//                 git branch: 'master', url: 'https://github.com/vikaskaushik3/jenkins_integration_with_selenium_api_framework.git'
                    checkout scmGit(
                        branches: [[name: '*/master']],
                                    extensions: [],
                                    userRemoteConfigs: [[url: 'https://github.com/vikaskaushik3/jenkins_integration_with_selenium_api_framework.git'
                                    ]]
                        )
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run UI Tests (Selenium)') {
            steps {
                sh '''
                    mkdir -p $TEST_REPORT_DIR
                    source $VENV_DIR/bin/activate
                    pytest tests/ui_tests --html=$TEST_REPORT_DIR/ui_report.html --self-contained-html
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    mkdir -p $TEST_REPORT_DIR
                    source $VENV_DIR/bin/activate
                    pytest tests/api_tests --html=$TEST_REPORT_DIR/api_report.html --self-contained-html
                '''
            }
        }

        stage('Publish Reports') {
            steps {
                publishHTML(target: [
                    reportDir: "${TEST_REPORT_DIR}",
                    reportFiles: 'ui_report.html,api_report.html',
                    reportName: 'Test Reports'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: "${TEST_REPORT_DIR}/*.html", fingerprint: true
        }
        failure {
            mail to: 'vikaskaushik166@gmail.com',
                 subject: "Jenkins Build Failed: ${env.JOB_NAME}",
                 body: "Check the build logs and reports for details."
        }
    }
}
