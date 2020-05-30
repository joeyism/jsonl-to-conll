from jsonl_to_conll import convert, io
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("input_filename", help="Input JSONL filename", type=str)
  parser.add_argument("output_filename", help="Output CONLL filename", type=str)
  args = parser.parse_args()

  data = io.read_jsonl(args.input_filename)
  data = convert.flatten_all(data)
  io.json_to_text(data, args.output_filename)

if __name__ == "__main__":
  main()
