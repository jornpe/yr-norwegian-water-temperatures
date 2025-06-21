from yrwatertemp import WaterTemperatures

api_key = "1cda72ab-3e66-4689-afaa-0bbb5055d46e"
client = WaterTemperatures(api_key)

water_temperatures = client.get_all_water_temperatures()
for temp in water_temperatures:
    print(f"{temp.name} ({temp.location_id}): {temp.temperature}°C at {temp.time}")



