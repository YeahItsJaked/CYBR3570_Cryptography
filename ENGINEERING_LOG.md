## Week 1 - Toolkit v0.1

### Added
- Caesar cipher educational implementation
- Brute force demonstration
- Frequency analysis helper

### Security Lesson
Classical ciphers are useful for learning, but they should never be used to protect real data.

### Reflection
We can't write our own encryption algorithm, because there are many things that can be left behind when using your own encryption algorithm. One such possible pattern is letter frequency. This was shown in that graph above that had letter frequency. Another thing that could happen is a small keyspace that someone can brute force. There are dozens of people with doctorates that have come up with modern encryption methods and many bad actors that are more educated than I to decrypt anything that I may try to make.

## Week 2 - Toolkit v0.2

### Added
- GCD functions
- Modular functions
- Randomness functions

### Most difficult function
extended GCD was probably the most difficult to understand the code of. There's a lot going on and python shorthand that makes some of it hard to follow compared to if it was all written out. 

### randomness failure
One way randomness can fail is in sampling bias. If we're grabbing a random byte of information, there are 256 possibilities. If we turn that into numbers 1-10, you're going to have a bias result since there is an extra chance for 6 of those options to be picked. Or if you grab a random byte from memory then you'll be more likely to find all 0's or if there is a specific set of bits that are often saved near each other in memory then those would be more likely. 

### rule for random values
If its meant to be secure, then use secrets. If I want repeatability to test, then I'll seed it and use random. 
