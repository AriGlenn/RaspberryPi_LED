localStorage.on_off = "off";
$( document ).ready(function() {
  $('div.light-switch input').change(function() {
    console.log($(this).prop('checked'))
    console.log( "Clicked!" );
    console.log(localStorage.on_off);
    if (localStorage.on_off == "off"){
      localStorage.on_off = "on";
      console.log(localStorage.on_off);
      fetch("http://0.0.0.0:5000/ledON");
    }else{
      localStorage.on_off = "off";
      console.log(localStorage.on_off);
      fetch("http://0.0.0.0:5000/ledOFF");
    }
  })
});
