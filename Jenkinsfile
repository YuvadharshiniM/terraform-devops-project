pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-portfolio"
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

        stage('Build & Deploy Docker') {
            steps {
                // Rebuild the image and restart the container
                sh 'docker build -t $DOCKER_IMAGE .'
                sh 'docker stop $DOCKER_IMAGE || true'
                sh 'docker rm $DOCKER_IMAGE || true'
                sh 'docker run -d --name $DOCKER_IMAGE -p 80:80 $DOCKER_IMAGE'
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
