pipeline {
    agent any
    stages {
        stage('pull') {
            steps{
            git 'https://github.com/YoelEigner/WorldOfGames.git'
         }
        }
        stage('Build') {
            steps{
            echo 'Docker image build'
            bat 'docker build -f ./Dockerfile . -t ye8323/worldofgames:latest'
         }
        }
        stage('Run') {
            steps{
                echo 'Start docker container'
                bat 'docker compose up -d'
            }
        }
        stage('Test') {
            steps{
                echo 'Testing...'
                bat (script: 'python e2e.py')
            }
        }
        stage('Close and publish'){
            steps {
                echo 'Stop the container'
                bat 'docker compose down'
                bat 'docker push ye8323/worldofgames:latest'
            }
        }
        }
    }

