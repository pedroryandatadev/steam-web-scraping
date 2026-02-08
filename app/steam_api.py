import requests
from app.config import EDITION_KEYWORDS

# Locale Setting for Steam API requests (Check the README.md file to find out yours)
CONFIG_COUNTRY = {
    "country": "BR", # country code (cc) for localized pricing
    "lang": "pt-BR" # Language code (l) for localized responses 
}

# Functions to fetch data from Steam API for both apps and packages (subs)
def get_package_data(package_id):
    url = f"https://store.steampowered.com/api/packagedetails?packageids={package_id}&cc={CONFIG_COUNTRY['country']}&l={CONFIG_COUNTRY['lang']}"
    try:
        response = requests.get(url).json()
        if response and response.get(str(package_id)) and response[str(package_id)]['success']:
            data = response[str(package_id)]['data']
            if 'price' not in data: return None
            
            return {
                "id": package_id,
                "name": data['name'],
                "current_price": data['price']['final'] / 100, # Converts to the normal value
                "discount": data['price'].get('discount_percent', 0)
            }
    except Exception as e:
        print(f"Error fetching package {package_id}: {e}")
    return None

# Main function to get data for either apps or subs based on the type specified in the config
def get_steam_data(item_id, item_type):
    if item_type == "sub":
        data = get_package_data(item_id)
        if data: # If we got valid data for the sub, we can set its type and return it as a single-item list
            data['type'] = "sub"
            return [data]
        return []
    
    # For apps, we need to check both the app details and its associated packages (if any) to find relevant editions
    url = f"https://store.steampowered.com/api/appdetails?appids={item_id}&cc={CONFIG_COUNTRY['country']}&l={CONFIG_COUNTRY['lang']}"
    try:
        response = requests.get(url).json()
        if not response or not response.get(str(item_id)) or not response[str(item_id)]['success']: 
            return []
        
        app_data = response[str(item_id)]['data']
        results = []

        if 'price_overview' in app_data:
            results.append({
                "id": item_id,
                "type": "app",
                "name": app_data['name'],
                "current_price": app_data['current_price'] if 'current_price' in app_data else app_data['price_overview']['final'] / 100,
                "discount": app_data['price_overview']['discount_percent']
            })

        if 'packages' in app_data:
            for pkg_id in app_data['packages']:
                pkg_info = get_package_data(pkg_id)
                if pkg_info and any(key in pkg_info['name'].lower() for key in EDITION_KEYWORDS):
                    pkg_info['type'] = "sub"
                    results.append(pkg_info)
        
        return results
    except Exception as e:
        print(f"Error on ID {item_id}: {e}")
        return []