#!/bin/bash
source "ENV.sh"
TABLENAME="RAW_DATA"
echo "processing...."
mysql -u$USER -p$PASSWORD -e "USE $DATABASE; CREATE TABLE IF NOT EXISTS $TABLENAME ( 
           id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
           pickup_date_time datetime,
           lat LONG,
           lon LONG,
           base TEXT
);"
echo "done ......

