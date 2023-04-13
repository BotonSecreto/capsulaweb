//TÍTULO COLABORACIONES MÚSICO
function escribirMus(){
    document.getElementById("colabMusico").innerHTML = '<b class="col-lg-2 offset-lg-0">Colaboraciones Realizadas</b>';
}

//INSERTAR FRAME DEL REPRODUCTOR SPTF
function capturar(){
  document.getElementById("reprod").innerHTML += document.getElementById("txt_sptf").value;
  }

//TÍTULO COLABORACIONES DISCO
function escribirDisc(){
  document.getElementById("colabDisco").innerHTML = '<b>Créditos y colaboraciones de la producción</b>';
}
