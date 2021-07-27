<div class="form-group row">
    <div class="col-lg-6">
        <label class="question" for="Q1">Given the current information, which recipe you choose?</label>
    </div>
    <div class="col-lg-6">
      <form id="form0" method="post" action="../php/quest_dolce.php/?keyw=$key_word&recipes=$ricettas&reciped=$ricettad&sinistraord=$ordinamentos&destraord=$ordinamentod">
        <select class="form-control" id="Q1" name="Q1" required onchange="dynamicForm()">
            <!--<option hidden disabled selected value></option>-->
            <option hidden selected></option>
            <option value="left">Left side recipe</option>
            <option value="none">None of these two</option>
            <option value="right">Right side recipe</option>
        </select>
        <div class="col md-1 text-center button-container">
        <button id="btnForm" class="link-button" type="submit" name="submit">Continue</button>                        
        </div> 
    </form>
    </div>
</div>

