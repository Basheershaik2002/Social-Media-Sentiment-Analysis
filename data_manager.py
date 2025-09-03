import pandas as pd
from datetime import datetime

class DataManager:
    def __init__(self):
        self.df = pd.DataFrame(columns=["post", "platform", "date", "polarity", "sentiment"])

    def add_post(self, text, platform, polarity, sentiment):
        new_row = {
            "post": text,
            "platform": platform,
            "date": datetime.today(),
            "polarity": polarity,
            "sentiment": sentiment
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)

    def get_data(self):
        return self.df
