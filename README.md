# Population-Data-Science
Population-Data-Science


Step 1) Create folder /data/populationdb.
        Make sure the population.sql file present at /data/populationdb/population.sql

Step 2) Deploy postgres 15.1 docker container using docker-compose file. 
        The docker compose file will create a database 'worldpopulation' and load the tables with population details of 1000 citizens around the world. 
        docker-compose -f docker-compose-population-postgres.yml up -d


Step 3) Create virtual environment 
        python -m venv .venv 
        source .venv/bin/activate 
        pip3 install -r requirements.txt

Step 4) Start python flask app server 
        python app.py 

Step 5) Reference - Python REST API with Flask - https://www.youtube.com/watch?v=DlNIXC9SaF4 

Step 6) Reference - REST API - https://www.youtube.com/watch?v=qbLc5a9jdXo 
