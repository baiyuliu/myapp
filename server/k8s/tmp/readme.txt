
docker run -d -p 5000:5000 --name registry registry:2

docker build -t server-web:latest -f web.Dockerfile .
docker tag server-web:latest baiyuliu/server-web:latest
docker push baiyuliu/server-web:latest

docker build -t mysql-service:latest -f database.Dockerfile .
docker tag mysql-service:latest baiyuliu/mysql-service:latest
docker push baiyuliu/mysql-service:latest

echo "password" > password.txt

kubectl create secret generic mysql-credentials --from-file=password.txt
kubectl get secrets mysql-credentials


docker run -d -p 3000:3000 -v /mnt/share/server/swagger_server:/usr/src/app/swagger_server -e MYSQL_HOST="database-service" -e MYSQL_USER=username -e MYSQL_PASSWORD=password --name web  server-web:latest


pyenv install 3.9.6
pyenv local 3.9.6
pyenv virtualenv 3.9.6 myenv
pyenv activate myenv 
pip install -r test-requirements.txt
pip install -r requirements.txt
