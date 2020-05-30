import json


def flatten(data):
  output_text = []
  beg_index = 0
  end_index = 0

  text = data["text"]
  all_labels = sorted(data["labels"])

  for ind in range(len(all_labels)):
    next_label = all_labels[ind]
    output_text += [(label_word, "O") for label_word in text[end_index:next_label[0]].strip().split()]

    label = next_label
    beg_index = label[0]
    end_index = label[1]
    label_text = text[beg_index:end_index]
    output_text += [(label_word, "B-" + label[2]) if not i else (label_word, "I-" + label[2]) for i, label_word in enumerate(label_text.split(" "))]

  output_text += [(label_word, "O") for label_word in text[end_index:].strip().split()]
  return output_text


def flatten_all(datas):
  return [flatten(data) for data in datas]
