pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps{
                git branch: "master", url: "https://github.com/yagogomes792/blog_project.git"
            }
        }
        stage('Deploy Homol '){
            steps{
                bat 'docker-compose build'
                bat 'docker-compose up -d'
            }
        }
        stage('Functional test'){
           steps{
               dir('functional-test'){
                    git branch: "main", url: "https://github.com/yagogomes792/blog_tests.git"
                    bat 'py.test'
                }
            }
        }
    }
    post {
        always {
            junit 'tests/*.xml'
        }
    }
}