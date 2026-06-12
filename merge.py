import json
import string
import urllib.request

# 1. Configuration
CUSTOM_FILE_PATH = "meals.json"  # Rename this to match your file
OUTPUT_FILE_PATH = "merged_themealdb.json"  # The final output file

print("[...] Loading your custom local JSON file...")
try:
    with open(CUSTOM_FILE_PATH, "r", encoding="utf-8") as f:
        custom_data = json.load(f)
except FileNotFoundError:
    print(f"[X] Error: Could not find '{CUSTOM_FILE_PATH}'. Please check the file name.")
    exit()

# Ensure the meals array exists
existing_meals = custom_data
if existing_meals is None:
    existing_meals = []

# Index existing meals by lowercased name to instantly check for duplicates
existing_names = {meal["strMeal"].strip().lower() for meal in existing_meals if meal.get("strMeal")}

# Find your highest ID so we can cleanly increment any incoming recipe IDs
current_max_id = max([int(meal["idMeal"]) for meal in existing_meals if meal.get("idMeal") and str(meal["idMeal"]).isdigit()], default=55000)

print(f"[!] Loaded {len(existing_meals)} local recipes. Highest ID found: {current_max_id}")
print("[...] Fetching latest recipes from TheMealDB API...")

official_meals_found = 0
new_meals_added = 0

# 2. Iterate through 'a' to 'z' to scrape the public database
# Also loop through 0-9 to catch any numerical recipes if they exist
search_chars = string.ascii_lowercase + "0123456789"

for letter in search_chars:
    # FIX: Corrected URL path and changed parameter back to 'f' for broad first-letter searching
    api_url = f"https://themealdb.com/api/json/v1/1/search.php?s={letter}"
    
    try:
        # Added a standard User-Agent header to prevent potential HTTP 403 blocks from the API host
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            meals_list = data.get("meals")
            
            if meals_list:
                for meal in meals_list:
                    official_meals_found += 1
                    meal_name = meal["strMeal"].strip().lower()
                    
                    # Merge only if the recipe doesn't already exist in your file
                    if meal_name not in existing_names:
                        current_max_id += 1
                        meal["idMeal"] = str(current_max_id)  # Re-index to prevent collisions
                        existing_meals.append(meal)
                        existing_names.add(meal_name)  # Avoid duplicate tracking
                        new_meals_added += 1
                        
    except Exception as e:
        print(f"[!] Failed to fetch recipes starting with '{letter}': {e}")

# 3. Save the results
custom_data = existing_meals
with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(custom_data, f, indent=4, ensure_ascii=False)

print("\n[:D] Process Completed successfully!")
print(f"- Total official recipes scanned: {official_meals_found}")
print(f"- New recipes merged into your file: {new_meals_added}")
print(f"[!] Saved updated database to: '{OUTPUT_FILE_PATH}'")
