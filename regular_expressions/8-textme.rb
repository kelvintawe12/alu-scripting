#!/usr/bin/env ruby

# Regular expression to extract sender, receiver, and flags
regex = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

# Get the input argument and apply the regex
matches = ARGV[0].match(regex)

if matches
  sender = matches[:sender]
  receiver = matches[:receiver]
  flags = matches[:flags]
  puts "#{sender},#{receiver},#{flags}"
else
  puts ""
end
