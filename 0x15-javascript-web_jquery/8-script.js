$.get('https://swapi.co/api/films/?format=json', function (response) {
  $('UL#list_movies').append(...response.results.map(movie => `<li>${movie.title}</li>`));
});
