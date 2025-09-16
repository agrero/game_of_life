import pandas as pd
import os
import datetime

class Merger:
    def __init__(self, new_filename:str, filepaths:list[str]) -> None:

        self.df = self.merge_reads(filepaths)

        # delete inputted filepaths
        self.delete_unmerged(filepaths)

        # save file and delete self to clear memory
        self.log(f'Wrote File: {new_filename}')
        self.df.to_csv(new_filename)

        del self

    def merge_reads(self, filepaths:list[str]) -> pd.DataFrame:
        df = pd.DataFrame()

        # iterate filepaths
        for path_ndx, path in enumerate(filepaths):
            self.log(f'Reading File: {path}')
            try:
                df = pd.concat(
                    [df, pd.read_csv(path, index_col=0).astype('Int8')]
                )
            # there's another errror that happens here
            except FileNotFoundError:
                self.log(f'Error finding file {path_ndx} : {path}. Skipping...')
        return df
    
    def delete_unmerged(self, filepaths:list[str]):
        for path in filepaths:
            os.remove(path)
            self.log('Removed File: {path}')

    
    def log(self, string:str) -> None:
        dt_string = f'[{datetime.datetime.now()}]'
        print(f'{dt_string}\t{string}')