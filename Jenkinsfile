node ('Docker') {

    stages {
        stage('Checkout'){
            steps{
                git branch: "master", url: "https://github.com/yagogomes792/blog_project.git"
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