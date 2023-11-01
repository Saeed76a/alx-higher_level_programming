#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('#red_header').on('click', () => {
    $('header').css('color', '#FF0000');
  });
});
