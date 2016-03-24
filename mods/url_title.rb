#!/usr/bin/env ruby
require 'mechanize'
require 'uri'

message = ARGV.join(' ')
url = URI.extract(message)[0]
if url
    puts "Title: #{Mechanize.new.get(url).title} [#{url}]"
end
