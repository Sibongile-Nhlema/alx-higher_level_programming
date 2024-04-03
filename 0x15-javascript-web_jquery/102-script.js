$(document).ready(() => {
    $('#btn_translate').click(() => {
        const languageCode = $('#language_code').val();

        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: { lang: languageCode },
            success: function(response) {
                $('#hello').text(response.hello);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    });
});
