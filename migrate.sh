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
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')"
cd ..

