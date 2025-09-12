# Grant_Tracking_System
A simple Grant Tracking System that helps manage and track grant opportunities efficiently.
The system uses OpenAI for smart data processing and SMTP for automated email notifications, ensuring that users never miss important grant deadlines.

#### Features
- Grant Data Tracking – Store and organize grant opportunities in structured files.
- AI-Powered Summarization – Use OpenAI to generate summaries and insights.
- Automated Email Alerts – Send grant reminders or drafts via SMTP.
- CSV Data Integration – Push grant data from pushing_csv.py.
- Lightweight & Extensible – Easy to expand with new workflows or data pipelines.

#### Tech Stack
- Python 3.10+
- OpenAI API
- SMTP (email automation)
- GitHub Actions (workflow automation)

#### Installation
1. Clone the repository:
```bash
   git clone https://github.com/your-username/grant-tracking-system.git
   cd Grant_Tracking_System
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Configure environment variables:
   Create a .env file in the root directory with:
```bash
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_APP_PASSWORD=your_google_app_password
   SENDER_EMAIL="sender_email"
   RECEIVER_EMAIL = ["reciever_email"] # can add more for multiple recipients
```

#### Usage
1. Push CSV grant data:
```bash
   python pushing_csv.py
```

2. Run the main workflow:
```bash
   python run main.py
```

3. Send email manually:
```bash
   python send_email.py
```
Outputs such as drafts or summaries will appear in the outputs/ folder.

#### Project Structure
```text
grant_tracking_system/
|
|--- .github/
|    |--- workflows/
|         |___ script.yml
|--- notebook/
|    |___ testing.ipynb
|--- outputs/
|    |___ Grant_Draft.txt
|--- src/
|    |--- main.py
|    |___ send_email.py
|--- .env
|--- pushing_csv.py
|--- requirements.txt
|___ README.md
```

#### 🤝 Contributing
Contributions are welcome! Fork the repo, create a feature branch, and submit a pull request.

#### 📧 Contact
For support or collaboration, reach out via info@risenetworks.org


