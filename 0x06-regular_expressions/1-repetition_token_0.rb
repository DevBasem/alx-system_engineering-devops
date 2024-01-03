#!/usr/bin/env ruby

if ARGV.length == 1
  input = ARGV[0]
  regex = /hb(t{2,5})n/

  matches = input.scan(regex)

  if matches.any?
    puts matches.join("\n")
  else
    puts "No match"
  end
else
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end
