//Jenkinsfile (Declarative Pipeline)

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
                echo "build a container"
                bat "docker-compose build"

            }
        }
        
        //run a container and test the application
        stage("run a container"){
            steps{
                echo "run a container"
               
                bat 'docker-compose up --detach'
            }
            
        }
        
        //run test
        stage("e2e test"){
            steps{
                //sleep 30 // seconds
                echo "e2e test"
                sh 'docker exec worldofgames_world_of_games_1 bash -c \"python e2e.py\"'
            }

        }
                
         // stop the container
        stage("finalize"){
            steps{
                echo "drop the container"
                
                bat "docker stop worldofgames_world_of_games"
            }
            
            
        }

    }
}
