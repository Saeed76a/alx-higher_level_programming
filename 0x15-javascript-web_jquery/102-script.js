#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('#btn_translate').click(() => {
    $('#hello').empty();
    let l = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${l}`,
      success: function (data) {
        $('#hello').append(data.hello);
      }
    });
  });
});
