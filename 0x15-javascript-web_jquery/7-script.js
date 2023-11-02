#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function (data) {
      $('#character').text(data.name);
    }
  });
});
