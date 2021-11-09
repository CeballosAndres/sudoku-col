
function resolve(sudoku_input) {
  $.ajax({
          data: {
            sudoku_input: sudoku_input, 
            sudoku_algorithm: 'dump'
          },
          type: 'POST',
          url: '/resolve'
        })
        .done(function(data) {
          alert(data.body);
   });
};
