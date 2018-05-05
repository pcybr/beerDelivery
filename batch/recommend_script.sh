docker exec -it spark-master sh -c "cd /app && ./install.sh"
docker exec -it spark-worker sh -c "cd /app && ./install.sh"

sleep 30


while sleep 120; do docker exec -it spark-master bin/spark-submit --master spark://spark-master:7077 --total-executor-cores 2 --executor-memory 512m /app/hello.py; done
