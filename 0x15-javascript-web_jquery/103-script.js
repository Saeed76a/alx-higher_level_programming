#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $("#hello").empty();
  let f = () => {
    const l = $("#language_code").val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${l}`,
      method: 'GET',
      success: function (data) {
        $("#hello").html(data.hello);
      }
    })
  }
  $("#btn_translate").click(() => {
    f();
  })
  $("#language_code").keydown(function (event) {
    if (event.which === 13) {
      f();
    }
  })
})
