#https://stackoverflow.com/questions/46032392/docker-compose-does-not-allow-to-use-local-images

docker-compose down
docker build -t crawler .
docker tag crawler:latest crawler:staging
docker-compose up


#remember to setting config in docker-compose.yml
#set namp_server's -> image: crawler:staging

