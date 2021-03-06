#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Using postgress username='user' for this example."
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_doctor TO '/tmp/app_doctor.csv' DELIMITER ',' CSV HEADER;\""
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_patient TO '/tmp/app_patient.csv' DELIMITER ',' CSV HEADER;\""
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_test TO '/tmp/app_test.csv' DELIMITER ',' CSV HEADER;\""
sudo docker exec -it postgresql-1 bash -c "export PGPASSWORD='123456789'; psql -h 172.0.0.10 -p 5432 -U user -d doctorCRM -c \"\copy app_trackingchart TO '/tmp/app_trackingchart.csv' DELIMITER ',' CSV HEADER;\""

sudo docker cp postgresql-1:/tmp/app_doctor.csv "$SCRIPT_DIR"/app_doctor.csv;
sudo docker cp postgresql-1:/tmp/app_patient.csv "$SCRIPT_DIR"/app_patient.csv;
sudo docker cp postgresql-1:/tmp/app_test.csv "$SCRIPT_DIR"/app_test.csv;
sudo docker cp postgresql-1:/tmp/app_trackingchart.csv "$SCRIPT_DIR"/app_trackingchart.csv;