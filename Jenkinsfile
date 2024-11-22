// pipeline {
//     agent any
//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Build stage.'
//             }
//         }
//
//         stage('Test') {
//             steps {
//                 echo 'Test stage.'
//                 sh 'bash -c "/opt/homebrew/bin/pytest test_mod.py --alluredir=allure-results"'
//
//             }
//         }
//     }
// }

pipeline {
    agent any
    stages {
        stage('Shell Test') {
            steps {
                echo 'Testing shell environment...'
                sh 'echo "Hello from shell"'
            }
        }
    }
}
