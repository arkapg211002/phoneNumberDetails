import phonenumbers
from phonenumbers import carrier,geocoder,timezone
#entering phone number
mobNo=input("Enter mobile number with country code\n")
mobNo=phonenumbers.parse(mobNo)

#timezone of phone number
print(timezone.time_zones_for_number(mobNo))
#carrier of phone number
print(carrier.name_for_number(mobNo,"en"))
#region information
print(geocoder.description_for_number(mobNo,"en"))
#validation of number
print("Valid phone number ",phonenumbers.is_valid_number(mobNo))
#checking possibilty of phone number
print("checking possibility... ",phonenumbers.is_possible_number(mobNo))
#print(carrier.__all__)
print(carrier.name_for_valid_number(mobNo,"en"))
print(carrier.safe_display_name(mobNo,'en'))
print(timezone.time_zones_for_geographical_number(mobNo))
