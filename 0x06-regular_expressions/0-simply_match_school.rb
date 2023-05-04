#!/usr/bin/env ruby

def search_for_school(input)
  input.scan(/School/).join
end

search_result = search_for_school(ARGV[0])
puts search_result

