$(document).ready(() => {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(response) {
            response.results.forEach(movie => {
                $('#list_movies').append(`<li>${movie.title}</li>`);
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log('Error:', errorThrown);
        }
    });
});
