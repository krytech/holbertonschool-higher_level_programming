$.get('https://swapi.co/api/people/5/?format=json', function (response) {
  $('DIV#character').text(response.name);
});
