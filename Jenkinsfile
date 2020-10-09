pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/yagogomes792/blog_project.git']]])
            }
        }
        stage('Build image'){
            steps{
                sh 'docker build -t myBlog .'
            }
        }
        stage('HomolEnv'){
            steps{
                sh 'docker-compose up'
            }
        }
    }
}