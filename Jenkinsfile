pipeline {
    agent any
    
    stages {
        stage('Checkout'){
            steps{
                git branch: "master", url: "https://github.com/yagogomes792/blog_project.git"
            }
        }
        stage('Build image'){
            steps{
                bat 'docker build -t myBlog -f Dockerfile .'
            }
        }
        stage('HomolEnv'){
            steps{
                bat 'docker-compose -f docker-compose.yml up'
            }
        }
    }
}