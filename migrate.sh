#!/bin/bash
export mode=production
export DATABASE__NAME=testmgmt
export DATABASE__USER=testmgmtadmin
export DATABASE__PASSWORD=testmgmtadmin@123
export DATABASE__HOST=localhost
export DATABASE__PORT=5432

cd test_mgmt
python manage.py makemigrations api
python manage.py makemigrations siteconfig
python manage.py makemigrations requirements
python manage.py makemigrations workitems
python manage.py makemigrations testdesign
python manage.py makemigrations automation
python manage.py makemigrations execution
python manage.py migrate
python manage.py shell -c "from create_super_user import create_super_user; create_super_user()"
cd ..

