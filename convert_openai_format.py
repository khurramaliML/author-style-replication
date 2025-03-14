import json
import os

def convert_txt2jsonl(input_file, output_file):
    with open(input_file, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
    
    qa_pairs = []
    current_question = None
    current_answer = []

    for line in lines:
        line = line.strip()
        if line.startswith("Question:"):
            if current_question and current_answer:
                qa_pairs.append((current_question, ' '.join(current_answer).strip()))
            current_question = line.replace("Question: ", "")
            current_answer = []
        elif line.startswith("Answer:"):
            if current_answer:
                qa_pairs.append((current_question, ' '.join(current_answer).strip()))
            current_answer = [line.replace("Answer: ", "")]
        else:
            if current_answer is not None:
                current_answer.append(line)

    if current_question and current_answer:
        qa_pairs.append((current_question, ' '.join(current_answer).strip()))

    with open(output_file, mode='w', encoding="UTF-8") as f:
        for question, answer in qa_pairs:
            json_line = json.dumps(
                {"messages": [{"role": "user", "content": question}, {"role": "assistant", "content": answer}]},
                ensure_ascii=False  # Preserve UTF-8 characters
            )
            f.write(json_line + '\n')

if not os.path.exists('jsonl'):
    os.makedirs('jsonl')

list_dirs = os.listdir("dataset")

for file_name in list_dirs:
    if file_name.endswith('.txt'):
        input_file = f'dataset/{file_name}'
        output_file = f'jsonl/{file_name.split(".")[0]}.jsonl'  
        convert_txt2jsonl(input_file, output_file)
        print(f"Successfully converted the {output_file} file")