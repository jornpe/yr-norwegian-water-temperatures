from yrwatertemp import WaterTemperatures

api_key = "your_api_key_here"  # Replace with your actual API key
client = WaterTemperatures(api_key)

water_temperatures = client.get_all_water_temperatures()
for temp in water_temperatures:
    print(f"{temp.name} ({temp.location_id}): {temp.temperature}°C at {temp.time}")



