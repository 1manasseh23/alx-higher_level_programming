// Wait for the document to be ready
$(document).ready(function () {
  // Get the <header> element
  const headerElement = $('header');

  // Get the DIV#toggle_header element
  const toggleHeader = $('#toggle_header');

  // Add a click event listener to the DIV#toggle_header
  toggleHeader.click(function () {
    // Toggle the class between "red" and "green"
    headerElement.toggleClass('red green');
  });
});

