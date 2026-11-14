
import json
from pathlib import Path


class GroupRepository:

    def __init__(self):
        self.data_file = (
            Path(__file__).resolve().parent.parent
            / "Data"
            / "groups.json"
        )

    def load_groups(self):

        if not self.data_file.exists():
            self.data_file.parent.mkdir(
                parents=True,
                exist_ok=True
            )
            self.data_file.write_text(
                "[]",
                encoding="utf-8"
            )

        try:
            with open(
                self.data_file,
                "r",
                encoding="utf-8"
            ) as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    def save_groups(self, groups):

        with open(
            self.data_file,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                groups,
                file,
                ensure_ascii=False,
                indent=4
            )

    def add_group(self, group_name):

        group_name = group_name.strip()

        if not group_name:
            return False

        groups = self.load_groups()
        groups.append(group_name)

        self.save_groups(groups)

        return True
