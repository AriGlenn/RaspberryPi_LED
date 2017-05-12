$( document ).ready(function() {

  $('div.light-switch input').change(function() {
  console.log($(this).prop('checked'))
  console.log( "Clicked!" );

  fetch("http://0.0.0.0:5000/ledON")


  })






});
