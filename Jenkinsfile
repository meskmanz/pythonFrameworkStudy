pipeline {
    agent {label 'docker_template1'}
    environment {
    PATH = "/home/jenkins/.local/bin:${env.PATH}"
  }
    stages {
        stage('Setup') {
            steps {
                script {
                    sh 'pip3 install -r requirements.txt --break-system-packages'
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --headless=True'
            }
        }
        post {
                always {
                    allure includeProperties:
                     false,
                     jdk: '',
                     results: [[path: 'build/allure-results']]
                }
            }
    }
}