# ARCHERO version=1.13.8

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
- `docker login $URLDOCKER`
- `user / mdp`
- `docker build -t $URLDOCKER/archero:v1.x .`
- `docker push $URLDOCKER/archero:v1.x .`

---

# DOCKER V2 :

- `mettre hyper V`
- `redémarrer PC`
- `& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon`
- `docker login $URLDOCKER`
- `user / mdp`
- `docker build -t archero:v1.x .`
- `docker image ls`
- `docker image tag [tag qui correspond] $URLDOCKER/archero:v1.x`
- `docker push $URLDOCKER/archero:v1.x`

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