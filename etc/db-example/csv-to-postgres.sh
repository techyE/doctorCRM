#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

for file in "$SCRIPT_DIR"/*.csv; do
  sudo docker cp "$file" postgresql-1:/tmp/;
done;

echo "Using postgress username='user' password='123456789' for this example."
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_doctor FROM '/tmp/app_doctor.csv' DELIMITER ',' CSV HEADER;\""
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_patient FROM '/tmp/app_patient.csv' DELIMITER ',' CSV HEADER;\""
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_test FROM '/tmp/app_test.csv' DELIMITER ',' CSV HEADER;\""
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_trackingchart FROM '/tmp/app_trackingchart.csv' DELIMITER ',' CSV HEADER;\""

