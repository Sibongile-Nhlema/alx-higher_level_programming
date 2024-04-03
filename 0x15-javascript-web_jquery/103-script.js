$(document).ready(() => {
    // Function to fetch and display translation
    const fetchTranslation = () => {
        // Get the language code entered by the user
        const languageCode = $('#language_code').val();

        // Make an AJAX request to fetch the translation
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: { lang: languageCode },
            success: function(response) {
                // Display the translation in the HTML tag DIV#hello
                $('#hello').text(response.hello);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    };

    // Fetch translation when user clicks Translate button
    $('#btn_translate').click(() => {
        fetchTranslation();
    });

    // Fetch translation when user presses Enter in the language code input field
    $('#language_code').keypress((e) => {
        if (e.which === 13) {
            fetchTranslation();
        }
    });
});
