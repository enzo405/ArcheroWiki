# ARCHERO version=1.2


# Step change db : 

- `python -Xutf8 manage.py dumpdata > data.json`
- `changement dans models.py`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `si migrate marche pas faut suppr la db en local`
- `python manage.py loaddata data.json`
___
# Script : 
- `python manage.py createsuperuser`
- `python manage.py makemigrations`
- `python manage.py migrate`

___
# DOCKER :
- `mettre hyper V`
- `redémarrer PC`
- `& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon`
- `docker login reg.chaboisseau.net`
- `user / mdp`
- `docker build -t reg.chaboisseau.net/archero:v1.x .`
- `docker push reg.chaboisseau.net/archero:v1.x .`

___
# DOCKER V2 :
- `mettre hyper V`
- `redémarrer PC`
- `& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon`
- `docker login reg.chaboisseau.net`
- `user / mdp`
- `docker build -t archero:v1.x .`
- `docker image ls`
- `docker image tag [tag qui correspond] reg.chaboisseau.net/archero:v1.x`
- `docker push reg.chaboisseau.net/archero:v1.x`

___
[FAVICO convert](https://favicon.io/favicon-converter/)


___
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









COPY public.calculator_egg_equipped_table (id, ingame_id, egg_equipped1, egg_equipped2, egg_equipped3, egg_equipped4) FROM stdin;
"20	1-987654321	Choose	Choose	Choose	Choose"
"1	5-122439675	Ice Worm	Crimson Witch	Pea Shooter	Icefire Phantom"
"4	2-4890500	Skeleton King	Lava Golem	Queen Bee	Wasp"
"7	2-82466122	Choose	Choose	Choose	Choose"
"8	4-148586047	Crimson Witch	Fire Demon	Queen Bee	Choose"
"9	3-91391997	Purple Phantom	Icefire Phantom	Piranha	Choose"
"13	5-117005768	Ice Worm	Medusa-Boss	Skeleton King	Crimson Witch"
"14	3-139661978	Medusa-Boss	Ice Worm	Crimson Witch	Fire Demon"
"18	1-65174137	Medusa-Boss	Icefire Phantom	Ice Worm	Crimson Witch"
"19	1-81522755	Crimson Witch	Ice Worm	Flame Ghost	Fire Mage"
"23	2-6001993	Choose	Choose	Choose	Choose"
"24	4-98152869	Choose	Choose	Choose	Choose"
"25	6-696969	Choose	Choose	Choose	Choose"
"28	4-119525915	Medusa-Boss	Crimson Witch	Fire Demon	Choose"
"3	1-1361227	Crimson Witch	Ice Worm	Medusa-Boss	Piranha"
"30	1-1915079	Purple Phantom	Medusa-Boss	Crimson Witch	Scarlet Mage"
"27	5-58712443	One-eyed Bat	Skeleton Swordsman	Thorny Snake	Crimson Witch"
"15	1-3964637	Fire Demon	Crimson Witch	Ice Worm	Medusa-Boss"
"2	1-6950167	Crimson Witch	Skeleton King	Medusa-Boss	Ice Worm"
"22	4-107286598	Ice Worm	Fire Demon	Medusa-Boss	Crimson Witch"
"10	1-000000	Ice Worm	Crimson Witch	Skeleton King	Ice Demon"



5	2-137937283	Piranha	Crimson Witch	Medusa-Boss	Pea Shooter
29	1-64673050	Ice Worm	Skull Wizard	Fire Demon	Crimson Witch