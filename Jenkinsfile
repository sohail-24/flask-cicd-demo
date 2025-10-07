@Library('my-shared-lib') _

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                buildDocker('sohail28/flask-cicd-demo:latest')
            }
        }
        stage('Test') {
            steps {
                testApp()
            }
        }
        stage('Deploy') {
            steps {
                deployApp()
            }
        }
    }
}
