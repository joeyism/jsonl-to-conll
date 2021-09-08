import json

def json_to_text(jsons, output_filename, separator):
  with open(output_filename, "w") as f:
    for each_json in jsons:
      for line in each_json:
        f.write(separator.join(line) + "\n")
      f.write("\n")

def read_jsonl(filename):
  with open(filename, "r") as f:
    return [json.loads(line) for line in f if line.strip()]
