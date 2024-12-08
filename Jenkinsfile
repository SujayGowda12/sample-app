pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials-id'
        DOCKER_IMAGE = 'sujaygowda12/sample-app:latest'
    }
    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repositories') {
            steps {
                script {
                    git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/sample-app.git'
                    dir('ansible-sample-app') {
                        git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/ansible-playbook.git', branch: 'main'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }
        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: "${DOCKER_CREDENTIALS_ID}",
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                dir('ansible-sample-app') {
                    withCredentials([string(credentialsId: 'vault-password-id', variable: 'VAULT_PASSWORD')]) {
                        sh '''
                        ansible-playbook -i hosts install_apache.yml --vault-password-file <(echo $VAULT_PASSWORD)
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'docker rmi $DOCKER_IMAGE || true'
            }
        }
        success {
            echo 'Pipeline executed successfully.'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
    }
}

