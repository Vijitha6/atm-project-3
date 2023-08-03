pipeline {
    agent any
    stages {

        stage("checking") {
            steps {
                script {
                    echo "checking"
                }
            }
        }
        stage("build image") {
            steps {
                script {
                    echo "building image"
                    echo "building the docker image..."
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh 'docker build -t atm:1.0 .'
                    sh 'docker tag atm:1.0 bogevijitha/atm-project:1.0'
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh 'docker push bogevijitha/atm-project:1.0'
    }
                }
            }
        }
        stage("deploy") {
            steps {
                script {
                    echo "deploying to ec2 ....."
                }
            }
        }
    }   
}
