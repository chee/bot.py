#!/usr/bin/env ruby
require 'mechanize'
require 'uri'

string = ARGV.join(' ')
url = URI.extract(string)[0]
if url
    puts "#{Mechanize.new.get(url).title} [#{url}]"
end
