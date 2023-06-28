$(document).ready(function () {

    // api del clima
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(ObtenerLocalizacion);
    }else{
        swal("Su navegador no soporta la geolocalización","Error","error");
    }

    function ObtenerLocalizacion(position){
        console.log(position.coords.latitude+ " - "+position.coords.longitude);

        
        $.get("https://api.open-meteo.com/v1/forecast?latitude="+position.coords.latitude+"&longitude="+position.coords.longitude+"&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m",function(data){

        $("#temperatura").html("La tempratura actual es:" + data["current_weather"]["temperature"]);
        $("#viento").html("La velocidad del viento actual es:" + data["current_weather"]["windspeed"]);
        });

        

    }


    $("#btnpagar").click(function (e) {
       
        if (validar() != "") {
            swal("Error de envio", validar(), "error");
        } else {
            swal("Datos enviados", "En brevedad nos contactaremos con usted", "success");
        }
        e.preventDefault();

    });
    



});
//Funcion que de validacion
function validar(){
    var html = "";
    var nombre = $("#Nombretxt").val();
    var Direccion = $("#Direcciontxt").val();
    var NumDepto = $("#NroDeptonum").val();
    var NumTarjata = $("#NroTarjetanum").val();
    
    if (nombre == "") {
        html += "- Debe Ingresar un Nombre \n";
    }
    if (Direccion == "") {
        html += "- Debe Ingresar un Correo \n";
    }

    if (NumDepto == "0") {
        html += "- Debe Seleccionar una Ciudad \n";
    }

    if (NumTarjata.trim().length < 16) {
        html += "- El numero de tarjeta es inferior a los 16 caracteres. \n";
    }
    

    


    return html;
    
}


