#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('#update_header').on("click", () => {
    $('header').text("New Header!!! ")
  })
})
