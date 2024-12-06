pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-integration', url: 'https://github.com/SujayGowda12/sample-app.git'
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
    }
}

