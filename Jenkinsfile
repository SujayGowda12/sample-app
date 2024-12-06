pipeline {
    agent any
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
}

