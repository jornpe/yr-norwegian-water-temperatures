from yrwatertemperatures import WaterTemperatures

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'
client = WaterTemperatures(api_key)

try:
    # Fetch the water temperature data
    temperatures = client.get_all_water_temperatures()

    # Print the location and temperature
    for temp in temperatures:
        print(f"Location: {temp.name}, Temperature: {temp.temperature}°C")

except Exception as e:
    print(f"An error occurred: {e}")



