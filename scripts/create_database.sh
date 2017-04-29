#!/bin/bash
source "ENV.sh"
echo "processing..."
mysql -u$USER -p$PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DATABASE"
echo "done......"
