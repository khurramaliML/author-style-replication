import os
import json

def merge_jsonl_files(input_directory, output_file):
    with open(output_file, 'w', encoding='UTF-8') as outfile:
        for file_name in os.listdir(input_directory):
            if file_name.endswith('.jsonl'):
                file_path = os.path.join(input_directory, file_name)
                with open(file_path, 'r', encoding='UTF-8') as infile:
                    for line in infile:
                        outfile.write(line)

input_directory = 'jsonl'  # Directory containing your JSONL files
output_file = 'openai.jsonl'  # Output file name

merge_jsonl_files(input_directory, output_file)
print(f"Successfully merged all JSONL files into {output_file}")