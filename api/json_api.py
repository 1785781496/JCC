import json
import os


class JsonAPI():
    def __init__(self, name='settings'):
        self.json_filename = "{}.json".format(name)
        self.json_dir = os.path.dirname(__file__)
        self.json_file = os.path.join(self.json_dir, self.json_filename).replace("\\", "/")

    def get_json_filename(self):
        return self.json_file

    def set_json_filename(self, filename):
        self.json_file = filename

    def set_json_file_path(self, path):
        self.json_file = os.path.join(path, self.json_filename).replace("\\", "/")

    def write_json_to_file(self, json_dict):
        with open(self.json_file, "w") as f:
            json_info = json.dumps(json_dict, sort_keys=True, indent=4, separators=(',', ': '))
            f.write(json_info)

    def read_json_from_file(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as f:
                return json.loads(f.read())