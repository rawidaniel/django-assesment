# Django-Assesment

Create a Django API with django rest framework

- [ ] users with custom roles - admin, coach, agent, football player
- [ ] sign up and social sign up (google, facebook)
- [ ] login and social login
- [ ] password reset

# How to install

- clone the repository from "<https://github.com/rawidaniel/django-assesment.git>"

- Create a `.env` file in your project root folder and add your variables. See .env.example file for assistance.

- create virtual environemtnal using "`pienv shell`" command
- install dependencies using "`pipenv install`" command
- create the docker container using "`docker compose up --build`" command
- access the postgres container using "`docker exec -it django-assesement-postgres psql -U postgres`" command
- create the databse using "`CREATE DATABASE djangoassessment;`" command
- create mailtrap account to receive email messages at "<https://mailtrap.io/home>"
- create an api app for google at "<https://console.cloud.google.com/welcome?project=lightning-menu>" to get Client_Secret and Client_Id.
- create an app at "<https://developers.facebook.com>" to get App ID and secrete

- run the server using "`python manage.py runserver`"
