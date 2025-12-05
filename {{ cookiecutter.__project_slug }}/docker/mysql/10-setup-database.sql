CREATE DATABASE IF NOT EXISTS test_{{ cookiecutter.database_name }};
GRANT ALL PRIVILEGES ON test_{{ cookiecutter.database_name }}.* TO {{ cookiecutter.__database_user }};
FLUSH PRIVILEGES;
