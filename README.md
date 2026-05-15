🌐 Dynamic Portfolio — Flask + AWS Elastic Beanstalk
A dynamic personal portfolio website built with Python Flask and deployed on AWS Elastic Beanstalk. Features a password-protected admin panel to add and manage projects without touching code.
Live Demo: http://myproject-env.eba-c3d2fnqu.eu-central-1.elasticbeanstalk.com/

🏗️ Architecture
Browser
  └── AWS Elastic Beanstalk (Environment)
        └── EC2 t3.micro (Free Tier)
              └── Nginx (Reverse Proxy)
                    └── Gunicorn (WSGI Server)
                          └── Flask App (Python)
                                └── projects.json (Project Data)

✨ Features

Dynamic projects — all projects loaded from projects.json, no hardcoded HTML
Admin panel — password-protected /admin page to add/delete projects via a form
Scroll animations — reveal on scroll, animated skill bars
Custom cursor — interactive cursor that reacts to hover
Fully responsive — works on mobile and desktop
Dark editorial design — clean, professional look


🛠️ Tech Stack
LayerTechnologyLanguagePython 3.14FrameworkFlask 3.1WSGI ServerGunicornReverse ProxyNginxCloud PlatformAWS Elastic BeanstalkComputeAmazon EC2 (t3.micro — Free Tier)StorageAmazon S3 (app version storage)

📁 Project Structure
flask-portfolio-aws-elasticbeanstalk/
├── application.py          # Flask app — routes and admin logic
├── requirements.txt        # Python dependencies
├── Procfile                # Tells EB how to start the app
├── projects.json           # All project data (single source of truth)
├── templates/
│   ├── index.html          # Main portfolio page
│   ├── admin.html          # Admin dashboard
│   └── login.html          # Admin login page
└── .ebextensions/
    └── python.config       # EB config — sets WSGI path

🚀 Deployment — AWS Elastic Beanstalk
Prerequisites

AWS account (free tier)
Python 3.x installed locally

Steps
1. Clone the repo
bashgit clone https://github.com/Raghvendrayadav07/flask-portfolio-aws-elasticbeanstalk.git
cd flask-portfolio-aws-elasticbeanstalk
2. Install dependencies locally (optional, for testing)
bashpip install -r requirements.txt
python application.py
3. Zip the project
bashzip -r portfolio.zip . -x "*.git*"
4. Deploy on AWS Elastic Beanstalk

Go to AWS Console → Elastic Beanstalk → Create Application
Platform: Python
Upload portfolio.zip
Instance type: t3.micro (Free Tier eligible)
Deploy!


🔐 Admin Panel
Visit /admin on your live URL to manage projects:

Add projects via a simple form — no code editing needed
Delete projects with one click
Password protected


⚠️ Change the default password in application.py before deploying:
pythonADMIN_PASSWORD = 'your-secure-password-here'


🐛 Issues Solved During Deployment
Real errors encountered and fixed — documented for learning:
ErrorCauseFix502 Bad GatewayGunicorn not runningAdded ProcfileModuleNotFoundError: No module named 'application'Wrong WSGI pathAdded .ebextensions/python.configFiles not found on EBZip had nested folder structureZipped from inside the folder

📄 License
MIT — feel free to use and adapt.

👤 Author
Raghvendra Yadav

LinkedIn: linkedin.com/in/raghvendra-yadav-6871b12b0
GitHub: github.com/Raghvendrayadav07


Portfolio designed & built with the help of Claude (Anthropic)
