# Web Login Bypass CTF

## Overview

This is a beginner-friendly web security CTF challenge focused on weak login logic. The challenge runs inside a Docker container and provides a simple Flask web application with an intentionally vulnerable login form.

## Category

Web Security / CTF / Docker

## Difficulty

Beginner

## Scenario

A small admin login portal is available to users. The application is supposed to allow only administrators to access the protected message. However, the login logic is weak and does not properly validate the password.

Your task is to test the login form, identify the logic flaw, and recover the CTF flag.

## Objectives

- Run the web application using Docker
- Access the application in the browser
- Test the login form
- Identify the weak authentication logic
- Recover the CTF flag
- Document the issue and basic recommendations

## Tools Used

- Python
- Flask
- Docker
- PowerShell
- Web browser
- GitHub

## Project Files

- `app.py` - vulnerable Flask web application
- `requirements.txt` - Python dependency list
- `Dockerfile` - builds the Flask application container
- `solution.md` - contains the solution and explanation
- `01-docker-flask-running.png` - screenshot showing the Docker container running
- `02-web-login-bypass-result.png` - screenshot showing the successful login bypass result

## How to Run

Build the Docker image:

```bash
docker build -t web-login-bypass-ctf .



