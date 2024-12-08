pipeline {
    agent any

    environment {
        VAULT_PASSWORD = credentials('vault-password-id')
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
                git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/sample-app.git', branch: 'master'
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                withCredentials([string(credentialsId: 'vault-password-id', variable: 'VAULT_PASSWORD')]) {
                    sh '''
                    ansible-playbook -i hosts install_apache.yml --vault-password-file <(echo $VAULT_PASSWORD)
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t sujaygowda12/sample-app:latest .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh '''
                echo $DOCKER_HUB_CREDS_PSW | docker login -u $DOCKER_HUB_CREDS_USR --password-stdin
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push sujaygowda12/sample-app:latest
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker rm -f sample-app || true
                docker run -d -p 5000:5000 --name sample-app sujaygowda12/sample-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'Build, deployment, and tests completed successfully!'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}

