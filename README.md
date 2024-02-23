## Sandbox API on FastAPI and Postgres
Current solution is for getting analyticals data.
Configured to run in docker-compose as a whole.

---
### Components and main features:
* API - Python FastAPI
  * Get method of analytical data, 1 select statements with parameters
  * Post method for adding new analytical data
  * DB communication via Psycopg pools
* DB - Postgresql (1 table)
  * Separate DB AND Schema AND User for project
  * Include some synthetic data configs to populate data via <a href="https://www.getsynth.com/" class="external-link" target="_blank">**Synth**</a>
  * If u r lazy, <a href="https://github.com/S0llCap/FastApi_Postgres_SND/tree/whole_db/app/DB/data" class="external-link" target="_blank">there is a whole synthetic database for current tables in branch "whole_db" </a> :)
and yes, container will map its data  if u download it :)
* DB UI - PgAdmin

### Configs to know about
Almost all configs have logins and passwords in them unfortunately :)
1. Main compose file ```/app/docker-compose.yml```. Is has port bindings, volumes mapping, resource allocation, some component configurations
  Dont forget to look inside that file and map volumes that are at the end. Or u can hardcode them instead in configs :)
3. In ```/app/DB/init``` there are .sql scripts for schema and roles creation.
4. In ```/app/DB/synth/adv_data``` there is .json config for <a href="https://www.getsynth.com/" class="external-link" target="_blank">**Synth**</a> data generator and .exe itself to run gen on windows
6. In ```/app/API ``` important files are:
   * .env . You need to create it yourself based on your database config. There is .example file in repo
   * Dockerfile for API. Docker-compose use this one to build API image
   * requerements.txt for Python modules installation

### How to run:
Locate to the directory where will be ```.../app/docker-compose.yml```
Run 
```bash
docker-compose -f docker-compose.yml up --build -d
```
If you want to generate some data in database yourself, you should do that before run the containers.
To do so <a href="https://www.getsynth.com/docs/blog/2021/03/09/postgres-data-gen#using-a-data-generator-like-synth" class="external-link" target="_blank">**just follow official documentation**</a>, ist fairly simple :)

### "Minor inconveniences" and what-to-improve list
* Add password storages
* Add monitoring, like Prometheus and etc
* In API:
  * add and config logging library
  * add ```try-except``` blocks, validations, error handlers
  * for ```getAnalyticsData``` try to find another way to restrict values  , aside converting GET to POST
  * for ```getAnalyticsData``` try to build select with less constant string in helper function (but tbh, after some days with SQLAlchemy is seems imposible for that kind of db queries)
* In DB:
 * MOAR DATA :D
 * For "online API" make up cases to use Redis/Tarantool hot-storage layer with business logic for storing actual data from Postgres

