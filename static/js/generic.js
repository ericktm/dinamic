jQuery.fn.exists = function () {
    return jQuery(this).length > 0 ? true : false;
};


$(document).ready(function () {

    $('.button').button();


    $('.open').on('click', function (e) {
        e.preventDefault();
        var div = $(this).attr('data-window');
        var title = $(this).attr('data-title');
        var height = $(this).attr('data-height');
        var width = $(this).attr('data-width');
        var address = $(this).attr('href');
        if ($('#' + div).exists()) {
        } else {
            console.log('Criando Elemento #' + div);
            $('<div class="hide" id="' + div + '"></div>').appendTo('body');
        }
        $('#' + div).dialog({
            title: title,
            resizable: false,
            modal: true
        });
        console.log('Carregando Conteudo do Elemento #' + div);

        $('#' + div).load(address);

    });


    //Table Definitions
    $('#table').dataTable({
        "bJQueryUI": true,
        "bStateSave": true,
        "sPaginationType": "full_numbers",
        "bServerSide": true,
        "sAjaxSource": "/get-data"
    });
});