pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
        IMAGE_NAME = 'sohail/flask-cicd-demo'
    }
    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sohail-24/flask-cicd-demo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }
        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                    }
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }
    }
}
