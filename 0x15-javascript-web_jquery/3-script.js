// 3-script.js

// Wait for the document to be ready
$(document).ready(function () {
  // Get the DIV#red_header element
  const redHeader = $('#red_header');

  // Add a click event listener to the DIV#red_header
  redHeader.click(function () {
    // Get the <header> element
    const headerElement = $('header');

    // Add the class "red" to the <header> element
    headerElement.addClass('red');
  });
});

