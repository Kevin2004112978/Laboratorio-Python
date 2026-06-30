def liters_100km_to_miles_gallon(liters):
    
    kms_per_mile = 1.609344
    
    liters_per_gallon = 3.785411784
    
    
    return (100 * liters_per_gallon) / (liters * kms_per_mile)

def miles_gallon_to_liters_100km(miles):
  
    kms_per_mile = 1.609344
    
    liters_per_gallon = 3.785411784
    
    
    return (100 * liters_per_gallon) / (miles * kms_per_mile)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
