# Client Disciplinas

Implementa o consumo dos webservices em REST e SOAP:
* Curso
* Disciplina
* Area

Running the Project Locally
First, clone the repository to your local machine:

git clone https://github.com/sibtc/restful-apis-example.git
Install the requirements:

pip install -r requirements.txt
PS: If you have issues installing either gunicorn or psycopg2, you can remove them from the requirements.txt file and run the command again.

Create the database:

python manage.py migrate
Finally, run the development server:

python manage.py runserver
The project will be available at 127.0.0.1:8000.
