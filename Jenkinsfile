pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Build stage.'
            }
        }

        stage('Test') {
            steps {
                echo 'Test stage.'
                sh "/opt/homebrew/bin/pytest test_mod.py --alluredir=allure-results"
            }
        }
    }
}
