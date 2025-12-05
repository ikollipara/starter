SELECT 'CREATE DATABASE test_{{ cookiecutter.database_name }}'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'test_{{ cookiecutter.database_name }}')\gexec
