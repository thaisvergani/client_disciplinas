# Client Disciplinas 📚

Implementa o consumo dos webservices em REST e SOAP:

* Curso
* Disciplina
* Area

Os web services estão no projeto https://github.com/gmilani/UniversidadeJava

## Setting Up the Environment

```
$ virtualenv venv --python=python3

$ . venv/bin/activate

$ git clone https://github.com/thaisvergani/client_disciplinas.git

$ cd proj_web/

$ pip install -r requirements_file.txt
```

## Running the application
```
$ python manage.py runserver
```

## Configuraçes

Para alterar o consumo dos web services entre SOAP/REST é preciso alterar o arquivo proj_web/client/settings.py na linha 12

### Consumir os Web Services REST:
```
WS = 'REST'
```
### Consumir os Web Services SOAP:

```
WS = 'SOAP'
```
