pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDS = credentials('dockerhub-credentials-id')
    }
    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/sample-app.git'
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                sh 'ansible-playbook -i hosts install_apache.yml'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_HUB_CREDS_USR}/sample-app:latest .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                sh 'echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push ${DOCKER_HUB_CREDS_USR}/sample-app:latest'
            }
        }
        stage('Deploy Application') {
            steps {
                sh './web-app.sh'
            }
        }
    }
    post {
        success {
            echo 'Build and deployment completed successfully.'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}

