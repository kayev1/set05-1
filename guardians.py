def percent_error(accepted_value, observed_value):
  assert isinstance(accepted_value,float), 'accepted value must be a number'
  assert isinstance(observed_value,float), 'observed value must be a number'
  assert accepted_value != 0, 'accepted value cannot be 0' 

  numerator = math.abs(observed_value - accepted_value)
  pct_error = numerator / accepted_value 

  return pct_error 

# Q24: What data types are allowed for the parameters of percent_error ? 

# Floats.

# Q25: What value is disallowed in a call to percent_error? Why?

# accepted_value = 0 because the last assertion does not allow it (pct_error = numerator / accepted_value does not have a real value if accepted value = 0).

# Q26: Add appropriate guardians to the getPrice function for the input.  

