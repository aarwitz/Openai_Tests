import json

def compare_strings(str1, str2):
    """Compares two strings character by character and returns the number of matching characters and a list of mismatches."""
    matching_chars = 0
    total_chars = max(len(str1), len(str2))
    mismatches = []
    
    # Compare each character in the two strings
    for i in range(total_chars):
        if i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                matching_chars += 1
            else:
                mismatches.append((str1[i], str2[i], i))
        elif i < len(str1):
            mismatches.append((str1[i], '', i))
        else:
            mismatches.append(('', str2[i], i))
    
    return matching_chars, total_chars, mismatches

def compare_json_files(file1, file2):
    # Load the JSON data from both files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)
    
    # Initialize variables to keep track of matching characters and total characters
    total_matching_chars = 0
    total_chars = 0
    all_mismatches = []

    # Iterate over the clauses in both JSONs
    for clause1, clause2 in zip(json1['clauses'], json2['clauses']):
        clause_title = clause1['title']
        
        # Compare the titles
        matching_chars, chars_in_title, mismatches = compare_strings(clause1['title'], clause2['title'])
        total_matching_chars += matching_chars
        total_chars += chars_in_title
        
        if mismatches:
            for char1, char2, idx in mismatches:
                all_mismatches.append(f"Title mismatch in clause '{clause_title}': '{char1}' vs '{char2}' at position {idx}")
        
        # Compare the content
        matching_chars, chars_in_content, mismatches = compare_strings(clause1['content'], clause2['content'])
        total_matching_chars += matching_chars
        total_chars += chars_in_content
        
        if mismatches:
            for char1, char2, idx in mismatches:
                all_mismatches.append(f"Content mismatch in clause '{clause_title}': '{char1}' vs '{char2}' at position {idx}")
    
    # Calculate the percentage similarity
    percent_similarity = (total_matching_chars / total_chars) * 100 if total_chars > 0 else 0
    
    return percent_similarity, all_mismatches

if __name__ == "__main__":
    # Specify the paths to the JSON files
    file1 = 'output_clauses.json'
    file2 = 'output_clauses_temp.json'
    
    # Compare the JSON files and calculate the percent similarity
    percent_similarity, mismatches = compare_json_files(file1, file2)
    
    # Print the result
    print(f"Percent similarity between {file1} and {file2}: {percent_similarity:.2f}%")

    # Print out mismatches
    if mismatches:
        print("\nMismatches found:")
        for mismatch in mismatches:
            print(mismatch)
    else:
        print("No mismatches found.")