<?php
include "myrror/json_read.php";
function getLogData(){
    $param = "";
    $json_data = queryMyrror($param);
    $data = getMyrrorData($json_data);

    return $data;
}
$key_word = $_POST['q'];
$tipo_dieta = $_POST['diet'];
$etichette_salutari = $_POST['labels'];
$tipo_pasto = $_POST['meal'];

function createURL_old($key_word, $tipo_dieta, $etichette_salutari, $tipo_pasto){
    $url = "http://localhost:5009/rec/?q=" . $key_word . '&';

    if($tipo_dieta == 'balanced')
        $url = $url . "diet=balanced&";
    if($tipo_dieta == 'high-protein')
        $url = $url . "diet=high-protein&";
    if($tipo_dieta == 'high-fiber')
        $url = $url . "diet=high-fiber&";
    if($tipo_dieta == 'low-carb')
        $url = $url . "diet=low-carb&";
    if($tipo_dieta == 'low-fat')
        $url = $url . "diet=low-fat&";
    if($tipo_dieta == 'low-sodium')
        $url = $url . "diet=low-sodium&";

    if($etichette_salutari == 'vegan')
        $url = $url . "health=vegan&" ;
    if($etichette_salutari == 'vegetarian')
        $url = $url . "health=vegetarian&" ;
    if($etichette_salutari == 'egg-free')
        $url = $url . "health=egg-free&" ;
    if($etichette_salutari == 'fish-free')
        $url = $url . "health=fish-free&" ;
    if($etichette_salutari == 'gluten-free')
        $url = $url . "health=gluten-free&" ;

    if($tipo_pasto == 'Breakfast')
        $url = $url.'mealType=Breakfast&';
    if($tipo_pasto == 'Launch')
        $url = $url.'mealType=Launch&';
    if($tipo_pasto == 'Dinner')
        $url = $url.'mealType=Dinner&';
    if($tipo_pasto == 'Sneak')
        $url = $url.'mealType=Sneak&';
    if($tipo_pasto == 'Teatime')
        $url = $url.'mealType=Teatime&';

    $url = $url . "n=10&lang=en";

    return $url;

}

function getRecipes($pers_url_new, $pers_url_old)
{
    $rec_1 = 2;
    $rec_2 = 0;

    $pers_url_1 = $pers_url_new;
    $pers_url_2 = "http://localhost:5009/mood/?n=10&lang=en";
    $pers_data_primo_1 = performRequest(($pers_url_1), $rec_1);
    $pers_data_primo_2 = performRequest(($pers_url_2), $rec_2);

    $pers_data_secondo_1 = performRequest(($pers_url_1), $rec_1);
    $pers_data_secondo_2 = performRequest(($pers_url_2), $rec_2);

    $pers_data_dolce_1 = performRequest(($pers_url_1), $rec_1);
    $pers_data_dolce_2 = performRequest(($pers_url_2), $rec_2);
    return array(
        "personalized_main_1" => $pers_data_primo_1,
        "personalized_main_2" => $pers_data_primo_2,
        "personalized_second_1" => $pers_data_secondo_1,
        "personalized_second_2" => $pers_data_secondo_2,
        "personalized_dessert_1" => $pers_data_dolce_1,
        "personalized_dessert_2" => $pers_data_dolce_2,
        "rec_1" => $rec_1,
        "rec_2" => $rec_2);
}
function performRequest($url, $typeRecommendation){
    /*
    se il valore di $typeRecommendation è 0 allora è stato utilizzato il sistema di raccomandazione popolare
    se il valore di $typeRecommendation è 1 allora è stato utilizzato il sistema di raccomandazione precedente (run on 5002)
    se il valore di $typeRecommendation è 2 allora è stato utilizzato il sistema di raccomandazione attuale (run on 5009)
    */
    $top = 0; //indica la ricetta restituita, se 0 => top-1

    /*
     * Se si tratta della ricetta consigliata con il sistema popolare ($typeRecommendation = 0) restituiamo una random tra le top-5 per diversificare
     * Se si tratta della ricetta consigliata dal recommender ($typeRecommendation = 1 o 2) restituiamo la top-1
     */
    if ($typeRecommendation == 0)
    {
        $top = rand(0, 4);
    }

    ///  Initiate curl
    $ch = curl_init();
    // Will return the response, if false it print the response
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    // Set the url
    curl_setopt($ch, CURLOPT_URL, $url);
    // Execute
    $result=curl_exec($ch);
    // Closing
    curl_close($ch);

    //sostituisco \" con " e \\ con \ nel risultato, poi elimino il primo carattere (") e gli ultimi due ("\n)
    //$result = str_replace("\\", "", "$result");
    $result = str_replace('\\"', "\"", "$result");
    $result = str_replace('\\\\', "\\", "$result");
    $result = substr($result, 1);
    $result = substr_replace($result ,"", -2);
    //echo $result;

    //vado a decodificare il json e lo metto in un array
    $arr = json_decode($result,true);

    //salvo il nome della ricetta, l'url dell'immagine e gli altri elementi da restituire
    if(!empty($arr["dict"])) {
        $name = $arr["dict"]["name"];
        $imageURL = $arr["dict"]["imageURL"];
        $ingredients = $arr["dict"]["ingredients"];
        $url = $arr["dict"]["url"];


        return array("name" => $name, "imgURL" => $imageURL, "ingredients" => $ingredients,  "url" => $url);
    }
    else{
        return array("name" => "Purtroppo non ho trovato nessuna ricetta &#x1f60c");
    }
}
