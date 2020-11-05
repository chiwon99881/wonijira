# Jira Clone 

- #0 First Init 

    > pipenv --three 

    > pipenv install Django==2.2.5

    --------------------------------------------------------------
    
    > 1.Create Repository on Github 

    > 2.git init

    > 3.git remote add origin [Your Repository URL]

    > 4.git add .

    > 5.git commit -m "#0 First Init" 

    > 6.git push origin master 


- #1 Settings

    > pipenv install flake8 black --dev 

- #2 User Custom 1

    > python manage.py makemigrations

    > python manage.py migrate 

    > python manage.py createsuperuser 

- #3 User Model 1

- #4 Project, Issue, Attachment Model 1

- #5 Generate Issue Key like JIRA

- #6 Issue Admin with Foreign Key