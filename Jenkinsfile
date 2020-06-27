pipeline{
    agent any
    
    stages
    {
        //get a repository from a github
        stage("checkout a repo"){
            steps{
                echo "checkout a repo"
                git 'https://github.com/YoelEigner/WorldOfGames'
           }
        }
       
       //build an image from the dockerfile
        stage("build a container"){
            steps{
                app = docker.build -f ./Dockerfile .

            }
        }
    }
}
