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