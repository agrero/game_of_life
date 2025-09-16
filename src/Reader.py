import pandas as pd

class Reader:
    def __init__(self, path:str='') -> None:
        self.path = path

        self.data = self.read_csv()

    def read_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.path, index_col=0)
    