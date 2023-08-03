pipeline {
  agent any
  stages {
    stage('build') {
      steps{
      sh "cd project1"
      sh "sudo docker build -t localhost:8083/pythonapp ."
      sh "docker image ls"}
      
    }
    stage('push') {

    }
    stage('depoly') {

    }
  }
}
