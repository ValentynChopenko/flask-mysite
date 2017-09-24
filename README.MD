INSTALL:
        if you want to download this application you have to write the following
        command in bash console and to be located in a folder that will used for
        creation an application folder:

            git clone https://github.com/ValentynChopenko/flask-mysite

        Now you have a clone of this application on your disk memory!
        Get in cloned application folder and save file "config_example.py" under name
        "config.py".

SETUP:
        Create a virtual evironment that will be appropriate just for this application
        For exaple, use the following command in bash console:

            virtualenv -p python3 path/to/virtualenv/envname

            or

            python3 -m venv path/to/virtualenv/envname

        And activate venv:

            source path/to/virtualenv/envname/bin/activate

        Get in an application folder and write the following command in console:

            pip install -r req_dev.txt

        Create a database for this application. It can be MySQL, PostgreSQL or SQLite.
        File "config.py" must be configurated using parameters of a created database.
        For example, a created databased is based on MySQL. In this case username,
        password and name of a database will be used for file "config.py" in line:

            SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

        If a created database is located locally it demands to use "@localhost/"
        instead of "@server/". Other cases you have to put host address instead of
        "@server/". As a relult of configuration SQLALCHEMY_DATABASE_URI will look
        like:

            SQLALCHEMY_DATABASE_URI = 'mysql://scott:tiger@localhost/mydatabase'

        There are examples of SQLALCHEMY_DATABASE_URI for PostgerSQL and SQLite:
        Postgres:

            'postgresql://username:password@server/db'

        SQLite (note the four leading slashes):

            'sqlite:////absolute/path/to/foo.db'

RUN:
        It seems everything is ready to run our application.
        Get in an application folder and write the following command in console:

            python3 run.py