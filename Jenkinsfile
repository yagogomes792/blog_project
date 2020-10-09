pipeline {
    agent any

    stages {
        stage('Checkout'){
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/yagogomes792/blog_project.git']]])
        }
        stage('Build image'){
            sh 'docker build -t myBlog .'
        }
        stage('HomolEnv'){
            sh 'docker-compose up'
        }
    }
}