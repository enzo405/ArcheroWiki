# Utilisation de l'image officielle Python version 3.10.5 comme base
FROM python:3.10.5

# Mise à jour de pip à la dernière version
RUN pip install --upgrade pip

# Copie des fichiers de configuration dans /bin/conf/ de l'image
COPY conf/requirements.txt requirements.txt
COPY conf/root /var/spool/cron/crontabs/root

# Installation des dépendances Python spécifiées dans requirements.txt
RUN pip install -r requirements.txt

# Installation de cron, nano et gettext via apt
RUN apt update && apt-get install -y cron nano && apt-get install -y gettext

# Copie de tout le contenu du répertoire de travail actuel dans /app de l'image
COPY . /app

# Définition du répertoire de travail par défaut
WORKDIR /app

# Exposition du port 8000
EXPOSE 8000

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD sh conf/start.sh