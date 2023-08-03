pipeline {
  agent any
  environment {
    NEXUS_LOGIN = credentials('NEXUS_LOGIN')
  }
  stages {
    stage('build') {
      steps {
        sh "sudo docker build -t localhost:8083/pythonapp ."
      }
    }
    stage('push') {
      steps {
        sh "sudo docker login localhost:8083 -u ${NEXUS_LOGIN_USR} -p ${NEXUS_LOGIN_PSW}"
      }
    }
    stage('deploy') {
      steps {
        sh "sudo docker stop pythonapp"
        sh "sudo dorcker rm pythonapp"
        sh "sudo docker run -d -p 5000:5000 -e SQL_HOST=mysql:3306 --name pythonapp localhost:8083/pythonapp"
      }
    }
  }
}
