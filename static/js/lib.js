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
            alert("Tiempo empleado: " + data.time + " segundos.");
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
