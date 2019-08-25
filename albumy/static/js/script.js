$(function () {
    var flash = null;

    $('#description-btn').click(function () {
        $('#description').hide();
        $('#description-form').show();    
    });
    $('#cancel-description').click(function() {
        $('#description-form').hide()
        $('#description').show()
    });
    $('#confirm-delete').on('show.bs.modal', function(e) {
        $('.delete-form').attr('action', $(e.relatedTarget).data('href'));
    });
});
