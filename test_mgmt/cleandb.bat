del /s /q api\migrations

del /s /q siteconfig\migrations
del /s /q requirements\migrations
del /s /q workitems\migrations
del /s /q testdesign\migrations
del /s /q automation\migrations
del /s /q execution\migrations
del /s /q people\migrations
del /s /q data\db.sqlite3
migrate.bat
python manage.py createsuperuser
