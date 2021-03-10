# Test task Alias

### Task
[File](https://docs.google.com/document/d/1bUqYFWh7lak07flxZ9ACltwBmGlVTWeb41jMU7I-yZ8/edit?usp=sharing)

### Start

```
sudo docker-compose build
sudo docker-compose run web python manage.py migrate
sudo docker-compose up
```

### Tests
Use this command after first two in block Start
```
sudo docker-compose run web python manage.py test
```
The program was formatted with black.
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
