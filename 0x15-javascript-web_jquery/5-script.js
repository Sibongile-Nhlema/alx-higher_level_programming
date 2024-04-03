$(document).ready(() => {
    $('#add_item').click(() => {
        const newItem = $('<li>').text('Item');
        
        $('ul.my_list').append(newItem);
    });
});
