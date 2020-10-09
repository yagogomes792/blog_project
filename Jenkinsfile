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
                bat 'docker-comnmpose up -d'
            }
        }
    }
}