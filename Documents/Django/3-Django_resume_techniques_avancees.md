#Django en resumé : [Les techniques avancées](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/les-vues-generiques)

[PREV](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/2-Django_resume_premiers_pas.md)
[NEXT](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/4-Django_resume_outils_supplementaires.md)

## Les vues génériques 
En résumé:

* Django fournit un ensemble de classes permettant d'éviter de réécrire plusieurs fois le même type de vue (affichage d'un template statique, liste d'objets, création d'objets…) ;

* Les vues génériques peuvent être déclarées directement au sein de urls.py (cas le plus pratique pour les TemplateView) ou dans views.py ;

* Chaque vue générique dispose d'un ensemble d'attributs permettant de définir ce que doit faire la vue : modèle concerné, template à afficher, gestion de la pagination, filtres… ;

* Il est possible d'automatiser les formulaires d'ajout, de mise à jour et de suppression d'objets via des vues génériques ;

* Le module django.views.generic regorge de classes (plusieurs dizaines en tout), n'hésitez pas à regarder si l'une d'entre elles fait ce que vous souhaitez avant de vous lancer.


## Techniques avancées dans les modèles 
En résumé:

* La classe Q permet d'effectuer des requêtes complexes avec les opérateurs « OU », « ET » et « NOT ».Avg, Max et Min permettent d'obtenir respectivement la moyenne, le maximum et le minimum d'une certaine colonne dans une table. Elles peuvent être combinées avec Countpour déterminer le nombre de lignes retournées.

* L'héritage de modèles permet de factoriser des modèles ayant des liens entre eux. Il existe plusieurs types d'héritage : abstrait, classique et les modèles proxy.

* L'application ContentType permet de décrire un modèle et de faire des relations génériques avec vos autres modèles (pensez à l'exemple des commentaires !).

## Simplifions nos templates : filtres, tags et contextes 

Schema d'exécution 
![alt text](http://uploads.siteduzero.com/files/420001_421000/420636.png)

En résumé :

* Django permet aux développeurs d'étendre les possibilités des templates en créant des filtres et des tags.

* Les filtres et tags créés sont organisés par modules. Pour utiliser un filtre ou un tag il faut charger son module via {% load nom_module %}.

* Les filtres sont de simples fonctions, prenant en entrée 1 ou 2 arguments et renvoyant toujours une chaîne de caractères.

* Le contexte des templates est l'ensemble des variables disponibles et utilisables dans un template. Ce contexte est rempli par toutes les fonctions citées dans TEMPLATE_CONTEXT_PROCESSORS, puis par la vue appelée et enfin par les éventuels tags du template.

* Les tags permettent des traitements plus complexes sur les données à afficher. Les tags peuvent avoir une « mémoire », plusieurs arguments, former des blocs…

## Les signaux et middlewares 
Ordre d'exécution des middlewares:
![alt text](http://sdz-upload.s3.amazonaws.com/prod/upload/middlewares-exec.png)

En résumé :

* Un signal est une notification envoyée par une application à Django lorsqu'une action se déroule, et renvoyée par le framework à toutes les autres parties d'applications qui se sont enregistrées pour savoir quand ce type d'action se déroule, et comment.

* Les signaux permettent d'effectuer des actions à chaque fois qu'un événement précis survient.

* Les middlewares sont des classes instanciées à chaque requête, exception, ou encore génération de template, dans l'ordre donné par MIDDLEWARE_CLASSES.

* Ils permettent d'effectuer une tâche précise à chaque appel.

[PREV](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/2-Django_resume_premiers_pas.md)
[NEXT](https://github.com/IRISIB/JukeBox/blob/master/Documents/Django/4-Django_resume_outils_supplementaires.md)
