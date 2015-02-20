#Django en resumé : [ Présentation de Django ](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/creez-vos-applications-web-avec-django)

[NEXT](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/2-Django_resume_premiers_pas.md)

##Le fonctionnement de Django

Schéma de l'architecture MVC:

![alt text](http://uploads.siteduzero.com/files/386001_387000/386515.png)

Schéma d'exécution d'une requête:

![alt text](http://uploads.siteduzero.com/files/386001_387000/386517.png)

En résumé :

* Django respecte l'architecture MVT, directement inspirée du très populaire modèle MVC ;

* Django gère de façon autonome la réception des requêtes et l'envoi des réponses au client (partie contrôleur) ;

* Un projet est divisé en plusieurs applications, ayant chacune un ensemble de vues, de modèles et de schémas d'URL ;

* Si elles sont bien conçues, ces applications sont réutilisables dans d'autres projets, puisque chaque application est indépendante.

##Gestion d'un projet
En résumé :

* L'administration de projet s'effectue via le script manage.py . Tout particulièrement, la création d'un projet se fait via la commande django-admin.py startproject mon_projet  ;

* À la création du projet, Django déploie un ensemble de fichiers, facilitant à la fois la structuration du projet et sa configuration ;

* Pour tester notre projet, il est possible de lancer un serveur de test, via la commande python manage.py runserver , dans le dossier de notre projet. Ce serveur de test ne doit pas être utilisé en production ;

* Il est nécessaire de modifier le settings.py, afin de configurer le projet selon nos besoins. Ce fichier ne doit pas être partagé avec les autres membres ou la production, puisqu'il contient des données dépendant de votre installation, comme la connexion à la base de données.

## Les bases de données et Django
En résumé :

![alt text](http://uploads.siteduzero.com/thb/396001_397000/396744.png)

* Une base de données permet de stocker vos données de façon organisée et de les récupérer en envoyant des requêtes à votre système de gestion de base de données ;

* De manière générale, nous communiquons la plupart du temps avec les bases de données via le langage SQL ;

* Il existe plusieurs systèmes de gestion de bases de données, ayant chacun ses particularités ;

* Pour faire face à ces différences, Django intègre une couche d'abstraction, afin de communiquer de façon uniforme et plus intuitive avec tous les systèmes : il s'agit de l'ORM que nous avons présenté brièvement ;

* Une ligne dans une table peut être liée à une autre ligne d'une autre table via le principe de clés étrangères : nous gardons l'identifiant de la ligne de la seconde table dans une colonne de la ligne de la première table.


[NEXT](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/2-Django_resume_premiers_pas.md)