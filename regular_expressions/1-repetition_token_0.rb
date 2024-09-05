#!/usr/bin/env ruby

regex = /hb+tn/
matches = ARGV[0].scan(regex)
puts matches.join
