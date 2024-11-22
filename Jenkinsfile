pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:$PATH"  // Ensure the correct path for binaries like pytest
    }

    stages {
        stage('Build') {
            steps {
                echo 'Build stage.'
            }
        }

        stage('Test') {
            steps {
                echo 'Test stage.'
                sh '/opt/homebrew/bin/pytest test_mod.py --alluredir=allure-results'
            }
        }
    }
}