import json

def format_json(input_file_path, output_file_path):
    try:
        # Load the JSON data from the input file
        with open(input_file_path, 'r') as file:
            parsed_json = json.load(file)
        
        # Reformat the parsed JSON with indentation for readability
        formatted_json = json.dumps(parsed_json, indent=4)
        
        # Write the formatted JSON to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(formatted_json)
        
        print(f"Formatted JSON has been written to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input file path
    input_file_path = 'output_clauses_temp.json'
    
    # Output file path
    output_file_path = 'formatted_json.json'
    
    # Call the function to format the JSON and write to a new file
    format_json(input_file_path, output_file_path)

