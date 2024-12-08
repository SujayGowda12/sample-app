pipeline {
    agent any
    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir() // Clears the workspace to ensure no leftover files interfere.
            }
        }

        stage('Clone Repositories') {
            steps {
                script {
                    // Clone the application repository
                    git credentialsId: 'github-integration', 
                        url: 'https://github.com/SujayGowda12/sample-app.git'

                    // Clone the Ansible playbook repository
                    dir('ansible-sample-app') {
                        git credentialsId: 'github-integration', 
                            url: 'https://github.com/SujayGowda12/ansible-playbook.git', 
                            branch: 'main'
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    def image = docker.build('sujaygowda12/sample-app:latest')
                    withDockerRegistry(credentialsId: 'docker-hub-creds', url: 'https://index.docker.io/v1/') {
                        image.push()
                    }
                }
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                dir('ansible-sample-app') {
                    withCredentials([string(credentialsId: 'vault-password-id', variable: 'VAULT_PASSWORD')]) {
                        sh '''
                        ansible-playbook -i hosts install_apache.yml \
                        --vault-password-file <(echo $VAULT_PASSWORD)
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            echo "Pipeline execution completed."
            cleanWs() // Cleans up the workspace after execution
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}

