import pandas as pd
import datetime

import os

# convert this to a self contained object

df_size = (1000,1000)

for directory in os.listdir('traj')[1:]:
    print(f'starting directory: {directory}')
    # read in df 1
   
    choice_dir = os.path.join('traj', directory)
    list_dir = os.listdir(choice_dir)

    if len(list_dir) == 1: continue

    path=os.path.join('traj', directory, list_dir[0])

    # these should be linear idk why they aren't
    def reshape_read(path:str, df_size:tuple[int,int], step:int):

        df = pd.read_csv(path, index_col=0).astype('Int8')

        df = pd.DataFrame(df.values.reshape(df_size))
        df['step'] = step
        
        return df

    df1 = reshape_read(path, df_size, 0)


    # need to check these are correct
    # the filenames seem to maybe be wrong when errors pop up
    # then we can have it delete itself or whatnot
    for ndx, path in enumerate(list_dir[1:]):
        try:
            path = os.path.join(choice_dir, path)
            df2 = reshape_read(path, df_size, (ndx+1)*100)
            df1 = pd.concat(
                [df1,df2]
            )
        except:
            print(f'Error with file {path}, likely invalid shape. Skipping...')
    if len(list_dir) > 1:
        for path in list_dir:
            print(f'removed: {path}')
            os.remove(os.path.join(choice_dir,path))

    minimum = df1.loc[:,['step']].min(0).values[0]
    maximum = df1.loc[:,['step']].max(0).values[0]

    new_filename = f'{minimum}-{maximum+100}.csv'
    df1.to_csv(os.path.join(choice_dir, new_filename))
    print(f'wrote file: {new_filename}')