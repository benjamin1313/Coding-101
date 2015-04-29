class Fixnum
    def to_human_number
        numbers = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight', 'nine', 'ten']
        numbers[self]
    end
end

humanNum = 0.to_human_number
puts humanNum

puts 'press enter to exit'
gets #waits for user to press enter