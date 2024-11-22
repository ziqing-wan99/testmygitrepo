pipeline {
    agent any

    environment {
        // Ensure PATH is correctly set
        PATH = "/opt/homebrew/bin:$PATH"
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
                // Correct command to run pytest
                sh '/opt/homebrew/bin/pytest test_mod.py --alluredir=allure-results'
            }
        }
    }
}
