# FoodRecSys2021
Sistema di raccomandazione di ricette personalizzate realizzato durante il lavoro di tesi di Serino <br>

# FoodRecSys 
All'interno della directory **FoodRecSys** sono presenti i file costituenti l'interfaccia web.

## Configurazioni
Sono state realizzate ai fini dello sviluppo del Recommender System due diverse configurazioni: la prima presenta insieme alle raccomandazioni delle etichette che danno informazioni su quanto una ricetta possa essere salutare, la seconda presenta la raccomandazione senza etichette.
<br>Per poter utilizzare la prima configurazione è necessario impostare alla riga 179 dei file *manage_request.php*, *manage_request2.php* e *manage_request3.php*
```php
    $random = 1;
```
Per poter utilizzare la seconda configurazione è necessario impostare alla riga 179 dei file *manage_request.php*, *manage_request2.php* e *manage_request3.php*
```php
    $random = 0;
```
Se si vuole impostare la configurazione in maniera randomizzata è necessario impostare alla riga 179 dei file *manage_request.php*, *manage_request2.php* e *manage_request3.php*
```php
    $random = rand(0,1);
```


# FoodWebApp
All'interno della directory **FoodWebApp** è presente il python nel quale è implementato il Recommender System e gli script per poter avviare e terminare il sistema di raccomanzazione.

## Installation
Prima di iniziare ad utilizzare il servizio, assicurati di avere a disposizione Python 3 e installa i seguenti moduli:
1. Flask
```shell
   pip install Flask    
```
2. Flask_restful
```shell
   pip install Flask-RESTful    
```
3. Requests
```shell
   pip install requests    
```
4. Random
```shell
   pip install random2   
```

## Recommender Service
Per avviare il Recommender eseguire il comando
```shell
    ./recommender_start.sh 
```
O 
```shell
    nohup python3 recommender.py &
```
Per terminare il Recommender eseguire il comando
```shell
    ./recommender_stop.sh 
```
O 
```shell
    pkill -f recommender.py
```




