"""
Class to handle writing and reading the addy api key

"""
import os
import platformdirs


class AddyKey:
    def __init__(self) -> None:
        filename = "addy_key.cfg"
        files_to_check = [os.path.join(dir_path, filename)
                          for dir_path in self._dirs()]
        for full_path in files_to_check:
            if os.path.exists(full_path):
                self.full_path = full_path
        else:
            self.full_path = files_to_check[0]
        os.makedirs(os.path.dirname(self.full_path), exist_ok=True)

    def _dirs(self) -> list[str]:
        """Returns possible dirs for config file, most to least preferred

        Storing the config file in the same location as this source file is
        supported for backward compatibility but should eventually be removed.
        """
        return (platformdirs.user_config_dir("addy"),
                os.path.dirname(os.path.abspath(__file__)))

    def write_to_config(self, key) -> None:
        with open(self.full_path, "w") as f:
            f.write(key)

    def load_key(self) -> None:
        key = None
        try:
            with open(self.full_path, "r") as f:
                key = f.readline()
        except OSError:
            if not self.api_key:
                raise ("No api key present: Run load-key")

        return key
