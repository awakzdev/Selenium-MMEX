pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('Build & Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test-Population Sheet) {
            steps {
                sh 'python ./mmex-population.py'
            }
        }
    }
}