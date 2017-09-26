
$('#dosis, #duracion, #medicacion').change(function(){
  crear_dosificacion();
});

$("#form :input").focus(function(){
  $(this).closest('.form-group').removeClass('has-error'); 
  $(this).css("background-color", "white");
});

function crear_dosificacion(){
  if (parseInt($("#dosis").val()) > 0 && parseInt($("#duracion").val()) > 0 && $("#medicacion").val() != ''){
    $.ajax({
      url: '/anadirDosificacion/',
      data: {
        'dosis': parseInt($("#dosis").val()),
        'medicacion': $("#medicacion").val(),
        'duracion': parseInt($("#duracion").val()),
      },
      dataType: 'json',
      success: function(data){
        heparina_inicial = [];
        construir_vista_dosificacion(data.dosificacion, "#panel_dosificacion");
        insertar_input_dosificacion(data.dosificacion, "#panel_dosificacion");            
      }
    });
  }
}

function construir_vista_dosificacion(dosificacion, id){
  var salida ="<input type='hidden' name='num_dias' value='"+dosificacion.length+"'>"+
              "<table class='table table-th'><tr><th><i class='fa fa-chevron-left' aria-hidden='true' onclick='distribuir_a_izquierda()'></i></th></tr><tr><th>Pastillas</th></tr><tr><th>Heparina</th></tr></table>"+
              "<div class='wrap'><table class='table'>";
  var imagen_jeringa = ruta_imagen+ "jeringuilla.png";
  dosificacion_inicial = dosificacion;
  for (var i = 0; i < dosificacion.length; i++){
    salida += "<tr class='vertical'><td class='vertical'>"+dosificacion[i]+"mg</td>"+
                  "<td class='vertical'>";
    salida += generar_codigo_pastillas(dosificacion[i]);
    salida += "</td><td class='vertical'>";
    if(heparina_inicial != [] && (heparina_inicial[i] == "on" || heparina_inicial[i] == true)){
       salida += "<input type='checkbox' name='cb"+i+"' id='cb"+i+"' checked='true' />"+
                "<label for='cb"+i+"' class='btn'><img src='"+imagen_jeringa+"'/></label></td>"
    }else{
      salida += "<input type='checkbox' name='cb"+i+"' id='cb"+i+"'/>"+
                "<label for='cb"+i+"' class='btn'><img src='"+imagen_jeringa+"'/></label></td>";
    }
    
    salida += "</tr>";
    
  }
  salida += "</table></div><table class='table table-th'><tr><th><i class='fa fa-chevron-right' aria-hidden='true' onclick='distribuir_a_derecha()'></i></th></tr><tr><td></td></tr> </table>";
  $(id).html(salida);
}

function generar_codigo_pastillas(dosis){
  salida_pastilla = "";
  if(dosis != 0){

    proporcion = 2;
    mg_pastilla = $("#medicacion").find(":selected").val();
    pastilla_1mg = true;
    dosis_local = dosis;
    if(mg_pastilla != 1){
      proporcion = 8;
      pastilla_1mg = false;
    }
    do{
      proporcion /= 2;
      for (var i = parseInt(dosis_local / proporcion); i > 0; i--){
        if (pastilla_1mg){
          salida_pastilla += "<img src='"+ruta_imagen+"pastilla4.png'>";
        }else{
          salida_pastilla += "<img src='"+ruta_imagen+"pastilla"+proporcion+".png'>";
        }
        
      }
      dosis_local = dosis_local % proporcion;
    }while (dosis_local > 0);
  }else{
    salida_pastilla += "<i class='fa fa-times-circle fa-lg' aria-hidden='true'></i>";
  }
  return salida_pastilla;
}

function insertar_input_dosificacion(dosificacion, id){
  var string_dosificacion ="";
  for (var i = 0; i < dosificacion.length; i++) {
    string_dosificacion += dosificacion[i]+" ";
  }
  $(id).append("<input type='hidden' name='dosificacion_final' value='"+string_dosificacion+"'>");
}

$('.clase_imagen').on('click',function(){
  $(this).toggleClass('checked').prev().prop('checked',$(this).is('.checked'));
});

function distribuir_a_izquierda(){
  nueva_dosificacion = dosificacion_inicial;
  nueva_dosificacion.push(nueva_dosificacion.shift());
  
  nueva_heparina = obtener_heparina_clickada();
  nueva_heparina.push(nueva_heparina.shift());
  heparina_inicial = nueva_heparina;
  
  construir_vista_dosificacion(nueva_dosificacion, "#panel_dosificacion");
  insertar_input_dosificacion(nueva_dosificacion, "#panel_dosificacion");
  
 
}

function distribuir_a_derecha(){
  nueva_dosificacion = dosificacion_inicial;
  nueva_dosificacion.unshift(nueva_dosificacion.pop());
  
  nueva_heparina = obtener_heparina_clickada();
  nueva_heparina.unshift(nueva_heparina.pop());
  heparina_inicial = nueva_heparina;
  
  construir_vista_dosificacion(nueva_dosificacion, "#panel_dosificacion");
  insertar_input_dosificacion(nueva_dosificacion, "#panel_dosificacion");
  

}

function obtener_heparina_clickada(){
  var duracion = $("#duracion").val();
  var salida = [];
  for (var i = 0; i< duracion; i++){
    salida.push($("#cb"+i).is(":checked"));
  }
  return salida;
}

function cambiarDuracion(){
  var date = $("#fecha").datepicker('getDate');
  var today = new Date();
  var dayDiff = Math.ceil((date - today) / (1000 * 60 * 60 * 24));
  $("#duracion").val(dayDiff);
}

function cambiarFecha(){
  var duracion = $("#duracion").val();
  // 86400000 equivale a un día en milisegundos
  var ms = new Date().getTime() + (86400000 * duracion);
  var new_date = new Date(ms);
  $("#fecha").datepicker('setDate', new_date);
}



function submit_formulario(){
  ok = true;

  $("#form").each(function(){
    items = $(this).find(":input");
    
    for (var i = 1; i < items.length; i++){
      if(items[i].required && (items[i].value == "" || items[i].value <= 0) ){
        ok = false;
        $("#"+items[i].id).closest('.form-group').addClass('has-error');
        $("#"+items[i].id).css("background-color", "yellow");
      }else if((items[i].id == "dosis" || items[i].id == "duracion") && items[i].value <= 0){
        $("#"+items[i].id).closest('.form-group').addClass('has-error');
        $("#"+items[i].id).css("background-color", "yellow");
      }
    }
  });

  if (ok){
    $("#form").submit();
  }

  /*
  duracion = $("#duracion").val();
  dosis = $("#dosis").val();

  var valor_duracion = parseInt(duracion);
  var valor_dosis = parseInt(dosis);
  if( (valor_duracion > 0 && valor_dosis > 0) && (duracion && dosis)){
    
  }else{
    if(valor_dosis <= 0 || !dosis){
      $('#dosis').closest('.form-group').addClass('has-error');  
      $('#dosis').css("background-color", "yellow");
    }
    if(valor_duracion <= 0 || !duracion){
      $('#duracion').closest('.form-group').addClass('has-error');  
      $('#duracion').css("background-color", "yellow");
    }
  }
  */
}

function anadir_comentario(){
  var nuevo_comentario = $("#id_comentario-texto").val();
  if (nuevo_comentario != "" && nuevo_comentario != " "){
    $.ajax({
      url: '/anadir_comentario/',
      data: {
      'id': id_visita,
      'nuevo_comentario' : nuevo_comentario,
      'autor' : $("#id_comentario-autor").val()
      },
      dataType: 'json',
      success: function (data) {
        $("#comentarios").val(data.todos_comentarios);
        $("#id_comentario-texto").val("");
      }
    });
  }
}