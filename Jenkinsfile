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

}


}
