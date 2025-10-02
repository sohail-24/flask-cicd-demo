pipeline {

 agent any
 stages {
  stage ("Clone the code") {
   steps {
    git url: "https://github.com/sohail-24/flask-cicd-demp.git", branch: "main"


}
}
   stage ("Build") {
    steps {
     sh "docker build -t sohail28/flask-cicd-demo:latest ."


}
}
   stage ("Push the code") {
    steps {
     withCredentials([usernamePassword( credentialsId: "dockerhub-creds", usernameVariable: "DOCKER_USER", passwordVariable: "DOCKER_PASS")]) {
      sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
      sh "docker push sohail28/flask-cicd-demo:latest"

}

}

}

  stage ("Deploy") {
   steps {
    sshagent (credentials: ['vm-ssh-key']) {
     sh """
     ssh -o StrictHostKeyChecking=no sohail@192.168.97.139 'cd ~/flask-mysql-nginx && ./deploy.sh'
     """
}
}

}



}


}
