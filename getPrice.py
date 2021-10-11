def get_price(age):
  if age <= 11:
    return 5
  elif (age>=12) and (age<18):
    return 7
  else:
    return 10

# Q21: The tests you wrote above for the get_weather_icon function were normal cases. When writing test cases it is good to also include tests for any edge (or boundary) cases. These tests check the specific values where the behavior of the function changes. 
# The above function is supposed to have prices of: 
# •	5 for children (11 or younger)
# •	7 for students (from 12 to 17 inclusive) 
# •	10 for adults (18 and over) 
# Write tests for get_price below that check that the price is correct for the edge case values of (11, 12, 17, 18). 
# Note: If you do this correctly, one of your test cases should fail. 

assert get_price(11) == 5
assert get_price(12) == 7
assert get_price(17) == 7
assert get_price(18) == 10

# Q22: Fix the error that was uncovered by your tests. Then rerun your tests in Q21 to confirm that they pass. 



# Q23: What are the edge case values for your fixed get_weather_icon function in Q20? You do not have to write test cases for them, just identify them. 
