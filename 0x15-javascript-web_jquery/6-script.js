// 5-script.js

// Wait for the document to be ready
$(document).ready(function() {
  // When the user clicks on the DIV#add_item
  $('#add_item').click(function() {
    // Create a new <li> element with the text "Item"
    const newItem = $('<li>').text('Item');
    
    // Append the new <li> element to the UL.my_list
    $('UL.my_list').append(newItem);
  });
});

