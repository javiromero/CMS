/***
 * 
 * Funciones Javascript:
 *      Validación de formulario rápido
 *      Envío ajax de formulario rápido
 *      Llenado de datos por defecto del formulario rápido
 * 
 * **/

function isValidEmailAddress(email){
    var RegExp = /^((([a-z]|[0-9]|!|#|$|%|&|'|\*|\+|\-|\/|=|\?|\^|_|`|\{|\||\}|~)+(\.([a-z]|[0-9]|!|#|$|%|&|'|\*|\+|\-|\/|=|\?|\^|_|`|\{|\||\}|~)+)*)@((((([a-z]|[0-9])([a-z]|[0-9]|\-){0,61}([a-z]|[0-9])\.))*([a-z]|[0-9])([a-z]|[0-9]|\-){0,61}([a-z]|[0-9])\.)[\w]{2,4}|(((([0-9]){1,3}\.){3}([0-9]){1,3}))|(\[((([0-9]){1,3}\.){3}([0-9]){1,3})\])))$/
    if(RegExp.test(email)){
        return true;
    }else{
        return false;
    }
}

function validate_rapido(){
    var chk     = true;
    var Tname   = $(".contacto_rapido #id_nombre").val();
    var Tphone  = $(".contacto_rapido #id_telefono").val();
    var Temail  = $(".contacto_rapido #id_email").val();
    var Tmsg    = $(".contacto_rapido #id_mensaje").val();
    var Tcond   = $(".contacto_rapido #id_condiciones").val();
    
    $("#contacto_thanks").hide();

    if(Tname=='' || Tname=='Nombre')
    {
        $(".contacto_rapido #id_nombre").css({'border':'1px solid red'});
        chk = false
    } else {
        $(".contacto_rapido #id_nombre").css({'border':'0px'});
    }
    if(Tphone=='' || Tphone=='Teléfono')
    {
        $(".contacto_rapido #id_telefono").css({'border':'1px solid red'});
        chk = false
    } else {
        $(".contacto_rapido #id_telefono").css({'border':'0px'});
    }
    if(Tmsg=='' || Tmsg=='Me gustaría saber más información acerca de...')
    {
        $(".contacto_rapido #id_mensaje").css({'border':'1px solid red'});
        chk = false
    }   else {
        $(".contacto_rapido #id_mensaje").css({'border':'0px'});
    }                       
    if(Temail=="" || Temail=='Correo Electrónico')
    {
        $(".contacto_rapido #id_email").css({'border':'1px solid red'});
        chk = false
    }else{
        if(!isValidEmailAddress(Temail))
        {
                $(".contacto_rapido #id_email").css({'border':'1px solid red'});
                chk = false
        } else {
            $(".contacto_rapido #id_email").css({'border':'0px'});
        }
    }
    if($(".contacto_rapido #id_condiciones").attr("checked") != true)
    {
        $(".contacto_rapido #label_condiciones").css({'border':'1px solid red'});
        chk = false
    } else {
        $(".contacto_rapido #label_condiciones").css({'border':'0px'});
    }
    
    if(chk ==  true){
        $(".contacto_rapido").hide();
        $(".contacto_thanks").show();
        $(".contacto_rapido").submit();
//         $.post(".",
//                { nombre: Tname, email: Temail, telefono: Tphone, mensaje: Tmsg, condiciones: Tcond},
//                function(data) {});
    }
}

function validate_contact(){
    var chk     = true;
    var Tname   = $(".contact #id_nombre").val();
//     var Tphone  = $(".contact #id_telefono").val();
    var Temail  = $(".contact #id_email").val();
    var Tmsg    = $(".contact #id_mensaje").val();
    var Tcond   = $(".contact #id_condiciones").val();
    
    if(Tname=='' || Tname=='Nombre')
    {
        $(".contact #id_nombre").css({'border':'1px solid red'});
        chk = false
    } else {
        $(".contact #id_nombre").css({'border':'1px solid #FE481A'});
    }
//     if(Tphone=='' || Tphone=='Teléfono')
//     {
//         $(".contact #id_telefono").css({'border':'1px solid red'});
//         chk = false
//     } else {
//         $(".contact #id_telefono").css({'border':'1px solid #FE481A'});
//     }
    if(Tmsg=='' || Tmsg=='Me gustaría saber más información acerca de...')
    {
        $(".contact #id_mensaje").css({'border':'1px solid red'});
        chk = false
    }   else {
        $(".contact #id_mensaje").css({'border':'1px solid #FE481A'});
    }                       
    if(Temail=="" || Temail=='Correo Electrónico')
    {
        $(".contact #id_email").css({'border':'1px solid red'});
        chk = false
    }else{
        if(!isValidEmailAddress(Temail))
        {
                $(".contact #id_email").css({'border':'1px solid red'});
                chk = false
        } else {
            $(".contact #id_email").css({'border':'1px solid #FE481A'});
        }
    }
    if($(".contact #id_condiciones").attr("checked") != true)
    {
        $(".contact #label_condiciones").css({'border':'1px solid red'});
        chk = false
    } else {
        $(".contact #label_condiciones").css({'border':'0px'});
    }
        
    if(chk ==  true){
        $(".contact").submit();
//         $.post(".",
//                { nombre: Tname, email: Temail, telefono: Tphone, mensaje: Tmsg, condiciones: Tcond},
//                function(data) {});
    }
}

function clearTextName(thefield){
    if (thefield.defaultValue==thefield.value){
    thefield.value = ""}
    if (thefield.value=='Nombre'){
    thefield.value = ""}
}
function setTextName(thefield){
    if (thefield.value=='')
    thefield.value = 'Nombre'
}

function clearTextEmail(thefield){
    if (thefield.defaultValue==thefield.value){
    thefield.value = ""}
    if (thefield.value=='Correo Electrónico'){
    thefield.value = ""}
}
function setTextEmail(thefield){
    if (thefield.value=='')
    thefield.value = 'Correo Electrónico'
}
function clearTextPhone(thefield){
    if (thefield.defaultValue==thefield.value){
    thefield.value = ""}
    if (thefield.value=='Teléfono'){
    thefield.value = ""}
}
function setTextPhone(thefield){
    if (thefield.value=='')
    thefield.value = 'Teléfono'
}
function clearTextMsg(thefield){
    if (thefield.defaultValue==thefield.value){
    thefield.value = ""}
    if (thefield.value=='Me gustaría saber más información acerca de...'){
    thefield.value = ""}
}
function setTextMsg(thefield){
    if (thefield.value=='')
    thefield.value = 'Me gustaría saber más información acerca de...'
}