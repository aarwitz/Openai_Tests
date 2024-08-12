import json

result = "```json\n{\n  \"clauses\": [\n    {\n      \"title\": \"1. THE LESSOR.\",\n      \"content\": \"Jane Smith (the \u201cLessor\u201d). Phone: (312) 555-7890 Email Address: jane.smith@example.com\"\n    },\n    {\n      \"title\": \"2. THE LESSEE.\",\n      \"content\": \"John Doe (the \u201cLessee\u201d). Phone: (217) 555-1234 Email Address: john.doe@example.com\"\n    },\n    {\n      \"title\": \"3. ADDRESS OF PREMISES.\",\n      \"content\": \"789 Oak Street, Chicago, IL 60610 (the \u201cPremises\u201d).\"\n    },\n    {\n      \"title\": \"4. RENTABLE SPACE.\",\n      \"content\": \"The total rentable space of the Premises consists of 2,500 square feet.\"\n    },\n    {\n      \"title\": \"5. LEASE TERM.\",\n      \"content\": \"The term of the lease shall commence on September 1, 2024, and end on August 31, 2029 (the \u201cLease Term\u201d).\"\n    },\n    {\n      \"title\": \"6. USE OF PREMISES.\",\n      \"content\": \"The Lessee shall be allowed to use the Premises for the following: retail store for organic groceries.\"\n    },\n    {\n      \"title\": \"7. RENT.\",\n      \"content\": \"The rent to be paid by the Lessee to"

# Step 1: Remove the markdown formatting (```json ... ```)
if result.startswith("```json"):
    result = result[7:].strip()
    print('1')
if result.endswith("```"):
    result = result[:-3].strip()
    print('2')
print(result)
# Step 2: Handle potentially incomplete content
# If the JSON is cut off, you'll need to detect this and handle it.
try:
    parsed_result = json.loads(result)
except json.JSONDecodeError:
    print("The JSON content appears to be incomplete or invalid.")
    # You can handle the incomplete content here, maybe log it or retry the request.
    exit(1)

# Step 3: Save the parsed dictionary to a JSON file
output_json_path = 'output_clauses.json'
with open(output_json_path, 'w') as json_file:
    json.dump(parsed_result, json_file, indent=2)

print(f"Output saved to {output_json_path}")