#!/usr/bin/env ruby
# A Ruby script to match strips

input_string = ARGV[0]
regex_pattern = /^hbt{2,5}n/

puts input_string if input_string.match?(regex_pattern)
