import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("-----------------------------------------")
print(" AK Phone Number Location - Telegram : https://t.me/AKHacking1")
print("-----------------------------------------")

entered_num = input("Please enter a phone number: ")

phone_num = phonenumbers.parse(entered_num, None)

print(phone_num)

print("Country :", geocoder.description_for_number(phone_num, "ar"))

print("Tele Company :", carrier.name_for_number(phone_num, "en"))

print("Timezone :", timezone.time_zones_for_number(phone_num))
