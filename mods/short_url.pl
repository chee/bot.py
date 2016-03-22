#!/usr/bin/env perl
use WWW:Shorten 'TinyURL';

$short_url = makeashorterlink('http://www.Google.com');
print $short_url;
