<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>FoodRecSys</title>
    <meta name="description" content="Core HTML Project">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- External CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400|Work+Sans:300,400,700" rel="stylesheet">

    <!-- CSS -->
    <link rel="stylesheet" href="css/style.min.css">
     <link rel="stylesheet" href="css/customcss.css">

</head>
<body data-spy="scroll" data-target="#navbar-nav-header" class="single-layout">
<div class="boxed-page">
    <nav id="gtco-header-navbar" class="navbar">
        <div class="container" >
                    <span class="navbar-brand">
                        <img src="icons/icon3.png" width="80" height="80" class="d-inline-block align-top" alt="">
                        <a href="html/index.html">FOOD RECOMMENDATIONS </a>
                    </span>
        </div>
    </nav>
    <section id="gtco-single-content" class="bg-white">
        <div class="container">
            <div class="section-content blog-content">

                <!-- Section Title -->
                <div class="title-wrap">
                    <h2 class="section-title">Profile builder</h2>
                    <p class="section-sub-title">Please answer the following questions</p>

                </div>
                <!-- End of Section Title -->

                <div class="row mx-auto">
                    <!-- form -->
                    <div class="col-md-10 offset-md-1 contact-form-holder mt-4">
                        <form id="form" method="post" action="dati.php">
                            
                            <div class="form-group row">
                                <label for="altezza">Height: </label>
                                <div class="col-sm-3">
                                    <div class="form-check form-check-inline">
                                        <input type="number" step="1" name="altezza" id="altezza" required>
                                        <label> cm </label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="peso">Weight: </label>
                                <div class="col-sm-3">
                                    <div class="form-check form-check-inline">
                                        <input type="number" step="1" name="peso" id="peso" required>
                                        <label> Kg </label>
                                    </div>
                                </div>
                            </div>



                            <!--tipo di dieta-->

                            <div class="form-group row">
                                <label for="sesso"> sex: </label>
                                <div class="col-sm-2">
                                    <select id="sesso" name="sesso" required>
                                        <option hidden disabled selected value></option>
                                        <option value="Male"> M </option>
                                        <option value="Female"> F </option>
                                        <option value="/"> / </option>
                                    </select>
                                </div>

                            </div>
                            <div class="form-group row">
                                <label for="age"> age: </label>
                                <div class="col-sm-2">
                                    <select id="age" name="age" required>
                                        <option hidden disabled selected value></option>
                                        <option value="16-19"> 16-19 </option>
                                        <option value="20-25"> 20-25 </option>
                                        <option value="26-30"> 26-30 </option>
                                        <option value="31-40"> 31-40 </option>
                                        <option value="41-59"> 41-59 </option>
                                        <option value="60+"> 60+ </option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="occupationSelector">Employment:</label>
                                <div class="col-sm-4">
                                    <select class="form-control" id="occupationSelector" name="occupation" required>
                                        <option hidden disabled selected value></option>
                                        <option>Student</option>
                                        <option>Private company staff</option>
                                        <option>Public company staff</option>
                                        <option>Self employed</option>
                                        <option>Unemployed</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="sport"> weekly sport activity: </label>
                                <div class="col-sm-2">
                                    <select id="sport" name="sport" required>
                                        <option hidden disabled selected value></option>
                                        <option value="0"> nothing </option>
                                        <option value=" 1 time at week"> 1 time </option>
                                        <option value="2-3 times at week"> 2-3 times </option>
                                        <option value="4-5 times at week"> 4-5 times </option>
                                        <option value="more of 5 times at week"> More of 5 </option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="websiteUsageSelector">Recipe website usage:</label>
                                <div class="col-sm-5">
                                    <select class="form-control" id="websiteUsageSelector" name="websiteUsage" required>
                                        <option hidden disabled selected value></option>
                                        <option value='daily'>Daily</option>
                                        <optio value='weekly'>Weekly</option>
                                        <option value='monthly'>Monthly</option>
                                        <option value='rarely'>Rarely</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group row ">
                                <label for="exp"> Cooking experience:</label>
                                <div class="col-sm-7">
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="exp" id="1" value="1" required>
                                        <label class="form-check-label" for="1">Very low</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="exp" id="2" value="2" required>
                                        <label class="form-check-label" for="2">Low</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="exp" id="3" value="3" required>
                                        <label class="form-check-label" for="3">Medium</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="exp" id="4" value="4" required>
                                        <label class="form-check-label" for="4">High</label>
                                    </div>
                                    <div class="form-check form-check-inline">
                                        <input class="form-check-input" type="radio" name="exp" id="5" value="5" required>
                                        <label class="form-check-label" for="5">Very High</label>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="goalSelector" >What is your goal?</label>
                                <div class="col-sm-5">
                                    <select class="form-control" id="goalSelector" name="goal" required>
                                        <option hidden disabled selected value></option>
                                        <option value='lose weight'>Lose weight</option>
                                        <option value='gain weight'>Gain weight</option>
                                        <option value='No goals'>No goals</option>
                                    </select>
                                </div>
                            </div>
                             <div class="form-group row">
                                    <label class="col-form-label">In your opinion, to have a healthy lifestyle is:</label>
                                       <div class="col-sm-6">
                                           <select class="form-control" id="HLselector" name="HS">
                                               <option hidden disabled selected value></option>
                                               <option>Not important</option>
                                               <option>Poorly important</option>
                                               <option>Important</option>
                                               <option>Very important</option>
                                           </select>
                                       </div>
                                   </div>

                            <div class="form-group row">
                                    <label class="col-form-label">How do you consider your lifestyle:</label>
                                       <div class="col-sm-6">
                                           <select class="form-control" id="HCselector" name="HC">
                                               <option hidden disabled selected value></option>
                                               <option>Absolutely not healthy</option>
                                               <option>Not healthy</option>
                                               <option>Quite healty</option>
                                               <option>Healty</option>
                                               <option>Very healty</option>
                                           </select>
                                       </div>
                                   </div>

                            





                            <input type="hidden" name="dish" id="hiddenField" value="main" />

                            <br>
                            <div class="col-md-8 offset-md-2 form-btn text-center">
                                <button id="btnForm" class="btn btn-block btn-secondary btn-red col-md-4 offset-md-4 " type="submit" name="submit" >Build Profile</button>
                                <small id="disclaimer" class="form-text text-muted">We'll use this data only for the purpose of the experiment</small>
                            </div>
                        </form>

                    </div>
                </div>
            </div>
        </div>
    </section>
    <footer class="mastfoot mb-3 bg-white py-4 border-top">
        <div class="inner container">
            <div class="row">
                <div class="col-md-6 d-flex">
                    <span> &copy; 2019 <a href="http://www.di.uniba.it/~swap/" target="_blank"> SWAP Research Group </a>,</span>
                    <span>&nbsp;<a href="html/privacy.html" target="_blank">Privacy Policy </a></span>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse  ">
                    <span>Developed by <a href="https://github.com/serino28" target="_blank">Antonio Serino</a> &amp; <a href="https://github.com/cataldomusto" target="_blank">Cataldo Musto</a></span>                        </div>
            </div>
        </div>
    </footer>
</div>

<!-- External JS -->
<script src="../../code.jquery.com/jquery-3.3.1.min.js" ></script>
<script src="../../cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="../../stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>

<!-- Mirrored from 90.147.102.243:8080/foodrecsys/form.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 21 Feb 2020 12:25:42 GMT -->
</html>