import json
import os
from threading import Lock


class FeedbackStore:
    def __init__(self, path="data/user_feedback.json"):
        self.path = path
        self.lock = Lock()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            self._write([])

    def _read(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _write(self, items):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(items, file, indent=2)

    def add(self, item):
        with self.lock:
            items = self._read()
            items.append(item)
            self._write(items)

    def count(self):
        with self.lock:
            return len(self._read())
