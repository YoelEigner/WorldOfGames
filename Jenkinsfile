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
                sh 'sudo docker build -f ./Dockerfile .'

            }
        }

                //run a container and test the application
        stage("run a container"){
            steps{
                sh 'sudo docker-compose up --detach'
            }

        }

        //run test
        stage("e2e test"){
            steps{
                sh 'docker exec worldofgames_world_of_games bash -c \"python e2e.py\"'
            }

        }

         // stop the container
        stage("finalize"){
            steps{

                sh "sudo docker stop worldofgames_world_of_games"
            }


        }
    }
}
