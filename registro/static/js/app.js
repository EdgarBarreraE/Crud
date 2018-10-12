console.log("Saludo")

function editar(nombre,correo,id){
    console.log(nombre+" "+correo+" "+id)
    $("#correo").val(correo)
    $("#nombre").val(nombre)
    $("#id").val(id)
    $('#formulario').attr('action', 'registro/editar');
}