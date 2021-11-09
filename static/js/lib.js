//Funcion para restringir la entrada de los input de 1-9 en caracteres ASCII (49-57)
function onlyNumberKey(evt) {    
  var ASCIICode = (evt.which) ? evt.which : evt.keyCode
  if (ASCIICode > 31 && (ASCIICode < 49 || ASCIICode > 57))
      return false;
  return true;
}

//para mostrar el algoritmo seleccionado en el dropmenu
$('.dropdown-menu a').click(function(){
  $('#selected').text($(this).text());
})

function numbers(){
  let numbers_matrix = '';
  for(let i = 0; i <= 80; i++){
    numbers_matrix += $("#cell-"+i).val();
    if (i != 80){
      numbers_matrix += ",";
    };
  }
  return numbers_matrix;
};

function fill(sudoku_array){
  let cell = 0;
  for(let i = 0; i < 9; i++){
    for(let j = 0; j < 9; j++){
      $("#cell-"+cell).val(sudoku_array[i][j]);
      cell++;
    }
  }
};

function resolve() {
  $.ajax({
    data: {
            sudoku_input: numbers(), 
            sudoku_algorithm: 'dump'
          },
          type: 'POST',
          url: '/resolve'
        })
        .done(function(data) {
          fill(data.body);
   });
};

function clean(){
    $("input").val('');
}
