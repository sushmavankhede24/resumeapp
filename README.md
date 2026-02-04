# ResumeApp

ResumeApp is a production-oriented Django application built to help professionals create, manage, and present structured digital resumes and project portfolios. The project follows industry-standard development practices with a focus on maintainability, modular architecture, and environment-based configuration, mirroring how modern commercial backend systems are designed.

---

## Overview

The platform provides a centralized system for organizing professional information, technical skills, and project experience in a clean and structured format. It is designed to be easily extensible and suitable for real-world deployment scenarios.

---

## Features

- Professional profile management  
- Skills tracking with proficiency indicators  
- Project portfolio with descriptions and external links  
- Modular Django architecture for scalability  
- Environment-driven configuration  
- Docker support for consistent development environments  
- Integrated linting and testing setup  

---

## Technology Stack

**Backend:** Django, Python  
**Frontend:** HTML, CSS  
**Containerization:** Docker, Docker Compose  
**Testing:** Pytest  
**Code Quality:** Flake8, Pre-commit  

---

## Project Structure

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/18f47a4d-b510-4128-b627-bf7f1f57fe61" />

The structure follows recommended Django conventions to promote readability and long-term scalability.

---

## Getting Started

### Prerequisites
- Python 3.x  
- pip  
- Docker (optional)

### Installation

```bash
git clone https://github.com/sushmavankhede24/resumeapp.git
cd resumeapp
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

### Application URL:
```bash
http://127.0.0.1:8000/
```
Running with Docker
```bash
docker-compose up --build
```
Docker ensures a consistent runtime environment across development and deployment workflows.

### Testing
```bash
pytest
```
Testing support is included to encourage reliable, production-quality development.

## Engineering Principles

- Clear separation of concerns
- Readable and maintainable code
- Scalable project structure
- Environment-based configuration
- Developer-friendly workflows

## Roadmap

- Authentication and authorization
- Resume export (PDF)
- REST API support
- Enhanced frontend experience
- Cloud deployment
- CI/CD integration

## Contributing

Contributions are welcome. Please open an issue to discuss significant changes before submitting a pull request.

## License
This project is licensed under the MIT License.
