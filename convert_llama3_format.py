import json

def convert_gpt3_turbo_to_custom_format(input_file, output_file):
    data_list = []
    
    # Open the input JSONL file and read it line by line
    with open(input_file, mode='r', encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line)
            
            prompt = ""
            completion = ""
            
            # Iterate over the messages in the conversation
            for message in data.get('messages', []):
                if message.get('role') == 'user':
                    prompt += message.get('content', '') + " "
                elif message.get('role') == 'assistant':
                    completion += message.get('content', '') + " "
            
            # Strip any extra spaces from the prompt and completion
            prompt = prompt.strip()
            completion = completion.strip()
            
            # Create the new format with instruction, input, and output
            new_data = {
                "instruction": "",  # Assuming instruction is empty as per your original script
                "input": prompt,
                "output": completion
            }
            data_list.append(new_data)
    
    # Write the list of new format data to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data_list, outfile, ensure_ascii=False, indent=4)  # Add indent for better readability

# Define input and output file paths
input_file = 'openai.jsonl'
output_file = 'llama3.json'

# Convert the data
convert_gpt3_turbo_to_custom_format(input_file, output_file)

print(f"Successfully converted {input_file} to {output_file} in custom format.")