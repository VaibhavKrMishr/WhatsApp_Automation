import pywhatkit as kit
import pandas as pd
import time
print("Start")
# Load contacts from CSV (Modify column name based on your file)
df = pd.read_csv("contacts.csv")
contacts = df["Phone 1 - Value"].dropna().tolist()# Replace with correct column name
print(df.columns)
message = "Happy Holi🙏"
for contact in contacts:
    contact = str(contact).replace(" ", "").replace("-", "")  
    if not contact.startswith("+"):  
        contact = "+91" + contact  # Add country code if missing (modify for your country)
    
    kit.sendwhatmsg_instantly(contact, message, wait_time=10)
    time.sleep(10)  # Delay to avoid spam detection
print("Done")