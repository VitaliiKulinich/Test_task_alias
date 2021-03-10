# Test_task_alias

### Task
[File](https://docs.google.com/document/d/1bUqYFWh7lak07flxZ9ACltwBmGlVTWeb41jMU7I-yZ8/edit?usp=sharing)

### Start

```
sudo docker-compose build .
sudo docker-compose run web python manage.py migrate
sudo docker-compose up
```

### Tests

```
sudo docker-compose build .
sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py test
```
