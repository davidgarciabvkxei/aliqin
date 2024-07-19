import json

# Assuming 'sections' is the data to be dumped and 'json_file' is the file object
json.dump(sections, json_file, ensure_ascii=False, indent=4)
