#!/usr/bin/env python3
"""
Script to convert words.json to words.txt with one word per line.
"""

import json

def convert_json_to_txt():
    """Convert words.json to words.txt with one word per line."""
    try:
        # Read the JSON file
        with open('words.json', 'r', encoding='utf-8') as json_file:
            words = json.load(json_file)
        
        # Write to text file, one word per line
        with open('words.txt', 'w', encoding='utf-8') as txt_file:
            for word in words:
                txt_file.write(word + '\n')
        
        print(f"Successfully converted {len(words)} words from words.json to words.txt")
        
    except FileNotFoundError:
        print("Error: words.json file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in words.json!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_json_to_txt()
