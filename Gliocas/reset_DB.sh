#!/bin/bash

rm db.sqlite3
for migration in gliocas_app/migrations/*.py
do
    if [ -e "$migration" ]; then
        if [[ "$migration" != *__init__.py* ]]; then
            rm "$migration"
        fi 
    fi 
done

python3 manage.py makemigrations
python3 manage.py migrate
python3 populate.py

exit 0