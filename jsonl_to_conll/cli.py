from jsonl_to_conll import convert, io
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("input_filename", help="Input JSONL filename", type=str)
  parser.add_argument("output_filename", help="Output CONLL filename", type=str)
  parser.add_argument("-s", "--separator", help="Separator to use between words and tags", type=str, default=' ', nargs='?')
  parser.add_argument("--text_field", help="Name of the JSON field the text is stored in", type=str, default='text', nargs='?')
  parser.add_argument("--label_field", help="Name of the JSON field the labels are stored in", type=str, default='label', nargs='?')
  args = parser.parse_args()

  data = io.read_jsonl(args.input_filename)
  data = convert.flatten_all(data, args.text_field, args.label_field)
  io.json_to_text(data, args.output_filename, args.separator)

if __name__ == "__main__":
  main()
