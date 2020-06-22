import json

def json_to_text(jsons, output_filename):
  with open(output_filename, "w") as f:
    for each_json in jsons:
      for line in each_json:
        f.writelines(" ".join(line) + "\n")
      f.writelines("\n")

def read_jsonl(filename):
  result = []
  with open(filename, "r") as f:
    for line in f.readlines():
      result.append(json.loads(line))
  return result
