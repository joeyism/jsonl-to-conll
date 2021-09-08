# JSONL to CONLL
A simple tool to convert JSONL to CONLL

## Installation
To install, run
```bash
pip3 install --user jsonl-to-conll
```

## Usage
### Sample Usage
Basic usage:
```bash
jsonl-to-conll input.jsonl output.conll
```

To specify a separator for the conll file and atypical names for the 'text' and 'label' json fields:
```bash
jsonl-to-conll input.jsonl output.conll -s $'\t' --text_field 'data' --label_field 'labels'
```

### Documentation
```bash
usage: jsonl-to-conll [-h] [-s [SEPARATOR]] [--text_field [TEXT_FIELD]] [--label_field [LABEL_FIELD]] input_filename output_filename

positional arguments:
  input_filename        Input JSONL filename
  output_filename       Output CONLL filename

optional arguments:
  -h, --help            show this help message and exit
  -s [SEPARATOR], --separator [SEPARATOR]
                        Separator to use between words and tags
  --text_field [TEXT_FIELD]
                        Name of the JSON field the text is stored in
  --label_field [LABEL_FIELD]
                        Name of the JSON field the labels are stored in

```
