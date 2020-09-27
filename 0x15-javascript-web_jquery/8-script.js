$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
  console.log(data.results);
  for (movie of data.results) {
    $("UL#list_movies").append(`<li>${movie.title}</li>`);
  }
});
