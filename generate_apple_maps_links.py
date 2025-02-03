import urllib.parse

def clean_and_generate_links(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    cleaned_lines = []
    
    # Process in chunks of 4 (business name, address, symbol, unwanted note)
    for i in range(0, len(lines), 4):
        if i + 1 < len(lines):  # Ensure there's a business name and address
            business_name = lines[i]
            business_address = lines[i + 1]
            cleaned_lines.append(f"{business_name} {business_address}")

    # Generate Apple Maps links
    apple_maps_links = [
        f"https://maps.apple.com/?q={urllib.parse.quote_plus(line)}" for line in cleaned_lines
    ]

    # Write the cleaned links to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(apple_maps_links))

# Run the script
input_file = "input.txt"
output_file = "apple_maps_links.txt"
clean_and_generate_links(input_file, output_file)

print("Processing complete! Links saved in apple_maps_links.txt.")