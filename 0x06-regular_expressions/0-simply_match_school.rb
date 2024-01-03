#!/usr/bin/env ruby

if ARGV.length == 1
  puts ARGV[0].scan(/School/).join
else
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end
