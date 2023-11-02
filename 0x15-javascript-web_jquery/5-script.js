#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('#add_item').on('click', () => {
    $('.my_list').append('<li>Item</li>');
  });
});
