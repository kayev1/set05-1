def get_weather_icon(pct_rain):
  """ Given the percent chance of rain as an integer (e.g. 75 is 75%), return the name of the icon to be displayed."""
  if int(pct_rain) <= 10: 
    return 'fullsun.ico' 
  elif int(pct_rain) <= 20: 
    return 'suncloud.ico' 
  elif int(pct_rain) <= 85: 
    return 'twodrops.ico' 
  elif int(pct_rain) <= 50: 
    return 'onedrop.ico' 
  else: 
    return 'pouring.ico' 

pct_rain=input('Enter percent chance of rain as an integer (e.g. 75 is 75%):')

print(get_weather_icon(pct_rain))

# Q15: What icon name is returned if there is a:
# •	15% chance of rain? 
# print(get_weather_icon(15))
# suncloud.ico

# •	90% chance of rain? 
# print(get_weather_icon(90))
# pouring.ico

# Q16: For what range of pct_rain values that will result in the icon fullsun.ico? 

# The range between 0 and 10.

# Q17: Run the test below to confirm that it passes. Add additional tests that check that the proper icon is returned for: 
# •	15% chance of rain
# •	75% chance of rain
# •	95% chance of rain 
# Run your tests to confirm that they all pass. 

assert get_weather_icon(5)=='fullsun.ico', 'should be fully sunny'

# Q18: Add another one that checks that the onedrop.ico is returned when there is a 45% chance of rain. 

assert get_weather_icon(45)=='onedrop.ico', 'should be onedrop'

# Q19: One of your tests in Q18 should fail. How can you tell from the output which test has failed? 

# The error message states the value for pct_rain for which the assertion is incorrect.