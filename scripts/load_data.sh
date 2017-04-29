#!/bin/bash
source "ENV.sh"
TABLENAME="RAW_DATA"
DATA_SQL_PATH=$1
echo "$USER"
echo "$PASSWORD"
echo "$DATABASE"
echo "DATA_SQL_PATH"

mysql -u$USER -p$PASSWORD < $DATA_SQL_PATH

