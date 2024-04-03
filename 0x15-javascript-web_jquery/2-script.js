$(document).ready(() => {
    $('#red_header').click(() => {
        const headerElement = $('header').first();
        
        headerElement.css('color', '#FF0000');
    });
});
