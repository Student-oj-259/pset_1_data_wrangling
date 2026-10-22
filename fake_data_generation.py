import numpy as np
import pandas as pd
from faker import Faker 

def create_fake_data(N, df_chisq=3):
    fake = Faker()
    rng = np.random.default_rng()
    rows = []
    
    while len(rows) < N:
        household_id = fake.unique.random_int(min=1, max=8888)
        
        household_size_chisq = int(np.floor(rng.chisquare(df=df_chisq))) + 1
        household_size = min(household_size_chisq, 7,N - len(rows))
        
        for person in range(1, household_size + 1):
            rows.append({
                "household_id": household_id,
                "person": person,
                "name": fake.name(),
                "age": fake.random_int(min=10, max=100),
                "income": fake.random_int(min=10000, max=150000),
                "female": fake.random_int(min=0, max=1)
            })
            
    return pd.DataFrame(rows)

fake_users_df = create_fake_data(20, df_chisq=1)

fake_users_df.to_csv("fake_users.csv")