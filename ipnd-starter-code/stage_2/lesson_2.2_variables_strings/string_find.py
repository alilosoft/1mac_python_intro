quote = "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence"
print quote.find("faith")
print quote.find("python")
print quote.find('')
quote = "It's easy to make a buck. It's a lot tougher to make a difference."
print  quote.find("make", 0) # equivalent to find("make") => 13 
print quote[13:]
print  quote.find("make", 14) # second 'make' @48
print  quote.find("make", 49) # -1

example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string