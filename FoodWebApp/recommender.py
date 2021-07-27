
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_restful import Api, Resource
import requests
import random




def nutriscore(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da):

    payload = {"q": key_word, "app_id": app_id, "app_key": app_key, "from": da, "to": fino, "health": etichette_salutari, "dishType": tipo_pasto, "diet": tipo_dieta}
    try:
        response = requests.get("https://api.edamam.com/search",params=payload)  # passo come parametri ciò che ho definito in payload

        if response.ok:
            data = response.json()

            # print (json.dumps(data, indent=2, sort_keys=True))
            for recipe in data['hits']:

                recipe['recipe']['totalNutrients']['PROCNT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['PROCNT']['quantity'])
                recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'])
                recipe['recipe']['totalNutrients']['FASAT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FASAT'][
                        'quantity'])  # trasformazione delle calorie da float a int
                recipe['recipe']['totalNutrients']['SUGAR']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['SUGAR']['quantity'])
                recipe['recipe']['totalNutrients']['NA']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['NA']['quantity'])
                recipe['recipe']['totalNutrients']['FIBTG']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FIBTG']['quantity'])

                energia = 0
                zuccheri = 0
                grassi_saturi = 0
                sodio = 0
                fibre = 0
                proteine = 0

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 335:
                    energia = 0

                if 335 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 670:
                    energia = 1

                if 670 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1005:
                    energia = 2

                if 1005 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1340:
                    energia = 3

                if 1340 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1675:
                    energia = 4

                if 1675 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2010:
                    energia = 5

                if 2010 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2345:
                    energia = 6

                if 2345 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2680:
                    energia = 7

                if 2680 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3015:
                    energia = 8

                if 3015 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3350:
                    energia = 9

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] > 3350:
                    energia = 10

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 4.5:
                    zuccheri = 0

                if 4.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 9:
                    zuccheri = 1

                if 9 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 13.5:
                    zuccheri = 2

                if 13.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 18:
                    zuccheri = 3

                if 18 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 22.5:
                    zuccheri = 4

                if 22.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 27:
                    zuccheri = 5

                if 27 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 31:
                    zuccheri = 6

                if 31 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 36:
                    zuccheri = 7

                if 36 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 40:
                    zuccheri = 8

                if 40 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 45:
                    zuccheri = 9

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] > 45:
                    zuccheri = 10

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 1:
                    grassi_saturi = 0

                if 1 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 2:
                    grassi_saturi = 1

                if 2 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 3:
                    grassi_saturi = 2

                if 3 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 4:
                    grassi_saturi = 3

                if 4 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 5:
                    grassi_saturi = 4

                if 5 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 6:
                    grassi_saturi = 5

                if 6 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 7:
                    grassi_saturi = 6

                if 7 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 8:
                    grassi_saturi = 7

                if 8 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 9:
                    grassi_saturi = 8

                if 9 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 10:
                    grassi_saturi = 9

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] > 10:
                    grassi_saturi = 10

                if recipe['recipe']['totalNutrients']['NA']['quantity'] <= 90:
                    sodio = 0

                if 90 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 180:
                    sodio = 1

                if 180 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 270:
                    sodio = 2

                if 270 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 360:
                    sodio = 3

                if 360 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 450:
                    sodio = 4

                if 450 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 540:
                    sodio = 5

                if 540 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 630:
                    sodio = 6

                if 630 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 720:
                    sodio = 7

                if 720 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 810:
                    sodio = 8

                if 810 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 900:
                    sodio = 9

                if recipe['recipe']['totalNutrients']['NA']['quantity'] > 900:
                    sodio = 10

                negativi = energia + zuccheri + grassi_saturi + sodio

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 0.7:
                    fibre = 0

                if 0.7 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 1.4:
                    fibre = 1

                if 1.4 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.1:
                    fibre = 2

                if 2.1 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.8:
                    fibre = 3

                if 2.8 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 3.5:
                    fibre = 4

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] > 3.5:
                    fibre = 5

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 1.6:
                    proteine = 0

                if 1.6 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 3.2:
                    proteine = 1

                if 3.2 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 4.8:
                    proteine = 2

                if 4.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 6.8:
                    proteine = 3

                if 6.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 8:
                    proteine = 4

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] > 8:
                    proteine = 5
                positivi = fibre + proteine

                health_score = negativi - positivi

                if health_score <= -1:
                    colore = 'verde scuro'
                if 0 <= health_score <= 2:
                    colore = 'verde'
                if 3 <= health_score <= 10:
                    colore = 'giallo'
                if 11 <= health_score <= 18:
                    colore = 'arancione'
                if health_score >= 19:
                    colore = 'rosso'

                recipe['recipe']['health score'] = health_score
                recipe['recipe']['nutri score'] = colore

            for recipe in data['hits']:
                r = sorted(data['hits'], key=lambda k: k['recipe']['health score'], reverse=True)
            dict2 = {}
            for recipe in r:
                name = recipe['recipe']['label']
                imageURL = recipe['recipe']['image']
                ingredients = recipe['recipe']['ingredientLines']
                url = recipe['recipe']['uri']
                ordinamento = 'nutriscore'
                etichetta = 'ricetta sana'
                dict2 = {'name': name,
                         'imageURL': imageURL,
                         'ingredients': ingredients,
                         'url': url,
                         'ordinamento': ordinamento,
                         'etichetta': etichetta}
        else:
            print("Status Code: ", response.status_code)
            print("Response Content:", response.content)
            raise Exception("C'è stato un errore...")

        return dict2

    except UnboundLocalError:
        messaggio= 'Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'
        errore = {'mess': messaggio}
        return messaggio


def anticalorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da):

    payload = {"q": key_word, "app_id": app_id, "app_key": app_key, "from": da, "to": fino, "health": etichette_salutari, "dishType": tipo_pasto, "diet": tipo_dieta}
    try:
        response = requests.get("https://api.edamam.com/search",params=payload)  # passo come parametri ciò che ho definito in payload

        if response.ok:
            data = response.json()

            # print (json.dumps(data, indent=2, sort_keys=True))
            for recipe in data['hits']:

                recipe['recipe']['totalNutrients']['PROCNT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['PROCNT']['quantity'])
                recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'])
                recipe['recipe']['totalNutrients']['FASAT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FASAT'][
                        'quantity'])  # trasformazione delle calorie da float a int
                recipe['recipe']['totalNutrients']['SUGAR']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['SUGAR']['quantity'])
                recipe['recipe']['totalNutrients']['NA']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['NA']['quantity'])
                recipe['recipe']['totalNutrients']['FIBTG']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FIBTG']['quantity'])

                energia = 0
                zuccheri = 0
                grassi_saturi = 0
                sodio = 0
                fibre = 0
                proteine = 0

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 335:
                    energia = 0

                if 335 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 670:
                    energia = 1

                if 670 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1005:
                    energia = 2

                if 1005 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1340:
                    energia = 3

                if 1340 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1675:
                    energia = 4

                if 1675 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2010:
                    energia = 5

                if 2010 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2345:
                    energia = 6

                if 2345 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2680:
                    energia = 7

                if 2680 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3015:
                    energia = 8

                if 3015 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3350:
                    energia = 9

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] > 3350:
                    energia = 10

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 4.5:
                    zuccheri = 0

                if 4.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 9:
                    zuccheri = 1

                if 9 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 13.5:
                    zuccheri = 2

                if 13.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 18:
                    zuccheri = 3

                if 18 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 22.5:
                    zuccheri = 4

                if 22.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 27:
                    zuccheri = 5

                if 27 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 31:
                    zuccheri = 6

                if 31 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 36:
                    zuccheri = 7

                if 36 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 40:
                    zuccheri = 8

                if 40 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 45:
                    zuccheri = 9

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] > 45:
                    zuccheri = 10

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 1:
                    grassi_saturi = 0

                if 1 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 2:
                    grassi_saturi = 1

                if 2 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 3:
                    grassi_saturi = 2

                if 3 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 4:
                    grassi_saturi = 3

                if 4 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 5:
                    grassi_saturi = 4

                if 5 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 6:
                    grassi_saturi = 5

                if 6 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 7:
                    grassi_saturi = 6

                if 7 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 8:
                    grassi_saturi = 7

                if 8 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 9:
                    grassi_saturi = 8

                if 9 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 10:
                    grassi_saturi = 9

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] > 10:
                    grassi_saturi = 10

                if recipe['recipe']['totalNutrients']['NA']['quantity'] <= 90:
                    sodio = 0

                if 90 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 180:
                    sodio = 1

                if 180 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 270:
                    sodio = 2

                if 270 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 360:
                    sodio = 3

                if 360 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 450:
                    sodio = 4

                if 450 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 540:
                    sodio = 5

                if 540 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 630:
                    sodio = 6

                if 630 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 720:
                    sodio = 7

                if 720 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 810:
                    sodio = 8

                if 810 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 900:
                    sodio = 9

                if recipe['recipe']['totalNutrients']['NA']['quantity'] > 900:
                    sodio = 10

                negativi = energia + zuccheri + grassi_saturi + sodio

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 0.7:
                    fibre = 0

                if 0.7 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 1.4:
                    fibre = 1

                if 1.4 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.1:
                    fibre = 2

                if 2.1 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.8:
                    fibre = 3

                if 2.8 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 3.5:
                    fibre = 4

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] > 3.5:
                    fibre = 5

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 1.6:
                    proteine = 0

                if 1.6 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 3.2:
                    proteine = 1

                if 3.2 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 4.8:
                    proteine = 2

                if 4.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 6.8:
                    proteine = 3

                if 6.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 8:
                    proteine = 4

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] > 8:
                    proteine = 5
                positivi = fibre + proteine

                health_score = negativi - positivi

                if health_score <= -1:
                    colore = 'verde scuro'
                if 0 <= health_score <= 2:
                    colore = 'verde'
                if 3 <= health_score <= 10:
                    colore = 'giallo'
                if 11 <= health_score <= 18:
                    colore = 'arancione'
                if health_score >= 19:
                    colore = 'rosso'

                recipe['recipe']['health score'] = health_score
                recipe['recipe']['nutri score'] = colore

            for recipe in data['hits']:
                r = sorted(data['hits'], key=lambda k: k['recipe']['totalNutrients']['ENERC_KCAL']['quantity'], reverse=False)
            dict2 = {}
            for recipe in r:
                name = recipe['recipe']['label']
                imageURL = recipe['recipe']['image']
                ingredients = recipe['recipe']['ingredientLines']
                url = recipe['recipe']['uri']
                ordinamento = 'anti-calorie'
                etichetta = ' ricetta popolare'
                dict2 = {'namen': name,
                         'imageURLn': imageURL,
                         'ingredientsn': ingredients,
                         'urln': url,
                         'ordinamenton': ordinamento,
                         'etichettan': etichetta}
        else:
            print("Status Code: ", response.status_code)
            print("Response Content:", response.content)
            raise Exception("C'è stato un errore...")

        return dict2

    except UnboundLocalError:
        messaggio= 'Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'
        errore = {'mess': messaggio}
        return messaggio


def calorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da):
    payload = {"q": key_word, "app_id": app_id, "app_key": app_key, "from": da, "to": fino, "health": etichette_salutari, "dishType": tipo_pasto, "diet": tipo_dieta}
    try:
        response = requests.get("https://api.edamam.com/search",
                                params=payload)  # passo come parametri ciò che ho definito in payload

        if response.ok:
            data = response.json()

            # print (json.dumps(data, indent=2, sort_keys=True))
            for recipe in data['hits']:

                recipe['recipe']['totalNutrients']['PROCNT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['PROCNT']['quantity'])
                recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'])
                recipe['recipe']['totalNutrients']['FASAT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FASAT'][
                        'quantity'])  # trasformazione delle calorie da float a int
                recipe['recipe']['totalNutrients']['SUGAR']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['SUGAR']['quantity'])
                recipe['recipe']['totalNutrients']['NA']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['NA']['quantity'])
                recipe['recipe']['totalNutrients']['FIBTG']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FIBTG']['quantity'])

                energia = 0
                zuccheri = 0
                grassi_saturi = 0
                sodio = 0
                fibre = 0
                proteine = 0

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 335:
                    energia = 0

                if 335 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 670:
                    energia = 1

                if 670 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1005:
                    energia = 2

                if 1005 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1340:
                    energia = 3

                if 1340 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1675:
                    energia = 4

                if 1675 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2010:
                    energia = 5

                if 2010 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2345:
                    energia = 6

                if 2345 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2680:
                    energia = 7

                if 2680 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3015:
                    energia = 8

                if 3015 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3350:
                    energia = 9

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] > 3350:
                    energia = 10

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 4.5:
                    zuccheri = 0

                if 4.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 9:
                    zuccheri = 1

                if 9 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 13.5:
                    zuccheri = 2

                if 13.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 18:
                    zuccheri = 3

                if 18 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 22.5:
                    zuccheri = 4

                if 22.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 27:
                    zuccheri = 5

                if 27 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 31:
                    zuccheri = 6

                if 31 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 36:
                    zuccheri = 7

                if 36 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 40:
                    zuccheri = 8

                if 40 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 45:
                    zuccheri = 9

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] > 45:
                    zuccheri = 10

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 1:
                    grassi_saturi = 0

                if 1 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 2:
                    grassi_saturi = 1

                if 2 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 3:
                    grassi_saturi = 2

                if 3 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 4:
                    grassi_saturi = 3

                if 4 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 5:
                    grassi_saturi = 4

                if 5 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 6:
                    grassi_saturi = 5

                if 6 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 7:
                    grassi_saturi = 6

                if 7 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 8:
                    grassi_saturi = 7

                if 8 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 9:
                    grassi_saturi = 8

                if 9 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 10:
                    grassi_saturi = 9

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] > 10:
                    grassi_saturi = 10

                if recipe['recipe']['totalNutrients']['NA']['quantity'] <= 90:
                    sodio = 0

                if 90 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 180:
                    sodio = 1

                if 180 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 270:
                    sodio = 2

                if 270 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 360:
                    sodio = 3

                if 360 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 450:
                    sodio = 4

                if 450 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 540:
                    sodio = 5

                if 540 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 630:
                    sodio = 6

                if 630 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 720:
                    sodio = 7

                if 720 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 810:
                    sodio = 8

                if 810 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 900:
                    sodio = 9

                if recipe['recipe']['totalNutrients']['NA']['quantity'] > 900:
                    sodio = 10

                negativi = energia + zuccheri + grassi_saturi + sodio

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 0.7:
                    fibre = 0

                if 0.7 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 1.4:
                    fibre = 1

                if 1.4 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.1:
                    fibre = 2

                if 2.1 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.8:
                    fibre = 3

                if 2.8 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 3.5:
                    fibre = 4

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] > 3.5:
                    fibre = 5

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 1.6:
                    proteine = 0

                if 1.6 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 3.2:
                    proteine = 1

                if 3.2 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 4.8:
                    proteine = 2

                if 4.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 6.8:
                    proteine = 3

                if 6.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 8:
                    proteine = 4

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] > 8:
                    proteine = 5
                positivi = fibre + proteine

                health_score = negativi - positivi

                if health_score <= -1:
                    colore = 'verde scuro'
                if 0 <= health_score <= 2:
                    colore = 'verde'
                if 3 <= health_score <= 10:
                    colore = 'giallo'
                if 11 <= health_score <= 18:
                    colore = 'arancione'
                if health_score >= 19:
                    colore = 'rosso'

                recipe['recipe']['health score'] = health_score
                recipe['recipe']['nutri score'] = colore
            for recipe in data['hits']:
                r = sorted(data['hits'], key=lambda k: k['recipe']['totalNutrients']['ENERC_KCAL']['quantity'], reverse=True)

            dict = {}
            for recipe in r:
                name = recipe['recipe']['label']
                imageURL = recipe['recipe']['image']
                ingredients = recipe['recipe']['ingredientLines']
                url = recipe['recipe']['uri']
                ordinamento = 'calorie'
                etichetta = 'ricetta ipocalorica'
                dict = {'name': name,
                        'imageURL': imageURL,
                        'ingredients': ingredients,
                        'url': url,
                        'ordinamento': ordinamento,
                        'etichetta': etichetta}
        else:
            print("Status Code: ", response.status_code)
            print("Response Content:", response.content)
            raise Exception("C'è stato un errore...")

        return dict
    except UnboundLocalError:
        messaggio = 'Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'
        errore = {'mess': messaggio}
        return messaggio


def etichette(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da):
    payload = {"q": key_word, "app_id": app_id, "app_key": app_key, "from": da, "to": fino,"health": etichette_salutari, "dishType": tipo_pasto, "diet":tipo_dieta}
    try:
        response = requests.get("https://api.edamam.com/search",
                                params=payload)  # passo come parametri ciò che ho definito in payload

        if response.ok:
            data = response.json()

            # print (json.dumps(data, indent=2, sort_keys=True))
            for recipe in data['hits']:

                recipe['recipe']['totalNutrients']['PROCNT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['PROCNT']['quantity'])
                recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'])
                recipe['recipe']['totalNutrients']['FASAT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FASAT'][
                        'quantity'])  # trasformazione delle calorie da float a int
                recipe['recipe']['totalNutrients']['SUGAR']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['SUGAR']['quantity'])
                recipe['recipe']['totalNutrients']['NA']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['NA']['quantity'])
                recipe['recipe']['totalNutrients']['FIBTG']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FIBTG']['quantity'])

                energia = 0
                zuccheri = 0
                grassi_saturi = 0
                sodio = 0

                fibre = 0
                proteine = 0

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 335:
                    energia = 0

                if 335 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 670:
                    energia = 1

                if 670 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1005:
                    energia = 2

                if 1005 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1340:
                    energia = 3

                if 1340 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1675:
                    energia = 4

                if 1675 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2010:
                    energia = 5

                if 2010 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2345:
                    energia = 6

                if 2345 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2680:
                    energia = 7

                if 2680 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3015:
                    energia = 8

                if 3015 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3350:
                    energia = 9

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] > 3350:
                    energia = 10

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 4.5:
                    zuccheri = 0

                if 4.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 9:
                    zuccheri = 1

                if 9 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 13.5:
                    zuccheri = 2

                if 13.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 18:
                    zuccheri = 3

                if 18 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 22.5:
                    zuccheri = 4

                if 22.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 27:
                    zuccheri = 5

                if 27 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 31:
                    zuccheri = 6

                if 31 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 36:
                    zuccheri = 7

                if 36 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 40:
                    zuccheri = 8

                if 40 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 45:
                    zuccheri = 9

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] > 45:
                    zuccheri = 10

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 1:
                    grassi_saturi = 0

                if 1 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 2:
                    grassi_saturi = 1

                if 2 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 3:
                    grassi_saturi = 2

                if 3 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 4:
                    grassi_saturi = 3

                if 4 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 5:
                    grassi_saturi = 4

                if 5 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 6:
                    grassi_saturi = 5

                if 6 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 7:
                    grassi_saturi = 6

                if 7 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 8:
                    grassi_saturi = 7

                if 8 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 9:
                    grassi_saturi = 8

                if 9 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 10:
                    grassi_saturi = 9

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] > 10:
                    grassi_saturi = 10

                if recipe['recipe']['totalNutrients']['NA']['quantity'] <= 90:
                    sodio = 0

                if 90 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 180:
                    sodio = 1

                if 180 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 270:
                    sodio = 2

                if 270 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 360:
                    sodio = 3

                if 360 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 450:
                    sodio = 4

                if 450 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 540:
                    sodio = 5

                if 540 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 630:
                    sodio = 6

                if 630 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 720:
                    sodio = 7

                if 720 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 810:
                    sodio = 8

                if 810 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 900:
                    sodio = 9

                if recipe['recipe']['totalNutrients']['NA']['quantity'] > 900:
                    sodio = 10

                negativi = energia + zuccheri + grassi_saturi + sodio

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 0.7:
                    fibre = 0

                if 0.7 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 1.4:
                    fibre = 1

                if 1.4 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.1:
                    fibre = 2

                if 2.1 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.8:
                    fibre = 3

                if 2.8 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 3.5:
                    fibre = 4

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] > 3.5:
                    fibre = 5

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 1.6:
                    proteine = 0

                if 1.6 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 3.2:
                    proteine = 1

                if 3.2 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 4.8:
                    proteine = 2

                if 4.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 6.8:
                    proteine = 3

                if 6.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 8:
                    proteine = 4

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] > 8:
                    proteine = 5
                positivi = fibre + proteine

                health_score = negativi - positivi

                if health_score <= -1:
                    colore = 'verde scuro'
                if 0 <= health_score <= 2:
                    colore = 'verde'
                if 3 <= health_score <= 10:
                    colore = 'giallo'
                if 11 <= health_score <= 18:
                    colore = 'arancione'
                if health_score >= 19:
                    colore = 'rosso'

                recipe['recipe']['health score'] = health_score
                recipe['recipe']['nutri score'] = colore
            for recipe in data['hits']:
                r = sorted(data['hits'], key=lambda k: len(k['recipe']['dietLabels']), reverse=True)
            dict = {}
            for recipe in r:
                name = recipe['recipe']['label']
                imageURL = recipe['recipe']['image']
                ingredients = recipe['recipe']['ingredientLines']
                url = recipe['recipe']['uri']
                ordinamento = 'etichette'
                etichetta = 'ricetta benefica'
                dict = {'name': name,
                        'imageURL': imageURL,
                        'ingredients': ingredients,
                        'url': url,
                        'ordinamento': ordinamento,
                        'etichetta':etichetta}
        else:
            print("Status Code: ", response.status_code)
            print("Response Content:", response.content)
            raise Exception("C'è stato un errore...")

        return dict
    except UnboundLocalError:
        messaggio = 'Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'
        errore = {'mess': messaggio}
        return messaggio




def proteine(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da):
    payload = {"q": key_word, "app_id": app_id, "app_key": app_key, "from": da, "to": fino,"health": etichette_salutari, "dishType": tipo_pasto, "diet": tipo_dieta}
    try:
        response = requests.get("https://api.edamam.com/search",params=payload)  # passo come parametri ciò che ho definito in payload

        if response.ok:

            data = response.json()
            # print (json.dumps(data, indent=2, sort_keys=True))
            for recipe in data['hits']:

                recipe['recipe']['totalNutrients']['PROCNT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['PROCNT']['quantity'])
                recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'])
                recipe['recipe']['totalNutrients']['FASAT']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FASAT'][
                        'quantity'])  # trasformazione delle calorie da float a int
                recipe['recipe']['totalNutrients']['SUGAR']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['SUGAR']['quantity'])
                recipe['recipe']['totalNutrients']['NA']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['NA']['quantity'])
                recipe['recipe']['totalNutrients']['FIBTG']['quantity'] = int(
                    recipe['recipe']['totalNutrients']['FIBTG']['quantity'])

                energia = 0
                zuccheri = 0
                grassi_saturi = 0
                sodio = 0
                fibre = 0
                proteine = 0

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 335:
                    energia = 0

                if 335 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 670:
                    energia = 1

                if 670 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1005:
                    energia = 2

                if 1005 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1340:
                    energia = 3

                if 1340 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 1675:
                    energia = 4

                if 1675 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2010:
                    energia = 5

                if 2010 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2345:
                    energia = 6

                if 2345 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 2680:
                    energia = 7

                if 2680 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3015:
                    energia = 8

                if 3015 < recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] <= 3350:
                    energia = 9

                if recipe['recipe']['totalNutrients']['ENERC_KCAL']['quantity'] > 3350:
                    energia = 10

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 4.5:
                    zuccheri = 0

                if 4.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 9:
                    zuccheri = 1

                if 9 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 13.5:
                    zuccheri = 2

                if 13.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 18:
                    zuccheri = 3

                if 18 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 22.5:
                    zuccheri = 4

                if 22.5 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 27:
                    zuccheri = 5

                if 27 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 31:
                    zuccheri = 6

                if 31 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 36:
                    zuccheri = 7

                if 36 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 40:
                    zuccheri = 8

                if 40 < recipe['recipe']['totalNutrients']['SUGAR']['quantity'] <= 45:
                    zuccheri = 9

                if recipe['recipe']['totalNutrients']['SUGAR']['quantity'] > 45:
                    zuccheri = 10

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 1:
                    grassi_saturi = 0

                if 1 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 2:
                    grassi_saturi = 1

                if 2 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 3:
                    grassi_saturi = 2

                if 3 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 4:
                    grassi_saturi = 3

                if 4 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 5:
                    grassi_saturi = 4

                if 5 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 6:
                    grassi_saturi = 5

                if 6 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 7:
                    grassi_saturi = 6

                if 7 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 8:
                    grassi_saturi = 7

                if 8 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 9:
                    grassi_saturi = 8

                if 9 < recipe['recipe']['totalNutrients']['FASAT']['quantity'] <= 10:
                    grassi_saturi = 9

                if recipe['recipe']['totalNutrients']['FASAT']['quantity'] > 10:
                    grassi_saturi = 10

                if recipe['recipe']['totalNutrients']['NA']['quantity'] <= 90:
                    sodio = 0

                if 90 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 180:
                    sodio = 1

                if 180 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 270:
                    sodio = 2

                if 270 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 360:
                    sodio = 3

                if 360 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 450:
                    sodio = 4

                if 450 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 540:
                    sodio = 5

                if 540 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 630:
                    sodio = 6

                if 630 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 720:
                    sodio = 7

                if 720 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 810:
                    sodio = 8

                if 810 < recipe['recipe']['totalNutrients']['NA']['quantity'] <= 900:
                    sodio = 9

                if recipe['recipe']['totalNutrients']['NA']['quantity'] > 900:
                    sodio = 10

                negativi = energia + zuccheri + grassi_saturi + sodio

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 0.7:
                    fibre = 0

                if 0.7 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 1.4:
                    fibre = 1

                if 1.4 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.1:
                    fibre = 2

                if 2.1 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 2.8:
                    fibre = 3

                if 2.8 < recipe['recipe']['totalNutrients']['FIBTG']['quantity'] <= 3.5:
                    fibre = 4

                if recipe['recipe']['totalNutrients']['FIBTG']['quantity'] > 3.5:
                    fibre = 5

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 1.6:
                    proteine = 0

                if 1.6 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 3.2:
                    proteine = 1

                if 3.2 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 4.8:
                    proteine = 2

                if 4.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 6.8:
                    proteine = 3

                if 6.8 < recipe['recipe']['totalNutrients']['PROCNT']['quantity'] <= 8:
                    proteine = 4

                if recipe['recipe']['totalNutrients']['PROCNT']['quantity'] > 8:
                    proteine = 5
                positivi = fibre + proteine

                health_score = negativi - positivi

                if health_score <= -1:
                    colore = 'verde scuro'
                if 0 <= health_score <= 2:
                    colore = 'verde'
                if 3 <= health_score <= 10:
                    colore = 'giallo'
                if 11 <= health_score <= 18:
                    colore = 'arancione'
                if health_score >= 19:
                    colore = 'rosso'

                recipe['recipe']['health score'] = health_score
                recipe['recipe']['nutri score'] = colore
            for recipe in data['hits']:
                r = sorted(data['hits'], key=lambda k: k['recipe']['totalNutrients']['PROCNT']['quantity'],reverse=True)
            dict1 = {}
            for recipe in r:
                name = recipe['recipe']['label']
                imageURL = recipe['recipe']['image']
                ingredients = recipe['recipe']['ingredientLines']
                url = recipe['recipe']['uri']
                ordinamento = 'proteine'
                etichetta = 'ricetta iperproteica'
                dict1 = {'name': name,
                         'imageURL': imageURL,
                         'ingredients': ingredients,
                         'url': url,
                         'ordinamento': ordinamento,
                         'etichetta': etichetta}

        else:
            print("Status Code: ", response.status_code)
            print("Response Content:", response.content)
            raise Exception("C'è stato un errore...")

        return dict1
    except UnboundLocalError:
        messaggio = 'Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'
        errore = {'mess': messaggio}
        return messaggio


def merge(risposta, risposta0):
    try:
        d3 = {**risposta, **risposta0}
        #d3 = risposta.copy()
        #d3.update(risposta0)
        #d3 = PyDict_Update(*risposta, *risposta0)
        return d3
    except TypeError:
        messaggio = 'Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'
        errore = {'mess': messaggio}
        return messaggio



app =Flask(__name__)
api = Api(app)

class Rec(Resource):
    app_id = "d735619c"
    app_key = "83413e2ddb14a5590908a339eb363622"
    da = "0"
    codice = 1

    if codice== 0:
        def recommender(self, ordinamento):

            if ordinamento == '1':
                nutriscore(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta)

            if ordinamento == '2':
                calorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta)

            if ordinamento == '3':
                etichette(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta)

            if ordinamento == '4':
                proteine(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta)

    if codice == 1:
        def get(self):
            fino = '100'
            key_word = request.args.get('q')
            etichette_salutari = request.args.get('health')
            tipo_pasto = request.args.get('dishType')
            tipo_dieta = request.args.get('diet')


            ordinamento = random.randint(0, 3)
            #ordinamento= 3
            app_id = "5b4aa300"
            app_key = "2a77a893f8a3def6264049423d208c06	"
            da = "0"


            if ordinamento == 0:
                risposta0 = anticalorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta,app_id, app_key, da)
                risposta = proteine(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                print(etichette_salutari)
                print(tipo_pasto)
                print(tipo_dieta)
                print(risposta)
                print(risposta0)
                res = merge(risposta, risposta0)
                print (res)
                print('ordinamento usato = proteine / anticalorie')

            if ordinamento == 1:
                risposta0 = anticalorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                risposta = calorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                print(etichette_salutari)
                print(tipo_pasto)
                print(tipo_dieta)
                print(risposta)
                print(risposta0)
                res = merge(risposta, risposta0)
                print (res)
                print('ordinamento usato = calorie / anticalorie')

            if ordinamento == 2:
                risposta0 = anticalorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                risposta = etichette(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                print(etichette_salutari)
                print(tipo_pasto)
                print(tipo_dieta)
                print(risposta)
                print(risposta0)
                res = merge(risposta, risposta0)
                print (res)
                print('ordinamento usato = etichette / anticalorie')

            if ordinamento == 3:
                risposta0 = anticalorie(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                risposta = nutriscore(key_word, fino, etichette_salutari, tipo_pasto, tipo_dieta, app_id, app_key, da)
                print(etichette_salutari)
                print(tipo_pasto)
                print(tipo_dieta)
                print(risposta)
                print(risposta0)
                res = merge(risposta, risposta0)
                print (res)
                print('ordinamento usato = nutriscore / anticalorie')


            return jsonify(res)






api.add_resource(Rec,'/rec/')

if __name__ == "__main__" :
    app.run(port=5028)
