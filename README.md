# MediStream: Streamlining Medical Documentation

MediStream is a comprehensive medical documentation platform developed for CUREMD, aimed at streamlining the burdensome process of medical note generation. This project leverages Django for the backend and React for the frontend, creating a seamless environment for healthcare providers to automate note creation for various stages of patient care, including initial notes, discharge notes, progress notes, visit notes, and more.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Medical documentation is an essential aspect of patient care, but it can often be a time-consuming and error-prone task for healthcare providers. MediStream is designed to simplify and accelerate the process of creating medical notes, ensuring that healthcare professionals can focus more on patient care and less on administrative tasks.

## Features

- **User-friendly Interface**: MediStream offers an intuitive and user-friendly interface accessible through web browsers.

- **Automated Note Generation**: The platform automates the generation of various medical notes, including initial patient assessments, discharge summaries, progress notes, and more.

- **Custom Templates**: Users can create custom note templates tailored to their specific medical practice or specialty.

- **Data Integration**: MediStream seamlessly integrates with electronic health record (EHR) systems to pull patient data, reducing manual data entry.

- **Secure and Compliant**: The platform complies with healthcare data security standards to ensure patient information remains confidential.

- **Multi-User Collaboration**: Supports multiple users collaborating on the same patient's notes in real-time.

## Getting Started

Before you begin using MediStream, please ensure you have the following prerequisites:

- **Python**: MediStream's backend is built with Django, which requires Python. Make sure you have Python installed on your system.

- **React.js**: The frontend is developed using React, which requires Node.js. Install Node.js if you haven't already.

- **Database**: MediStream uses a database to store patient data and notes. MySQL is recommended. Also, it uses CUREMD proprietary database for pulling patient details and history.

## Installation

1. **Clone the Repository**:

   ```
   git clone https://github.com/yourusername/MediStream.git
   ```

2. **Backend Setup**:

   - Navigate to the `backend` directory:
     ```
     cd MediStream/backend
     ```

   - Install Python dependencies:
     ```
     pip install -r requirements.txt
     ```

   - Create the database:
     ```
     python manage.py migrate
     ```

   - Start the Django development server:
     ```
     python manage.py runserver
     ```

3. **Frontend Setup**:

   - Navigate to the `frontend` directory:
     ```
     cd MediStream/frontend
     ```

   - Install Node.js dependencies:
     ```
     npm install
     ```

   - Start the React development server:
     ```
     npm start
     ```

4. **Access MediStream**:

   - Open your web browser and visit `http://localhost:3000` to access MediStream.

## Usage

1. **User Registration**:
   - Users can't be directly registered on this site but are pulled from the CUREMD database for security and compliance. 

2. **Login**:
   - Registered users can log in to their accounts.

3. **Dashboard**:
   - The dashboard provides an overview of a user's patients and their corresponding medical notes.

4. **Create Notes**:
   - Users can create various types of medical notes using predefined templates or custom templates.

5. **Edit and Save Notes**:
   - Notes can be edited, and changes are saved automatically.

6. **Export and Print**:
   - Completed notes can be exported in PDF format or printed directly.

7. **Collaboration**:
   - Multiple users can collaborate on the same patient's notes, ensuring comprehensive and accurate documentation.

## Database Access

Please note that MediStream relies on a secured and proprietary database owned and managed by CUREMD. Access to this database is restricted to authorized personnel only for privacy, security, and compliance reasons.

The database used in MediStream contains sensitive patient data and must be protected in accordance with healthcare industry regulations and best practices. Therefore, it is not publicly accessible or included as part of this open-source project.

If you are interested in deploying and using MediStream in your own environment, you will need to set up your own database or contact CUREMD directly to inquire about the availability of database access for integration with this platform.

For inquiries regarding database access or any other questions related to MediStream, please contact [CUREMD Support](mailto:support@curemd.com).

Please note that using sensitive patient data without proper authorization and compliance with healthcare regulations is strictly prohibited.
