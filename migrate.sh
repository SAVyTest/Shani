#!/bin/bash
export mode=production
export DATABASE__NAME=testmgmt
export DATABASE__USER=testmgmtadmin
export DATABASE__PASSWORD=testmgmtadmin@123
export DATABASE__HOST=localhost
export DATABASE__PORT=5432

cd test_mgmt
python3 manage.py makemigrations api
python3 manage.py makemigrations automation
python3 manage.py makemigrations siteconfig
python3 manage.py migrate
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')"l̥
cd ..

