export USERID=$(id -u)
export GROUPID=$(id -g)
export USERNAME=$(whoami)
export CONTAINERNAME='DYNAS_T'
printf "USERID=%s\n" $USERID 
printf "GROUPID=%s\n" $GROUPID 
printf "USERNAME=%s\n" $USERNAME 
xhost +
xhost +local:docker
echo $xhost
#docker-compose up -d --force-recreate --no-deps --build
docker-compose rm -f
docker rm -f $CONTAINERNAME
docker-compose -p $CONTAINERNAME up -d --build 
docker-compose exec echo $xhost
docker-compose exec /bin/bash
