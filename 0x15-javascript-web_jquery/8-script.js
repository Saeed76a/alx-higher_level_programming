#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      for (const m in data.results) {
        $('#list_movies').append(`<li>${data.results[m].title}</li>`);
      }
    }
  });
});
