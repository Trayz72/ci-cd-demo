pipeline {
    agent any

    environment {
        IMAGE_NAME = "trayz72/selenium-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        TEST_IMAGE = "selenium-test:${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Source') {
            steps {
                
                checkout scm
            }
        }

        stage('Build Test Image') {
            steps {
                echo "Building TEST stage to prepare for Selenium..."
                
                sh "docker build --target test -t $TEST_IMAGE ."
            }
        }

        stage('Run Selenium UI Tests') {
            steps {
                echo "Executing Selenium tests inside the container environment..."
                
                sh "docker run --rm $TEST_IMAGE pytest tests/"
            }
        }

        stage('Build Runtime Image') {
            steps {
                echo "Building optimized, lightweight production image..."
                
                sh "docker build --target runtime -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Docker Hub Auth & Push') {
            steps {
                
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                        docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest
                        docker push $IMAGE_NAME:latest
                    """
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
            sh 'docker system prune -f || true'
        }
        success {
            echo "✅ Pipeline Success: Image $IMAGE_NAME:$IMAGE_TAG is live on Docker Hub!"
        }
    }
}