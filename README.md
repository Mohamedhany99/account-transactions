Hello,
This is is "Mohamed Hany`s Basic Example of a small bank system"

how to run the application:

    1- you will need a csv file that hold 3 colums (id:uuid | name:string | balance:decimal)

    2- you will need to clone it and add .env file that contains two variable (SECRET_KEY:django secret key | DEBUG:boolean)

    3- create a virtualenv and acccess it in linux you can run (virtualenv venv then run source venv/bin/activate).

    4- run (pip install -r requirements.txt)

    5- run (python manage.py migrate)

    6- run (python manage.py runserver)

Notes:
    1- there is a json collection called (bank.postman_collection.json) in the repo that contains all the api documented and an example for each api to run it on Postman.

    2- the project is documented it`s api using Swagger docs you can access it using the link (localhost:8000/api/docs/)

    3- the project can configure with rest framework authentication using tokens for authentication but will need to modify the accounts model to make it inherit from abstractbaseuser class.

    4- the app database works on sqlite3.

