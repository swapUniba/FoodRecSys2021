# FoodRecSys2021
Sistema di raccomandazione di ricette personalizzate realizzato durante il lavoro di tesi di Serino <br>

# FoodRecSys 
All'interno della directory **FoodRecSys** sono presenti i file costituenti l'interfaccia web.

# FoodWebApp
All'interno della directory **FoodWebApp** è presente il python nel quale è implementato il Recommender System e gli script per poter avviare e terminare il sistema di raccomanzazione.

# Recommender Service
#h1 Per avviare il Recommender eseguire il comando
```shell
    ./recommender_start.sh 
```
O 
```shell
    nohup python3 recommender.py &
```
#h2 Per terminare il Recommender eseguire il comando
```shell
    ./recommender_stop.sh 
```
O 
```shell
    pkill -f recommender.py
```


