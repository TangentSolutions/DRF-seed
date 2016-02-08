# DRF-seed
A seed project for create a Django Rest Framework-based API


# Getting started

## On a mac/linuxy system:

Download and run the startup script

```
wget https://raw.githubusercontent.com/TangentSolutions/DRF-seed/master/start.sh
sh ./start.sh {project_name}
```

Where `{project_name}` is the name of your project (e.g.: UserService, ProjectService, .. etc). 

.. This might take quite a while to run the first time .. so perhaps go grab yourself a coffee while you wait for this to finish.

Once this has run: 

```
cd {project_name}
docker-compose up
```

Check out your website on `docker-machine ip default`:8000. 

You might also be interested in: 

**Run python manage.py commands as per normal, you just prefix them with**

```
docker-compose run --rm web python manage.py ...
```

**Other things you can do:**

**Run the tests automatically**

```
docker-compose run --rm web sniffer
```

