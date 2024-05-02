// Ensures that the script runs after the HTML document has finished loading.

$(document).ready(function() {
  //  Initiates an AJAX request to the specified URL.
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function(data) {
      $.each(data.results, function(index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function() {
      $('#list_movies').append('<li>Error fetching movie data</li>');
    }
  });
});
