#!/usr/bin/env node

var process = require('process')
var short_url = require('short-url')
message = process.argv.splice(2).join(' ')
var url = message.match(/(https?:\/\/[^\s]+)/)
if (url) {
    short_url.shorten(url[1], function(err, url) {
    console.log(url)
    })
}
