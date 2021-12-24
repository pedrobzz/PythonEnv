import os

def add_directory(path: str):
        if not os.path.isdir(path):
            os.mkdir(path)

class Struct:
    data_path: str
    def __init__(self, **entries):
        self.__dict__.update(entries)

class Env(Struct):
    def __init__(self, tokens_path=None):
        """
            To initialize:
            --------------
            >>> from env import Env
            >>> env = Env()
            >>> env.password
            pass123

            How to store variables:
            -----------------------
            Open ./tokens/.env and declare:\n
            ``VARIABLE``=``VALUE``\n
            Every value is a string as default, even without quotation marks.

        """
        if not tokens_path:
            filedir = __file__.replace("\\", "/")
            filedir = filedir.split("/")
            filedir = "/".join(filedir[:-1])
            tokens_path = f"{filedir}/tokens/"
        add_directory(tokens_path)
        self.env_file = f"{tokens_path}/.env"
        trunc = self.initialize()
        super().__init__(**trunc)

    def initialize(self) -> Struct:
        try:
            with open(self.env_file) as file:
                data = file.read().splitlines()

            variables = [list(dt.split("="))[0] for dt in data if dt]
            values = ["=".join(list(dt.split("="))[1:]) for dt in data if dt]
            trunc = dict(zip(variables, values))
            return trunc
        except FileNotFoundError:
            open(f"{self.env_file.replace('.env', '')}/.env", "w").close()
            print(f".env file created at: \n{self.env_file}")
            print('To add new variables, please restart the script')
            return self.initialize()


if __name__ == "__main__":
    main = Env()
    s = main.initialize()
