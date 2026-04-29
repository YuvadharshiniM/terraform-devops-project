pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-portfolio"
        DOCKER_HUB_USER = "yuvadharshinim"
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        DOCKER_HUB_CREDS = credentials('docker-hub-creds')
    }

    stages {
        stage('Checkout') {
            steps {
                // This pulls your code from GitHub
                checkout scm
            }
        }

        stage('Terraform Init & Plan') {
            steps {
                sh 'terraform init'
                sh 'terraform plan'
            }
        }

        stage('Terraform Apply') {
            steps {
                // This ensures your server is always up-to-date
                sh 'terraform apply -auto-approve'
            }
        }

        stage('Build & Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DUSER', passwordVariable: 'DPASS')]) {
                    sh "echo '$DPASS' | docker login -u '$DUSER' --password-stdin"
                    sh "docker build -t $DUSER/$DOCKER_IMAGE:latest ."
                    sh "docker push $DUSER/$DOCKER_IMAGE:latest"
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                sh 'docker stop $DOCKER_IMAGE || true'
                sh 'docker rm $DOCKER_IMAGE || true'
                sh 'docker run -d --name $DOCKER_IMAGE -p 80:80 $DOCKER_HUB_USER/$DOCKER_IMAGE:latest'
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful!"
        }
        failure {
            echo "❌ Deployment Failed. Check Logs."
        }
    }
}
