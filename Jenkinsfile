pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            environment {
                AWS_REGION = 'eu-west-2' // Replace with your desired AWS region
                ECR_REPOSITORY = 'project3'
                ECS_CLUSTER = 'PythonAppCluster'
                ECS_SERVICE = 'PythonApp'
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'qalearner', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                        // Authenticate with ECR
                        sh "aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPOSITORY"

                        // Build Docker image
                        sh "docker build -t $ECR_REPOSITORY:latest ."

                        // Push Docker image to ECR
                        sh "docker push $ECR_REPOSITORY:latest"
                    }
                }
            }
        }
        stage('Deploy to ECS') {
            environment {
                AWS_REGION = 'eu-west-2' // Replace with your desired AWS region
                ECS_CLUSTER = 'PythonAppCluster'
                ECS_SERVICE = 'PythonApp'
            }
            steps {
                script {
                    // Update ECS service with the new image
                    sh "aws ecs update-service --cluster $ECS_CLUSTER --service $ECS_SERVICE --force-new-deployment"
                }
            }
        }
        stage('Run Docker Container') {
            environment {
                RDS_ENDPOINT = 'project3db.cnoalucxc1ah.eu-west-2.rds.amazonaws.com'
            }
            steps {
                script {
                    // Run the Docker container after ECS deployment
                    sh "sudo docker run -d -p 5000:5000 -e SQL_HOST=$RDS_ENDPOINT --name pythonapp $ECR_REPOSITORY:latest"
                }
            }
        }
    }
}
