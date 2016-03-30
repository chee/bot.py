#!/usr/bin/env node
message = process.argv.splice(2).join(' ')

if (message.indexOf('&echo') == 0) {
    console.log(message.substring(5))
}
