pipeline {
    agent any

    environment {
        IMAGE_NAME = "sohail28/flask-cicd-demo"
        CONTAINER_NAME = "flask-app"
        DEPLOY_SERVER = "sohail@192.168.97.139"
    }

    stages {

        stage('Clone the Code') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/sohail-24/flask-cicd-demo.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy on Server') {
            steps {
                sshagent (credentials: ['vm-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no $DEPLOY_SERVER "
                            docker pull $IMAGE_NAME:latest &&
                            docker rm -f $CONTAINER_NAME || true &&
                            docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME:latest
                        "
                    '''
                }
            }
        }
    }
}

