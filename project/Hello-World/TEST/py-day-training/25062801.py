#STEP1 先在kaggle上建立一個新的notebook，然後在kaggle上下載3個檔案
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

#STEP2 從kaggle上下載3個檔案至本機後上傳到KAGGLE的個人專案INPUT資料夾

#STEP3 讀取檔案
train_data = pd.read_csv("/kaggle/input/titanic-hachi/train.csv")
train_data.head()


