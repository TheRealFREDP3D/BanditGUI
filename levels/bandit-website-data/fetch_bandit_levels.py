import requests
from bs4 import BeautifulSoup
import json
import re
import time

def fetch_bandit_levels():
    # Since the website might be using JavaScript to load content dynamically,
    # we'll create a basic structure based on the known number of levels
    levels_data = {}
    
    # Add headers to make our request look more like a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Create data for levels 0 through 34
    for level in range(35):
        # The correct URL format is level -> level+1
        next_level = level + 1
        url = f"https://overthewire.org/wargames/bandit/bandit{next_level}.html" if level > 0 else "https://overthewire.org/wargames/bandit/bandit0.html"
        
        try:
            print(f"Fetching data for level {level} from {url}...")
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Add a small delay between requests to be polite
            time.sleep(5)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Get the main content div
            content_div = soup.find('div', class_='col-md-12')
            if not content_div:
                print(f"Warning: No content found for level {level}")
                continue
            
            # Get all paragraphs and lists
            content = content_div.find_all(['p', 'ul'])
            if not content:
                print(f"Warning: No paragraphs or lists found for level {level}")
                continue
            
            # Extract description (first paragraph)
            description = content[0].get_text(strip=True, separator=' ') if content else ""
            
            # Extract objective (remaining paragraphs)
            objective_parts = []
            hints = []
            
            for elem in content[1:]:
                if elem.name == 'ul':
                    # Extract hints from list items
                    hints.extend([li.get_text(strip=True) for li in elem.find_all('li')])
                else:
                    # Add paragraph to objective
                    text = elem.get_text(strip=True, separator=' ')
                    if text:
                        objective_parts.append(text)
            
            objective = ' '.join(objective_parts)
            
            level_info = {
                "level": f"Level {level}",
                "description": description,
                "objective": objective,
                "hints": hints
            }
            
            levels_data[str(level)] = level_info
            print(f"Successfully processed level {level}")
            
        except requests.RequestException as e:
            print(f"Error fetching level {level}: {e}")
        except Exception as e:
            print(f"Unexpected error processing level {level}: {e}")
    
    # Save to JSON file
    if levels_data:
        output_file = "bandit_levels.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(levels_data, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved {len(levels_data)} levels to {output_file}")
    else:
        print("No level data was collected!")

if __name__ == "__main__":
    fetch_bandit_levels()
