$(document).ready(function() {
    //additional script required for functioning of materialize elements
    $('.collapsible').collapsible();
    $(".button-collapse").sideNav();
    $('select').material_select();
    $('.modal').modal();
            
    //code below was provided in the code institue module
    //adding validation classes to materialise select
    validateMaterializeSelect();
    
    function validateMaterializeSelect(){
        let classValid = {"border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50"};
        let classInvalid = {"border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336"};
        //hide the select element physically but still keep it a part of the DOM
            if($("select.validate").prop("required")){
                $("select.validate").css({"display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute"});
            }
            $(".select-wrapper input.select-dropdown").on("focusin", function(){
                $(this).parent(".select-wrapper").on("change", function(){
                    if($(this).children("ul").children("li.selected:not(.disabled)").on("click", function(){})){
                        $(this).children("input").css(classValid); 
                    }
                });
            }).on("click", function(){
            if($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color")==="rgba(0,0,0,0.03)"){
                $(this).parent(".select-wrapper").children("input").css(classValid);
            }else{
                $(".select-wrapper input.select-dropdown").on("focusout", function(){
                    if($(this).parent(".select-wrapper").children("select").prop("required")){
                        if($(this).css("border-bottom")!="1px solid rgb(76, 175, 80)"){
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
            });
        }
    });
         
//function to add an input field for ingredients field
    function add_input_field_ingredients(){
        var new_input= document.createElement("div");
        new_input.innerHTML = '</br><div class="input-field col s9 m11"><input name="ingredients[]" type="text" class="validate" required></div>';
        document.getElementById("ingredients-div").appendChild(new_input);
    }
//function to add an input field for instructions field
    function add_input_field_instructions(){
        var new_input1= document.createElement("div");
        new_input1.innerHTML = '</br><div class="input-field col s9 m11"><input name="instructions[]" type="text" class="validate" required></div>';
        document.getElementById("instructions-div").appendChild(new_input1);    
    }
//function to add an input field for tools field
    function add_input_field_tools(){
        var new_input2= document.createElement("div");
        new_input2.class="row";
        new_input2.innerHTML = '<div class="input-field col s3"><input name="name[]" type="text" class="validate" required></div><div class="input-field col s8"><input name="link[]" type="text" class="validate" required></div>';
        document.getElementById("tools-div").appendChild(new_input2);
    }