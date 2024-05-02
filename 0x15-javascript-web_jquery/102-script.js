// This ensures that the script runs after the HTML document has finished loading.

$(document).ready(function() {
  $('#btn_translate').click(function() {
    var languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
      type: 'GET',
      success: function(data) {
        $('#hello').text(data.hello);
      },
      error: function() {
        $('#hello').text('Error fetching translation');
      }
    });
  });
});
