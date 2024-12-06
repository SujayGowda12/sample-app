pipeline {
    agent any
    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir() // Clean workspace before each build
            }
        }
        stage('Clone Repositories') {
            steps {
                script {
                    // Clone the main application repository
                    git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/sample-app.git'

                    // Clone the Ansible playbook repository into ansible-sample-app directory
                    dir('ansible-sample-app') {
                        git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/ansible-playbook.git'
                    }
                }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                dir('ansible-sample-app') { // Navigate to the ansible-sample-app directory
                    withCredentials([string(credentialsId: 'vault-password-id', variable: 'VAULT_PASSWORD')]) {
                        sh '''
                        ansible-playbook -i hosts install_apache.yml --vault-password-file <(echo $VAULT_PASSWORD)
                        '''
                    }
                }
            }
        }
    }
}

