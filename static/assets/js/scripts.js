
function scroll_to_class(element_class, removed_height) {
	var scroll_to = $(element_class).offset().top - removed_height;
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 0);
	}
}
function bar_progress(progress_line_object, direction) {
	var number_of_steps = progress_line_object.data('number-of-steps');
	var now_value = progress_line_object.data('now-value');
	var new_value = 0;
	if(direction == 'right') {
		new_value = now_value + ( 100 / number_of_steps );
	}
	else if(direction == 'left') {
		new_value = now_value - ( 100 / number_of_steps );
	}
	progress_line_object.attr('style', 'width: ' + new_value + '%;').data('now-value', new_value);
}


jQuery(document).ready(function() {
    /*
        Fullscreen background
    */
    $.backstretch("../../../static/assets/img/backgrounds/3.jpg");

    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("cover");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("cover");
    });

    /*
        Form
    */
    $('.f1 fieldset:first').fadeIn('slow');

    $('.f1 input[type="text"],.f1 input[type="number"], .f1 input[type="email"],select,.f1 input[type="password"], .f1 textarea').on('focus', function() {
    	$(this).removeClass('input-error');


    });

    // next step
    $('.f1 .btn-next').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;

        // validate edad alumno a inscribir

        var fecha=document.getElementById("id_fecha_de_nacimiento").value;
        // Si la fecha es correcta, calculamos la edad
        var values=fecha.split("-");
        var dia = values[2];
        var mes = values[1];
        var ano = values[0];

        // cogemos los valores actuales
        var fecha_hoy = new Date();
        var ahora_ano = fecha_hoy.getYear();
        var ahora_mes = fecha_hoy.getMonth()+1;
        var ahora_dia = fecha_hoy.getDate();

        // realizamos el calculo
        var edad = (ahora_ano + 1900) - ano;
        if ( ahora_mes < mes )
        {
            edad--;
        }
        if ((mes == ahora_mes) && (ahora_dia < dia))
        {
            edad--;
        }
        if (edad > 1900)
        {
            edad -= 1900;
        }


    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
    	// fields validation
    	parent_fieldset.find('input[type="text"], input[type="password"],input[type="number"],input[type="email"],select, textarea').each(function() {
            //var estado_civil = document.getElementById('id_estado_civil')
            if($(this).value == ''){
                $(this).addClass('input-error');
                next_step = false;

            }
            if (form.cedula.value <99999){
                $(cedulaale).removeClass('hidden');
                $(form.cedula).addClass('input-error');
                document.getElementById('cedulaale').innerHTML="CEDULA INVALIDA, INTRODUZCA UN MINIMO DE 7 CARACTERES";
                next_step = false;
                
            }
            

            
            
            if(form.nombre.value.length<3){
                $(nombreale).removeClass('hidden');
                $(form.nombre).addClass('input-error');
                document.getElementById('nombreale').innerHTML="NOMBRE INVALID0, INTRODUZCA UN MINIMO DE 3 CARACTERES";
                next_step = false;

            }
            if(form.apellido.value.length<3 ){
                $(apellidoale).removeClass('hidden');
                $(form.apellido).addClass('input-error');
                document.getElementById('apellidoale').innerHTML="APELLIDO INVALID0, INTRODUZCA UN MINIMO DE 3 CARACTERES";
                next_step = false;
            }

            if(form.celular_number.value.length<7 && form.celular_number.value.length>1 ){
                $(number1).removeClass('hidden');
                $(form.celular).addClass('input-error');
                $(form.celular_number).addClass('input-error');
                document.getElementById('number1').innerHTML="NUMERO INVALID0, INTRODUZCA UN MINIMO DE 7 CARACTERES";
                next_step = false;
            }

            if(form.telefono_residencial.value.length<13 && form.telefono_residencial.value.length>1 ){
                $(residencial).removeClass('hidden');
                $(form.telefono_residencial).addClass('input-error');
                document.getElementById('residencial').innerHTML="NUMERO INVALID0, INTRODUZCA UN MINIMO DE 11 CARACTERES";
                next_step = false;
            }

            if(form.telefono_residencial.value.length==13){
                $(residencial).addClass('hidden');
                $(form.telefono_residencial).removeClass('input-error');

            }
            if(form.celular_number.value.length==8 ){
                $(number1).addClass('hidden');
                $(form.celular_number).removeClass('input-error');
            }
            if(form.celular.value == 0 && form.celular_number.value.length>1 ){
                $(number1).removeClass('hidden');
                $(form.celular).addClass('input-error');

                document.getElementById('number1').innerHTML="DEBE COLOCAR UN CODIGO DE AREA VALIDO";
                next_step = false;
            }

            if(form.celular.value.length>1 && form.celular_number.value == 0 ){
                $(number1).removeClass('hidden');
                $(form.celular).addClass('input-error');

                document.getElementById('number1').innerHTML="INTRODUZCA UN NUMERO";
                next_step = false;
            }

            if(edad <= 15 ){
                $(fecha_naci).removeClass('hidden');
                $(form.fecha_de_nacimiento).addClass('input-error');
                document.getElementById('fecha_naci').innerHTML="NO POSEE LA EDAD ADECUADA PARA INSCRIBIRSE";
                next_step = false;
            }

            if(edad > 15 ){
                $(fecha_naci).addClass('hidden');
                $(form.fecha_de_nacimiento).removeClass('input-error');
            }

            if(form.fecha_de_nacimiento.value == 0 ){
                $(fecha_naci).removeClass('hidden');
                $(form.fecha_de_nacimiento).addClass('input-error');
                document.getElementById('fecha_naci').innerHTML="INTRODUZCA UNA FECHA VALIDA";
                next_step = false;
            }

            if(form.sexo.value == 0 ){
                $(sexo).removeClass('hidden');
                $(form.sexo).addClass('input-error');
                document.getElementById('sexo').innerHTML="INTRODUZCA UN VALOR VALIDO";
                next_step = false;
            }

            if(form.sexo.value != 0 ){
                $(sexo).addClass('hidden');
                $(form.sexo).removeClass('input-error');
            }

            if(form.direccion.value.length<8 ){
                $(direccion).removeClass('hidden');
                $(form.direccion).addClass('input-error');
                document.getElementById('direccion').innerHTML="INTRODUZCA UN MINIMO DE 8 CARACTERES";
                next_step = false;
            }
            if(form.direccion.value.length>=8 ){
                $(direccion).addClass('hidden');
                $(form.direccion).removeClass('input-error');
            }

            if(form.nombre.value.length>=3 ){
                $(nombreale).addClass('hidden');
            }

            if(form.apellido.value.length>=3 ){
                $(apellidoale).addClass('hidden');
            }

            if(form.cedula.value > 999999 ){
                $(cedulaale).addClass('hidden');
            }
            else {
                $(this).removeClass('input-error');
            }
            //validacion con msj de correo electronico
            object=document.getElementById("id_email");
            valueForm=object.value;

            // Patron para el correo
            var patron=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
            if(valueForm.search(patron)==0)
            {
                //Mail correcto
                $(email1).addClass('hidden');
                $(form.email).removeClass('input-error');
            }
            else {
                $(email1).removeClass('hidden');
                $(form.email).addClass('input-error');
                document.getElementById('email1').innerHTML="CORREO ELECTRONICO INVALIDO";
                next_step = false;
                
            }

            
            //Mail incorrecto

    	}
        );
    	// fields validation
    	if( next_step ) {
    		parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$(this).next().fadeIn();
	    		// scroll window to beginning of the form
    			scroll_to_class( $('.f1'), 20 );
	    	});
    	}

    });

    // previous step
    $('.f1 .btn-previous').on('click', function() {
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');

    	$(this).parents('fieldset').fadeOut(400, function() {
    		// change icons
    		current_active_step.removeClass('active').prev().removeClass('activated').addClass('active');
    		// progress bar
    		bar_progress(progress_line, 'left');
    		// show previous step
    		$(this).prev().fadeIn();
    		// scroll window to beginning of the form
			scroll_to_class( $('.f1'), 20 );
    	});
    });

    // submit
        // fields validation

   

});




function maxLengthCheck(object)
  {
    if (object.value.length > object.maxLength)
      object.value = object.value.slice(0, object.maxLength)
  }
$(window).scroll(function() {
    if ($("#menu").offset().top > 56) {
        $("#menu").removeClass("navbar-no-bg");
        $("#menu").addClass("bg-primary");
    } else {
        $("#menu").removeClass("bg-primary");
        $("#menu").addClass("navbar-no-bg");
    }
});
$(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

function text(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true;
    patron =/[A-Za-z- ]/;
    te = String.fromCharCode(tecla);
    return patron.test(te);
}

function texto(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true;
    patron =/[ivx]/;
    te = String.fromCharCode(tecla);
    return patron.test(te);
}
$(".alert").alert()

function showDiv(select){
   if(select.value== 'si'){
    document.getElementById('hidden_div1').style.display = "block";
    document.getElementById('hidden_div2').style.display = "block";

   } if(select.value== 'no'){
    document.getElementById('hidden_div1').style.display = "none";
    document.getElementById('hidden_div2').style.display = "none";

   }
}
function submitform(){
    buscar.submit();
}



$('#form1').submit(function(e){
    var next_step1 = true;
    var telefono = document.getElementById('id_telefono_profesor')

    if (telefono.value.length!=11){
        $(telefono_profesor).removeClass('hidden');
        $(telefono).addClass('input-error');
        document.getElementById('telefono_profesor').innerHTML="NUMBERO DE TELEFONO INVALIDO";
        e.preventDefault()
        next_step = false;
    }
    if(telefono.value.length == 0 ){
        $(telefono_profesor).addClass('hidden');
        $(telefono).removeClass('input-error');

    }});

$('.btn-next1').on('click', function() {
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        var ingreso = document.getElementBy('id_ing_famil')
        if (ingreso.value.length <3){
            $(ingresoale).removeClass('hidden');
            $(ingreso).addClass('input-error');
            document.getElementById('ingresoale').innerHTML="INGRESO INVALIDO, INTRODUZCA UN MINIMO DE 4 CARACTERES";
            next_step = false;
            e.preventDefault()
        }
    });



$('#form').submit(function(e){
    var next_step1 = true;
    var nombre = document.getElementById('id_first_name')
    var cedula = document.getElementById('id_ci')
    var apellido = document.getElementById('id_last_name')

    $('.f1').find('input[type="text"], input[type="password"],input[type="number"],input[type="email"],select, textarea').each(function() {
       if ( $(this).val() == '') {
            e.preventDefault()
            $(this).addClass('input-error')
       }

       if (cedula.value <99999){
            $(cedulaale).removeClass('hidden');
            $(cedula).addClass('input-error');
            document.getElementById('cedulaale').innerHTML="CEDULA INVALIDA, INTRODUZCA UN MINIMO DE 7 CARACTERES";
            next_step = false;
                
            }
        if(cedula.value > 999999 ){
            $(cedulaale).addClass('hidden');
            $(cedula).removeClass('input-error');

            }
        if (nombre.value.length <3){
            $(nombreale).removeClass('hidden');
            $(nombre).addClass('input-error');
            document.getElementById('nombreale').innerHTML="NOMBRE INVALIDO, INTRODUZCA UN MINIMO DE 3 CARACTERES";
            next_step = false;
        }
        if(nombre.value.length >3){
            $(nombreale).addClass('hidden');
            $(nombre).removeClass('input-error');
        }
        if (apellido.value.length <3){
            $(apellidoale).removeClass('hidden');
            $(nombre).addClass('input-error');
            document.getElementById('apellidoale').innerHTML="APELLIDO INVALIDO, INTRODUZCA UN MINIMO DE 3 CARACTERES";
            next_step = false;
        }
        if(apellido.value.length >3){
            $(apellidoale).addClass('hidden');
            $(apellido).removeClass('input-error');
        }

        else {
            $(this).removeClass('input-error');
        }
        if (nombre.value.length < 3){
            $(this).addClass('input-error')
            console.log('funciona')
        }
        object=document.getElementById("id_email");
            valueForm=object.value;

            var patron=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
            if(valueForm.search(patron)==0)
            {
                //Mail correcto
                $(emailale).addClass('hidden');
                $(object).removeClass('input-error');
            }
            else {
                $(emailale).removeClass('hidden');
                $(object).addClass('input-error');
                document.getElementById('emailale').innerHTML="CORREO ELECTRONICO INVALIDO";
                next_step = false;
                
            }
            //Mail incorrecto
            //$(email1).removeClass('hidden');
           //document.getElementById('email1').innerHTML="CORREO ELECTRONICO INVALIDO";
        
    });
    
});