
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>FoodRecSys</title>
        <meta name="description" content="Core HTML Project">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- External CSS -->
        <link rel="stylesheet" href="../../stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Lato:300,400|Work+Sans:300,400,700" rel="stylesheet">

        <!-- CSS -->
        <link rel="stylesheet" href="../css/style.min.css">
        <link rel="stylesheet" href="../css/customcss.css">

    </head>
<div class="boxed-page">
            <nav id="gtco-header-navbar" class="navbar">
                <div class="container" >
                    <span class="navbar-brand">
                        <img src="../icons/icon3.png" width="80" height="80" class="d-inline-block align-top" alt="">
                        <a href="../html/index.html">FOOD RECOMMENDATIONS </a>
                    </span>
                </div>
            </nav>
<section id="gtco-single-content" class="bg-white">

        <div class="container">
            <div class="section-content blog-content">
            
                <!-- Section Title -->
                <div class="title-wrap">
                    <h2 class="section-title">Thank you!</h2>
                    <p class="section-sub-title">The experiment is ended, enjoy your meal! &#x1F355;</p>

                    <?php
                    include "quest_dolce.php";
                    echo "This is the code to complete your experiment:<br />".$_SESSION['randomNumber'];
                    session_destroy();
                    ?>
                </div>
                <!-- End of Section Title -->
                <div class="col md-1 text-center button-container">
                    <a href="../html/index.html">
                         <div class="col-md-8 offset-md-2 form-btn text-center">
                                <button id="btnForm" class="btn btn-block btn-secondary btn-red col-md-4 offset-md-4 " type="submit" name="submit" >Exit</button>
                    </a>
                </div>
            </div>
        </div>
        <footer class="mastfoot mb-3 bg-white py-4 border-top">
    <div class="inner container">
        <div class="row">
            <div class="col-md-6 d-flex">
                <span> &copy; 2020 <a href="http://www.di.uniba.it/~swap/" target="_blank"> SWAP Research Group </a>,</span>
                <span>&nbsp;<a href="privacy.html" target="_blank">Privacy Policy </a></span>
            </div>
            <div class="col-md-6 d-flex flex-row-reverse ">
                <span> &copy; Developed by <a href="https://github.com/serino28" target="_blank">Antonio Serino</a></span>
        </div>
    </div>
</footer>
    </section>
