import numpy as np
import pandas as pd
import joblib

# প্যান্ডাস সেটিংস
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# লোড করুন
preprocessor = joblib.load("artifact/data_transformation/transformed_object/preprocessor.pkl")
train_arr = np.load("artifact/data_transformation/transformed/train.npy")

# কলামের নাম ও ডাটাফ্রেম তৈরি
feature_names = preprocessor.get_feature_names_out()
df_check = pd.DataFrame(train_arr[:, :-1], columns=feature_names)
df_check['target_price'] = train_arr[:, -1]

# প্রথম ৫টি রো প্রিন্ট করুন
print(df_check.head())