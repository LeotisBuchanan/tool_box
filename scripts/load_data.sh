#!/bin/bash
source "ENV.sh"
TABLENAME="RAW_DATA"
DATA_SQL_PATH=$1
echo "processing...."
mysql -u$USER -p$PASSWORD < $DATA_SQL_PATH
echo "done .....
