pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                script {
                    sh 'docker build -t testapp .'
                    sh 'docker tag testapp $DOCKER_TESTAPP_IMAGE'
                }
            }
        }
        stage('Run Script') {
            steps {
                sh "docker exec container /bin/bash -c 'pytest --headless True'"
            }
        }
    }
    post {
        always {
            cleanWs()
            sh "docker stop container || true"
            sh "docker rm container || true"
        }
    }
}