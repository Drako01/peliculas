/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*..............................................................................................
... TODOS LOS CURSOS .............................................................
............................................................................................. */
$( "#boton_prod" ).click(function(){
	valor = $( "#id_querycom" ).val();
	respuestproducto(valor)
});

function respuestproducto(valor){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/vistaprevia/buscar_libro2/",
		type : "GET",
		data : { valor : valor,},
		success : function(json){

            valor_retornado = "<h2 style='text-align:center;'>"+json[0].producto+"</h2>"+ "<img style='width:100%;' src='/media/" + json[0].ruta_imagen + "'/>"



            $('#contenedor_filtrado').html(valor_retornado);
            console.log(json[0].producto);

		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
}
