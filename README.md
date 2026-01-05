# 🚀 Policy-Driven Infrastructure Automation System

A DevOps-focused project that validates infrastructure configurations against predefined policies to ensure **security, compliance, and cost control**.  
The system follows **Policy-as-Code** principles and can be used as a backend engine or exposed via a web interface.

---

## 📌 Problem Statement
Manual infrastructure provisioning often leads to:
- Security misconfigurations
- Policy violations
- Increased cloud costs
- Inconsistent environments

This project solves the problem by **automatically enforcing policies before infrastructure deployment**.

---

## 🎯 Project Objectives
- Enforce infrastructure policies automatically
- Prevent insecure or non-compliant configurations
- Demonstrate Policy-as-Code concepts
- Provide a reusable DevOps validation engine
- Expose policy checks via a web interface

---

## 🛠️ Tech Stack
- **Python 3.14**
- **Flask** (Web Interface)
- **YAML** (Policy Definition)
- **JSON** (Infrastructure Configuration)

---

## 📂 Project Structure

Policy-Driven-Infrastructure-Automation-System/
│
├── app.py # Flask web application
├── policy_engine.py # Core policy validation logic
├── policy.yaml # Infrastructure policies
├── infrastructure.json # Sample infrastructure config
├── README.md # Project documentation

---

## ⚙️ How It Works
1. Policies are defined in `policy.yaml`
2. Infrastructure configuration is provided in `infrastructure.json`
3. The policy engine validates configuration against policies
4. Violations are blocked, compliant setups are approved
5. Results are displayed via a web interface

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install flask pyyaml
python app.py
open in browser
http://127.0.0.1:5000
Example Policies

Allow only approved instance types

Enforce encryption on resources

Prevent unauthorized configurations
Key Features

Policy-as-Code implementation

Automated infrastructure validation

Simple web-based interface

CI/CD pipeline–ready architecture

Easily extendable for Terraform & Cloud integration
Future Enhancements

REST API support

Terraform policy validation

GitHub Actions CI/CD integration

Cloud provider integration (AWS/Azure)

Advanced UI with forms and dashboards
