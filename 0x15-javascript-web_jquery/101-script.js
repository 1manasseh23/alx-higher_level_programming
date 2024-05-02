// This ensures that the script runs after the HTML document has finished loading.

$(document).ready(function() {
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function() {
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
