#Django en resumé :  [Annexes](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/deployer-votre-application-en-production)

[PREV](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/4-Django_resume_outils_supplementaires.md)

## Déployer votre application en production 
En résumé :

* Il ne faut pas utiliser le serveur python manage.py runserver en production ;

* Une des méthodes d'installation possible passe par Apache2 avec le mod_wsgi, en exécutant le script wsgi.py contenu dans le répertoire du projet ;

* Il existe également le combo nginx + gunicorn, que l'on a également décrit ;

* Si l'on désactive le mode DEBUG, Django enverra un e-mail à toutes les personnes listées dans le tuple ADMINS en cas d'erreur 500 sur le site. Il est possible d'être averti en cas d'erreurs 404, et de filtrer les données sensibles envoyées (telles que les mots de passe) ; 

* Sentry est un projet Django permettant de surveiller votre propre projet de manière plus fine.

## [L'utilitaire manage.py](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/l-utilitaire-manage-py)  

[PREV](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/4-Django_resume_outils_supplementaires.md)
