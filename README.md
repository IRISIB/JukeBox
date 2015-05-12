# JukeBox

##Installation on a linux device

One shot install :

```shell
git clone git@github.com:IRISIB/JukeBox.git
cd JukeBox
virtualenv --distribute --no-site-packages ve
source ve/bin/activate
pip install -r requirements.txt
cd JukeBox
chmod +x ./manage.py
```

Run :

```shell
source ve/bin/activate 
./manage.py migrate
./manage.py runserver
```

##Installation of NodeJS on a linux device

```shell
sudo apt-get install python-software-properties python g++ make
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
```

Run on a Node.js shell:

```shell
JukeBox\nodejs>node server.js
```

## Demo
https://jukebox-demo.herokuapp.com/

## Contact information

Contact : dev.jukebox@gmail.com



Pour utiliser alauth sur le site, il faut suivre la marche à suivre suivante : 

- faire une migration de la base de donnée pour la création des tables 
- creer un super user pour pouvoir acceder à l'administration DJango 
- Il faut ensuite ajouter les différentes applications sociales (une pour twitter et une pour facebook)
- Les clés publiques et secretes sont récupérables sur l'api des sites en question une fois connecté avec le compte dev
- tester si la page connexion de la section voting fonctionne. -> si erreur, il faut changer le site id dans settings.py