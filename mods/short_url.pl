#!/usr/bin/env perl
use strict;
use warnings;

use Regexp::Common qw/URI/;
use WWW::Shorten 'TinyURL';

my $message = join(' ', @ARGV);
my ($url) = $message =~ /$RE{URI}{-keep}/;
if ($url) {
    my $short_url = makeashorterlink($url);
    print $short_url;
}
