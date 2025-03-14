# WhatsApp Message Automation with Python

This Python script automates sending WhatsApp messages to multiple contacts using the `pywhatkit` library. It reads phone numbers from a CSV file and sends an automated message to each contact.

## Features
- Reads contacts from a CSV file
- Automatically adds country code if missing
- Sends instant WhatsApp messages with a delay to avoid spam detection

## Prerequisites
Ensure you have the following installed:

- Python (>=3.x)
- Required Python libraries:
  ```sh
  pip install pywhatkit pandas
  ```

## How to Use

### 1. Export WhatsApp Contacts
Since WhatsApp doesn’t allow direct contact extraction, use Google Contacts Export:

1. Go to [Google Contacts](https://contacts.google.com/)
2. Click **Export** → Choose **CSV format**
3. Download the `.csv` file containing all contacts

### 2. Prepare the CSV File
- Open the CSV file in Excel or Google Sheets.
- Ensure there is a column named **"Phone Number"** (modify the script if your column name differs).
- Remove unnecessary spaces or special characters from phone numbers.

### 3. Run the Script
Save the script as `whatsapp_sender.py` and run it:
```sh
python whatsapp_sender.py
```

### 4. How It Works
- Reads the CSV file and extracts phone numbers.
- Cleans and formats the numbers (adds `+91` for India if missing; modify as needed).
- Uses `pywhatkit.sendwhatmsg_instantly()` to send a message to each contact.
- Waits for 10 seconds between messages to prevent spam detection.

## Notes
- Ensure you have an active WhatsApp Web session.
- Do not use this script for spam or unsolicited messages.
- Modify the script as needed for different formats or country codes.

## Disclaimer
Use this script responsibly and comply with WhatsApp’s terms of service. Unauthorized automated messaging may result in account restrictions.

