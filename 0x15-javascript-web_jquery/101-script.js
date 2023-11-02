#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(() => {
    $('UL.my_list li:last').remove();
  });

  $('#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
