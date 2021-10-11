def sum_one_to_n(n):
  assert isinstance(n,int), 'n must be an integer'
  assert n>=1, 'n must be positive' 

  s1n=0
  add=1
  for num in range(n): 
    s1n = s1n +add 
    add = add + 1 

  return s1n

# Q27: Refactor it to use excessively short variable names (don’t do this on real programs).  Then re-run the automated tests to ensure that you didn't make any mistakes. 

# s1n = sum_of_number_one_to_n
# add = the_number_to_add_to_sum

# Q28: The guardian for n being positive works correctly, but some might argue that a check for positive would be more clear if it just checks if the value is greater than 0. Refactor it for better readability by changing the guardian. Then re-run the automated tests to ensure that you didn't make any mistakes. 



# Q29: You might have noticed that running the test cases takes a little while. That is because of the big test case for n=100000000. That is a lot of time to go around the for loop. It turns out that the formula below, attributed to Gauss (1777-1855) (https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to- 100/), computes this sum much more efficiently without any need for a loop: 
# sum=(n∙(n+1))/2
# Take out the loop and compute the sum using the formula above. 
# Then re-run the automated tests to ensure that this new approach still gets the correct answers. Also be sure to notice how much faster it is!! 