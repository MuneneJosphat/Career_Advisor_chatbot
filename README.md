# AI Career Advisor Chatbot
An intelligent chatbot that recommends tech career paths and learning resources based on user skills, goals, and interests.
---
## Overview
The AI Career Advisor Chatbot uses natural language processing (NLP) and decision logic to guide users toward the best-suited tech careers. It analyzes your skills, preferences, or even resume, then recommends:
- Relevant career paths (e.g., Data Scientist, Web Developer)
- Curated learning resources (free courses, GitHub repositories, tools)
- Personalized tips for career growth
---
## Features
- Smart chatbot powered by AI (OpenAI / NLP engine)
- Skill-based career recommendations
- Learning resource suggestions (updated dynamically)
- Resume parsing (PDF/DOCX) (optional)
- User feedback loop to improve recommendations
- Web-based chat interface (Flask + HTML/JS frontend)
---
## Tech Stack
| Layer       | Tech                          |
|-------------|-------------------------------|
| NLP         |OpenAI API / HuggingFace / Rasa|
| Logic       | Python decision engine        |
| Backend     | Flask (REST API)              |
| Frontend    | HTML, CSS, JavaScript         |
| Storage     | JSON / SQLite                 |
---
## Project Structure
```bash
career-advisor-bot/
├── app.py              # Flask backend
├── chatbot.py          # Chat logic + NLP
├── recommender.py      # Career path + resource logic
├── templates/
│   └── index.html      # Chat UI
├── static/
│   ├── styles.css
│   └── script.js
├── data/
│   └── career_paths.json  # Career-to-skill mapping
├── requirements.txt
└── README.md
Getting Started

1. Clone the Repository
-git clone https://github.com/yourusername/career-advisor-bot.git
cd career-advisor-bot
2. Install Dependencies
-pip install -r requirements.txt
3. Run the Application
-python app.py
4. Then open your browser and visit http://localhost:5000
---
Data and Resources:
-Career mappings and resource links are stored in:
.data/career_paths.json
.You can expand this with new roles, topics, and external learning materials.
---
Future Enhancements:
-Resume upload and NLP extraction
-Admin interface to manage career mappings
-Offline/local chatbot integration
-User login and progress tracking
---
Contributing:
-Contributions and suggestions are welcome. Feel free to submit a pull request or open an issue to improve the project.
---
License:
-This project is licensed under the MIT License.
---

Author
Created by MUNENE JOSPHAT
