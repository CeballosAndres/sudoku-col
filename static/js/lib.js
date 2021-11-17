//Funcion para restringir la entrada de los input de 1-9 en caracteres ASCII (49-57)
function onlyNumberKey(evt) {    
  var ASCIICode = (evt.which) ? evt.which : evt.keyCode
  if (ASCIICode > 31 && (ASCIICode < 49 || ASCIICode > 57))
      return false;
  return true;
}

// Para mostrar el algoritmo seleccionado en el dropmenu
$('.dropdown-menu a').click(function(){
  $('#selected').text($(this).text());
})

// Método auxiliar para obtener los valores de todas las celdas en orden
// ascendente
function get_inputs(){
  let numbers_matrix = '';
  for(let i = 0; i <= 80; i++){
    numbers_matrix += $("#cell-"+i).val();
    if (i != 80){
      numbers_matrix += ",";
    };
  }
  return numbers_matrix;
};

// Método auxiliar para rellenar la matriz con la respuesta del backend
function fill(sudoku_array){
  let cell = 0;
  for(let i = 0; i < 9; i++){
    for(let j = 0; j < 9; j++){
      $("#cell-"+cell).val(sudoku_array[i][j]);
      cell++;
    }
  }
};

// Método auxiliar para rellenar la matriz con un string
function fill_from_string(sudoku){
  sudoku_array = sudoku.split(',');
  alert(sudoku);
  for(let i = 0; i <= 81; i++){
      $("#cell-"+ i ).val(sudoku_array[i]);
  }
};

// Genera nuevas tarjetas para el historico
function push_historical_data(algorithm, time_to_resolve, sudoku){
  date = new Date();
  $("#history-content").prepend([
    $('<div class="card" style="width: 18rem;"><div class="card-body"></div></div>').append([
        $('<h5>'+date.toLocaleDateString() + " " + date.toLocaleTimeString()+'</h5>'),
        $('<p><b>Algoritmo </b>'+ algorithm + '</p>'),
        $('<p><b>Tiempo </b>'+ time_to_resolve.toFixed(5) + ' segundos</p>'),
        $('<a href="#" class="btn btn-primary" onclick="fill_from_string(\''+ sudoku +'\')">Cargar Sudoku</a>'),
    ]),
  ]); 
}


// Inicia una llamada ajax, enviando el algoritmo seleccionado así como un
// string de los valores ingresados por el usuario: "1,2,3,6,4,,,,,5,3,4"
function resolve() {
  sudoku_input = get_inputs();
  sudoku_algorithm = $('#selected').text().toLowerCase();

  if (sudoku_algorithm != 'elija algoritmo'){
  $.ajax({
    data: {
            sudoku_input: sudoku_input,
            sudoku_algorithm: sudoku_algorithm
          },
          type: 'POST',
          url: '/resolve'
        })
        .done(function(data) {
          if (data.status == "error"){
            alert(data.type);
          } else {
            fill(data.body);
            push_historical_data(sudoku_algorithm, data.time, sudoku_input);
            $('#history').css('visibility', 'visible');
          }
   });
  } else {
    alert('Es necesario seleccionar un algoritmo');
  } 
};

// Función para limpiar todas las celdas
function clean(){
    $("input").val('');
}

//funcion para mostrar historial
function showHistorial() {
  var x = document.getElementById("history");
  if (x.style.visibility === "hidden") {
    x.style.visibility = "visible";
  } else {
    x.style.visibility = "hidden";
  }
} 
