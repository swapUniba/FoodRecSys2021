<!-- External CSS -->
        <link rel="stylesheet" href="../../stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Lato:300,400|Work+Sans:300,400,700" rel="stylesheet">

        <!-- CSS -->
       <link rel="stylesheet" href="../css/style.min.css">
       <link rel="stylesheet" href="../css/customcss.css">
       <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css"
        
        <script src="https://developer.edamam.com/attribution/badge.js"></script>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>


<style>
#main-container{
	display: flex;
	justify-content: center;
	width: 100%;
}
.card{
	background: white;
	width: 90% !important;
	border: 2px solid aliceblue;
	border-radius: 15px;
	margin: 20px;

}

.card-img-top{
	border-radius: 15px 15px 0px 0px;
	width: 100%;
	height: 300px;
	object-fit: contain;
}

.card-body{
	padding: 10px 20px;
}

.card-title{
	text-align: center;
	width: 100%;
	text-transform: uppercase;
	font-size: 18px;
}

.ingrediente{
	margin-bottom: 10px;
}

.cards-container{
	display: grid;
	grid-template-columns: 50% 50%;
}
</style>

<?php

session_start();
$key_word = $_POST["q"];
/*$tipo_dieta = $_POST["diet"];
$etichette_salutari = $_POST["labels"];*/
$tipo_pasto = $_POST["dishType"];







function createURL($key_word, $tipo_pasto){
    //$url = "http://localhost:5009/rec/?q=" . $key_word . '&';
    $url = "http://localhost:5028/rec/?q=" . $key_word .'&';

/*
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
*/  
    if($tipo_pasto == 'Starter')
    	$url = $url.'dishType=Starter&';
    if($tipo_pasto == 'Biscuits and cookies')
        $url = $url.'dishType=Biscuitsandcookies&';
    if($tipo_pasto == 'Bread')
        $url = $url.'dishType=Bread&';
    if($tipo_pasto == 'Cereals')
        $url = $url.'dishType=Cereals&';
    if($tipo_pasto == 'Condimentsandsauces')
        $url = $url.'dishType=Condimentsandsauces&';
    if($tipo_pasto == 'Desserts')
        $url = $url.'dishType=Desserts&';
    if($tipo_pasto == 'Egg')
        $url = $url.'dishType=Egg&';
    if($tipo_pasto == 'Main course')
        $url = $url.'dishType=Maincourse&';
    if($tipo_pasto == 'Omelet')
        $url = $url.'dishType=Omelet&';
    if($tipo_pasto == 'Pancake')
        $url = $url.'dishType=Pancake&';
    if($tipo_pasto == 'Preps')
        $url = $url.'dishType=Preps&';
    if($tipo_pasto == 'Preserve')
        $url = $url.'dishType=Preserve&';
    if($tipo_pasto == 'Salad')
        $url = $url.'dishType=Salad&';
    if($tipo_pasto == 'Sandwiches')
        $url = $url.'dishType=Sandwiches&';
    if($tipo_pasto == 'Soup')
        $url = $url.'dishType=Soup&';
    
    
    $url = $url . "n=10&lang=en";

    return $url;

}



$request = createURL($key_word, $tipo_pasto);
$response  = file_get_contents($request);
$jsonobj  = json_decode($response);
#var_dump($jsonobj); 
#echo($jsonobj->mess); 
$_SESSION['query1']=$key_word;
include ('header1.php');


function get_ingredients($ingredienti){
	$html = "";
	
	 for($i=0; $i<count($ingredienti);$i++){
	 	$html .=  "<div class='ingrediente'>- ".$ingredienti[$i]."</div>";
    }
return $html;
}

function get_ingredientsn($ingredientin){
	$html = "";
	
	 for($i=0; $i<count($ingredientin);$i++){
	 	$html .=  "<div class='ingrediente'>- ".$ingredientin[$i]."</div>";
    }
return $html;
}



if ($jsonobj =='Non è stato possibile raccomandare nessuna ricetta mediante la parola chiave espressa'){
	$html = "<div id='main-container'><div class='cards-container'>";
	$risperror = "<b>OPS...NON E' STATO POSSIBILE RACCOMANDARE NESSUNA RICETTA</b>";
	$html.='<div class="card" style="width: 1000px !important;">
	<div class="card-body">
		<p class="card-text">'.$risperror.'</p>
	</div>
	<div class="col md-1 text-center button-container"> 
        <a href="../html/debugform.html" class="link-button">COME BACK</a> 
    </div>
</div>';
    echo($html);
}
 else{
    $etichetta = ($jsonobj->etichetta);
    $etichettan = ($jsonobj->etichettan);
	$ingredienti =  get_ingredients($jsonobj->ingredients);
    $ingredientin = get_ingredients($jsonobj->ingredientsn);
    $html = "<div id='main-container'><div class='cards-container'>";
	$random = rand(0,1);
                 if($random == '1')
                    { $html .= ' 
            <div class="card" style="width: 18rem;">
              <p class="card-text" style="background-color:green; text-align:center"><b>'.$etichetta.'</b></p>
			  <img src="'.$jsonobj->imageURL.'" class="card-img-top" alt="...">
			  <div class="card-body">
			    <h5 class="card-title">'.$jsonobj->name.'</h5>
			    <p class="card-text">'.$ingredienti.'</p>
			  </div>
			</div>
            <div class="card" style="width: 18rem;">
               <p class="card-text"  style="text-align:center; background-color:red"><b>'.$etichettan.'</b></p>
              <img src="'.$jsonobj->imageURLn.'" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">'.$jsonobj->namen.'</h5>
                <p class="card-text">'.$ingredientin.'</p> 
              </div>
            </div>';     
		 } else{
            $html .= '  
            <div class="card" style="width: 18rem;">
              <img src="'.$jsonobj->imageURL.'" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">'.$jsonobj->name.'</h5>
                <p class="card-text">'.$ingredienti.'</p>
              </div>
            </div>
            <div class="card" style="width: 18rem;">
              <img src="'.$jsonobj->imageURLn.'" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">'.$jsonobj->namen.'</h5>
                <p class="card-text">'.$ingredientin.'</p> 
              </div>
            </div>';
            };


        
		$html .= "</div></div>";
         
        #include("questionnaire.php?keyw=$key_word&recipes=$ricettas&reciped=$ricettad");
        $html .=' 
                     <div class="col md-1 text-center button-container"> 
                            
                                <a href="../html/debugform.html" class="link-button">Continue</a> 

                            </div>
';
        echo($html);
        /*$bottone= '
        <div class="col md-1 text-center button-container"> 
        <a href="../html/form2.html" class="link-button">Continue</a> 
        </div>';
        echo($bottone);
        */include("footer.php");
        }#giusto, ricordati di fare altro ciclo per gli altri ingredienti e poi modificare le altre funzioni python per test generale





?>