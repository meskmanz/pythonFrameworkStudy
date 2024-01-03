pipeline {
    agent {label 'docker_template1'}
    environment {
    PATH = "/home/jenkins/.local/bin:${env.PATH}"
  }
    stages {
        stage('Git Checkout') {
            steps {
                script {
                    git branch: 'master',
                        url: 'https://github.com/meskmanz/pythonFrameworkStudy.git'
                }
            }
        }
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
    }
}