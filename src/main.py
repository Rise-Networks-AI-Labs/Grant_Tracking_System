import pandas as pd
import os 
import numpy as np
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get the parent directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ensure 'outputs' directory exists in the parent directory
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Initializing OpenAI's client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Loading the file
file_url = r"https://raw.githubusercontent.com/Rise-Networks-AI-Labs/Grant_Tracking_System/refs/heads/main/data/grant_data.csv"
df = pd.read_csv(file_url)


grant_content_list = []
def generate_email_content(df):
    df = df
    for _, rows in df.iterrows():
        grant_name = rows["Grant Name"]
        status = rows["Status"]
        deadline = rows["Deadline"]
        application_link = rows["Application Link"]
        priority = rows["Priority"]

        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """
                    You are a grants communication analyst responsible for highlighting funding opportunities for a newsletter. 
                    You will receive a list of grants.

                    Each grant includes:
                    - Grant Name
                    - Status
                    - Deadline
                    - Application Link
                    - Priority

                     task is to:
                    - Highlight all the grant opportunities with their respective information.
                    - Highlight key info such as priorities, and deadlines, etc.
                    - Do not copy directly; paraphrase for clarity and brevity.
                    - Use professional, and informative language suitable for NGOs.
                    """
            },
            {
                "role": "user",
                "content": f"""
                    **Grant Name:** {grant_name}

                    **SYourtatus:**
                    {status}

                    **Deadline:**
                    {deadline}

                    **Application Link:**
                    {application_link}

                    **Priority:**
                    {priority}

                    Generate a structured and engaging two-paragraph summary that highlights the funding opportunities from this category. 
                    This is meant to be a reminder mail.
                """
            }
        ],
            temperature=0
            )
        content = completion.choices[0].message.content.strip()
        # Append all the content
        grant_content_list.append(content)
    return grant_content_list


def merge_email_content():
    grant_content_list = generate_email_content(df)
    # Merge all the content
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """
                Your role is to generate professional email reminders about grant opportunities. 
                You must strictly follow the email template provided. 
                Always paraphrase the details for clarity and brevity. 
                Use formal, informative language suitable for NGOs.
                """
            },
            {
                "role": "user",
                "content": f"""
                Greetings MD and the Team,

                I trust this email finds us well.

                This email is a gentle reminder regarding the grants we are yet to apply for. 
                Please kindly find the details of the grants below:

                Grant 1:
                - Name of the grant
                - Application deadline
                - Every other necessary details in bullet points  

                **Grant_List:** {grant_content_list}

                Task:
                - Rewrite the grant list in the exact structure of the template above.
                - For each grant, use the label "Grant 1", "Grant 2", etc.
                - Under each grant, use bullet points for name, deadline, priorities, and other key details.
                - Do not write paragraphs, introductions, or summaries beyond the greeting and reminder text.
                - End the email with: 

                Warm Regards,
                """
            }
        ],
        temperature=0,
    )

    grant_content = completion.choices[0].message.content.strip()

    # Print or save the newsletter
    output_path = os.path.join(OUTPUTS_DIR, "Grant_Draft.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(grant_content)
        print(f"Email draft content saved as Grant_Draft.txt")

    return grant_content

if __name__ == "__main__":
    merge_email_content()