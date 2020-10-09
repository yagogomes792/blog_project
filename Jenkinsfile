pipeline {
    agent any

    stages {
        stage('Build image'){
            steps{
                sh 'docker build -t myBlog -f Dockerfile .'
            }
        }
        stage('HomolEnv'){
            steps{
                sh 'docker-compose -f docker-compose.yml up'
            }
        }
    }
}