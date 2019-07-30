moment.locale("en");
function flask_moment_render(elem) {
    $(elem).text(eval('moment("' + $(elem).data('timestamp') + '").' + $(elem).data('format') + ';'));
    $(elem).removeClass('flask-moment').show();
}
function flask_moment_render_all() {
    $('.flask-moment').each(function() {
        flask_moment_render(this);
        if ($(this).data('refresh')) {
            (function(elem, interval) { setInterval(function() { flask_moment_render(elem) }, interval); })(this, $(this).data('refresh'));
        }
    })
}
$(document).ready(function() {
    flask_moment_render_all();
});
moment.locale("pt");


// código para trocar uma palavra dentro de uma tag selecionada por uma classe
// const td_status = document.getElementsByClassName('td_status')
// console.log(td_status)
// for(let e of td_status){
//     let txt = e.firstChild.nodeValue.replace("active", "Ativo")
//     e.innerHTML = txt
// }

// let permissao = document.getElementsByClassName('permissao')
// console.log(permissao)
// for(let e of permissao){
//     let txt = e.firstChild.nodeValue.replace("admin", "Administrador")
//     e.innerHTML = txt
// }