def count_studios():
    input_file_path = r"C:\Users\sethw\OneDrive\Documents\Projects\assignment 9\toprankedanime.csv"
    output_file_path = r"C:\Users\sethw\OneDrive\Documents\Projects\assignment 9\studio_counts.csv"
    
    studio_counts = {}
    
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        # Skip the header line
        next(infile)
        
        for line in infile:
            line = line.strip()
            if not line:
                continue
            
            fields = []
            current_field = ""
            inside_quotes = False
            
            for char in line:
                if char == ',' and not inside_quotes:
                    fields.append(current_field)
                    current_field = ""
                else:
                    if char == '"':
                        inside_quotes = not inside_quotes
                    current_field += char
            
            fields.append(current_field)  # Add the last field
            
            if len(fields) > 11:  # Ensure there are enough fields
                studios = fields[9].strip('[]"').split(", ")
                for studio in studios:
                    studio = studio.strip("'")
                    if studio in studio_counts:
                        studio_counts[studio] += 1
                    else:
                        studio_counts[studio] = 1
    
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write("Studio,Count\n")
        for studio, count in studio_counts.items():
            outfile.write(f"{studio},{count}\n")

# Call the function to execute the script
count_studios()