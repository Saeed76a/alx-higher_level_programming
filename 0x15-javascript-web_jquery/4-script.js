#!/usr/bin/node
/* global $ */

let old = '';
let newest = '';
$(document).ready(() => {
  $('#toggle_header').on('click', () => {
    old = $('header').hasClass('red') ? 'red' : 'green';
    newest = old === 'red' ? 'green' : 'red';
    $('header').removeClass(old);
    $('header').addClass(newest);
  });
});
