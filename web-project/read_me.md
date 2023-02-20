# ARCHERO version=1.19.1
____
## Règle nommage variables calcul :
- type : var (+x%) / flat (+x)
- type2 : passiv / activ
- boost : atk / hp
- system : (jewel, altar, dragon etc...)
- for which variable it serve : (coef1)
- cumul pour total
- `[cumul_]system_type_type2_boost_...`


___
# Step change db :

- `python -Xutf8 manage.py dumpdata > data.json`
- `changement dans models.py`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `si migrate marche pas faut suppr la db en local`
- `python manage.py loaddata data.json`

---

# Script :

- `python manage.py createsuperuser`
- `python manage.py makemigrations`
- `python manage.py migrate`

---

# DOCKER :

- `mettre hyper V`
- `redémarrer PC`
- `& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon`
- `docker login url-dockerhub`
- `user / mdp`
- `docker build -t url-dockerhub/archero:v1.x .`
- `docker push url-dockerhub/archero:v1.x .`

---

# DOCKER V2 :

- `mettre hyper V`
- `redémarrer PC`
- `& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon`
- `docker login url-dockerhub`
- `user / mdp`
- `docker build -t archero:v1.x .`
- `docker image ls`
- `docker image tag [tag qui correspond] url-dockerhub/archero:v1.x`
- `docker push url-dockerhub/archero:v1.x`

---

[FAVICO convert](https://favicon.io/favicon-converter/)

---

# DUMP DB :

- `ssh connection sur pc distant`
- `aller dans docker `
- `docker exec -u postgres -ti archero-db  pg_dumpall > toto`
- `ensuite le moove dans /home/ozne`
- `exit du pc distant`
- `puis dans le fichier qu'on veut faire scp  exemple@x.x.x.x:/home/ozne/nomdata .`
  Ensuite pour exécuté notre fichier il suffit d'utiliser la commande suivante :
- `psql -U <username> -d <dbname> -a -f <filenamescript>`
- `En dernier il suffit de faire la commande de django : python -Xutf8 manage.py dumpdata > data.json`

Et voilà nous avons notre fichier dump de la base de donnée en json
Si probleme lors du loaddata avec unicode Error => ouvrir le fichier dans notepad++ pour changer l'encodage vers UTF-8


```sql
DROP TABLE ************** CASCADE;
DROP TABLE ************** CASCADE;
DROP TABLE ************** CASCADE;
DROP TABLE ************** CASCADE;
DROP TABLE ************** CASCADE;
DROP TABLE ************** CASCADE;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
DROP TABLE **************;
```


```diff
TODO :
- form relics remake
- data relics
- glyphs unlocked in form (new table)
+ when patched : necklace attack base jewel stats
- bug login id null
```
```diff
Future Release:
- dragon upgrade cost (switch between rank A, S, SS or choice select)
- change font familly
- add upgrade cost for altar & relics
- add page for emulator skill in fight (with like medals, skill you can check)
+ embed link for skill & heros & item page
- details page add run boost from glyphs, dragon, stuff etc...
```
```diff
Why not ?
- system maintenance changement db
- guild API for clan recruiting
- models put the correct runes for it's matched line (models.py)
- form submit fixed pos
- new method to update profile ?
+ page data missing
```
```diff
When TigerShark API finished :
+ modify data with API
- translate
```

*Update 20/02 21h36*