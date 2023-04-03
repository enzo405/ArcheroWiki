# Wiki Actual Version : v1.5

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# README
## Description
This is a web application built using the Django framework in Python, designed to help the Archero gaming community. Archero is a popular game that involves battling through levels while upgrading your character's abilities and equipment. The application offers a range of tools to help players improve their gameplay, including an advanced stats calculator, tier lists, and other useful information.

## Contributors
I am the sole contributor to this project, which was started in late August 2022.

## Technologies
The application is built using a range of technologies, including:

- Python
- JavaScript
- HTML
- CSS
- JSON
- crontab

It also uses Docker for deployment, with a PostgreSQL database.

## Getting Started
To run the application locally, you will need to have Docker installed on your system. Once you have Docker installed, simply clone the repository and run the docker-compose up command to start the application.

## Usage
Once the application is up and running, you can access it by navigating to the appropriate URL in your web browser. From there, you can explore the various features and tools offered by the application to help you improve your gameplay in Archero.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


____
## Naming convention rule for calculation variables :
- type : var (+x%) / flat (+x)
- type2 : passiv / activ
- boost : atk / hp
- system : (jewel, altar, dragon etc...)
- for which variable it serve : (coef1)
- cumul for the total/global
- `[cumul_]system_type_type2_boost_...`

___
# Step change database :

- `python -Xutf8 manage.py dumpdata > data.json`
- `changing models.py`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `if migrate doesn't work, you need to delete the database through the psql command and DROP TABLE`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py loaddata data.json`
<!-- Remind to fill up the data.json -->
---


```diff
TODO :
- add page for emulator skill in fight with skill you can check (don't forget medals boost)
- details page add run boost from glyphs, dragon, stuff etc...
- refacto code poo
- centralize : theorycrafting page in data.py to make it editable with the futur API 
- dmgcalc put the correct runes for it's matched line
- README GitHub
- font number stuff image
```
```diff
Need to hack / datamine
- finish stuff data.py
- data relics
```
```diff
Future Release:
- glyphs unlocked in form (new table)
+ when patched : necklace attack base jewel stats
- form relics remake
- add all heroes star for future information in profile page
```
```diff
Why not ?
- system maintenance when changing db
```
```diff
When TigerShark API finished :
+ modify data with API
- translate
```
