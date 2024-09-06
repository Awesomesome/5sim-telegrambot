import os

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Manually read the .env file
env_path = os.path.join(os.getcwd(), '.env')
env_vars = {}

if os.path.exists(env_path):
    print("Contents of .env file:")
    with open(env_path, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
                print(line.strip())
else:
    print(".env file not found!")

TELEGRAM_TOKEN = env_vars.get('TELEGRAM_TOKEN')
SIM_API_KEY = env_vars.get('SIM_API_KEY')

print(f"Loaded TELEGRAM_TOKEN: {TELEGRAM_TOKEN}")
print(f"Loaded SIM_API_KEY: {SIM_API_KEY[:10]}...") # Print only the first 10 characters of the API key for security
print(f"SIM_API_KEY (first 10 characters): {SIM_API_KEY[:10]}...")