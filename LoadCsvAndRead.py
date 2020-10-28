
import pandas as pd

# data_folder = Path("C:/Users/adam.batchelor/Desktop/")
# file_to_open = data_folder / "LoungeBuddyDetail.csv"

df = pd.read_csv("LoungeBuddyDetail.csv")
df.columns

print(df.head)