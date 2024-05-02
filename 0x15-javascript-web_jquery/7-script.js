// This ensures that the script runs after the HTML document has finished loading.

$(document).ready(function() {
  // Initiates an AJAX request to the specified URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    success: function(data) {
      $('#character').text(data.name);
    },
    error: function() {
      $('#character').text('Error fetching character data');
    }
  });
});

