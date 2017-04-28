#!/bin/bash
source "ENV.sh"
echo "$USER"
echo "$PASSWORD"
echo "$DATABASE"
mysql -u$USER -p$PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DATABASE"

