#!/usr/bin/env ruby
# A Ruby script to match strings

input_string = ARGV[0]
regex_pattern = /^hbtt*n$/

puts input_string if input_string.match?(regex_pattern)
