# FitLog — Fitness Tracker with Azure CI/CD Pipeline

A full-stack fitness tracking web application that combines strength training and cardio logging, automatically deployed to the cloud using a complete CI/CD pipeline on Microsoft Azure.

---

# Live Demo
http://4.255.215.220:5000

---

# Project Overview
FitLog is a web application inspired by Strong and Strava, allowing users to log and track both strength training sessions and cardio workouts in one place. The app is containerized with Docker and automatically deployed to an Azure Virtual Machine whenever code is pushed to GitHub.

---

#  Architecture

GitHub → Azure DevOps Pipeline → Azure Container Registry → Azure VM (Docker)

---

# Tech Stack

# Application
- Python Flask — web framework
- SQLAlchemy — ORM and database management
- SQLite — lightweight relational database
- HTML/CSS — frontend UI

# DevOps & Cloud
- Docker — containerization
- Azure Container Registry (ACR) — Docker image storage
- Azure Virtual Machine (Ubuntu 24.04) — cloud hosting
- Azure DevOps Pipelines — CI/CD automation
- GitHub — source control

---

## Features
- Log strength training sessions (exercise, sets, reps, weight)
- Log cardio sessions (type, distance, duration, pace)
- View workout history dashboard
- Auto-calculated stats (total sessions, total distance, pace)
- Delete individual logs
- Fully containerized and cloud-deployed

---

# CI/CD Pipeline
Every push to the main branch automatically:
1. Triggers Azure DevOps Pipeline
2. Builds a Docker image from the latest code
3. Pushes the image to Azure Container Registry
4. SSHs into the Azure VM
5. Pulls the latest image and restarts the container

---

# Project Structure
flask-azure-cicd/
├── app.py                  # Flask application and routes
├── models.py               # Database models
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── azure-pipelines.yml     # CI/CD pipeline definition
└── templates/
├── base.html           # Base template with navigation
├── index.html          # Homepage
├── strength.html       # Strength logging form
├── cardio.html         # Cardio logging form
└── dashboard.html      # Stats and workout history

---

## 🏃 Running Locally

**Prerequisites:**
- Python 3.11+
- Docker Desktop

**Clone the repo:**
```bash
git clone https://github.com/Dheeraj0737/flask-azure-cicd.git
cd flask-azure-cicd
```

**Run with Python:**
```bash
pip install -r requirements.txt
python app.py
```

**Run with Docker:**
```bash
docker build -t fitlog-app .
docker run -p 5000:5000 fitlog-app
```

Open http://localhost:5000

---

## ☁️ Azure Infrastructure
| Resource | Details |
|---|---|
| Virtual Machine | Standard_B2ats_v2, Ubuntu 24.04 |
| Container Registry | Basic tier |
| Region | West Central US |
| Pipeline Agent | Self-hosted on Windows |

---

## 📸 Screenshots
> Add screenshots of your homepage, strength log, cardio log, and dashboard here

---

## 🎓 Key Learnings
- Containerizing Python Flask applications with Docker
- Setting up CI/CD pipelines with Azure DevOps
- Managing Docker images with Azure Container Registry
- Deploying and managing Linux VMs on Azure
- Configuring self-hosted pipeline agents
- Networking and port configuration on Azure

---

## 👤 Author
**Dheeraj Vallabhapurapu**
Illinois Institute of Technology
GitHub: [@Dheeraj0737](https://github.com/Dheeraj0737)