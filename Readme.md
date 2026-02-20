# 🚀 Two-Tier Automated Web Deployment Pipeline

![Jenkins](https://img.shields.io/badge/Jenkins-Automated-green?style=for-the-badge&logo=jenkins)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![AWS](https://img.shields.io/badge/AWS-EC2%20Deployed-orange?style=for-the-badge&logo=amazon-aws)

This project demonstrates a complete **CI/CD lifecycle** for a 2-tier application. It automates the transition from local code development to a live production environment on **AWS EC2** using **Jenkins** and **Docker Compose**.

---

## 🛠 Tech Stack
- **Frontend:** Python (Flask)
- **Database:** MySQL (Data Persistence)
- **Orchestration:** Docker & Docker Compose
- **CI/CD:** Jenkins (Declarative Pipeline)
- **Infrastructure:** AWS EC2 (Ubuntu)
- **Monitoring:** Discord Webhooks

---

## ✨ Key Features
- **Continuous Deployment:** Automated pipeline triggered via **GitHub Webhooks** on every code push.
- **Health Checks:** Integrated a validation stage in Jenkins that verifies the app's responsiveness before finalizing the build.
- **Automated Maintenance:** Implemented `docker image prune` and **Docker Log Rotation** to prevent AWS EBS disk exhaustion.
- **Real-time Notifications:** Instant build status alerts sent to **Discord** via secure webhooks.
- **Security:** Managed secrets using Jenkins Credentials to keep Webhook URLs and API keys private.

---

## 🏗 CI/CD Workflow
1. **Push:** Developer pushes code to the `main` branch on GitHub.
2. **Trigger:** GitHub notifies Jenkins via a **Webhook**.
3. **Pipeline:** - **Checkout:** Pulls the latest code.
   - **Build:** Builds fresh Docker images and starts containers via `docker compose`.
   - **Health Check:** Pings the Flask app to ensure it's live.
   - **Maintenance:** Cleans up dangling Docker images.
4. **Notify:** Sends success/failure alert to **Discord**.

---

## 📂 Project Structure
- `app/app.py` - Flask application with retry logic for MySQL connectivity.
- `app/templates/index.html` - UI template.
- `Dockerfile` - Application image build configuration.
- `docker-compose.yml` - Orchestration with log rotation and dependency management.
- `Jenkinsfile` - Declarative pipeline as code.

---

## 🚀 How to Run Locally
```bash
docker-compose up --build