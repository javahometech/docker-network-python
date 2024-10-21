# Running Python app and Mysql using a bridge network
## Create a bridge network
  ``` docker network create jhc ```
## Create MySQL container
```
docker run -d \
  --name mysql \
  --network jhc \
  -e MYSQL_ROOT_PASSWORD=javahomecloud \
  -e MYSQL_DATABASE=mydb \
  -e MYSQL_USER=appuser \
  -e MYSQL_PASSWORD=javahomecloud \
  -p 3306:3306 \
  mysql:latest
```
## Build docker image for python application
``` docker build -t myapp:0.1 . ```

## Run python application to talk to mysql db
```
docker run -d \
  --name myapp \
  --network jhc \
  -e MYSQL_HOST=mysql \
  -e MYSQL_PORT=3306 \
  -e MYSQL_USER=appuser \
  -e MYSQL_PASSWORD=javahomecloud \
  -e MYSQL_DATABASE=mydb \
  myapp:0.1

```
## Verify the output
```
docker logs myapp
```
## Expected output in the log is
```
Connected to MySQL database 'mydb' on host 'mysql:3306'
```
