# Birthday Email Sender

This project is a simple Python script that reads birthday data from a CSV file and sends a birthday email to the individuals whose birthday matches today's date. The email contains a randomly selected birthday message.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## Introduction

The Birthday Email Sender script reads a list of birthdays from a CSV file and sends a personalized birthday email to each individual whose birthday is today. It uses the `pandas` library for data manipulation, `smtplib` for sending emails, and `random` for selecting a random birthday message.

## Features

- Reads birthday data from a CSV file
- Filters and identifies birthdays that match today's date
- Sends personalized birthday emails with randomly selected messages

## Setup

### Prerequisites

- Python 3.x
- A Gmail account (or any other email service with appropriate SMTP settings)

### Installation

1. Clone the repository (or create a new directory and navigate into it):
    ```sh
    mkdir python-birthday-email
    cd python-birthday-email
    ```

2. Create a CSV file named `birthdays.csv` with the following structure:
    ```csv
    name,email,year,month,day
    John Doe,john.doe@example.com,1990,5,17
    Jane Smith,jane.smith@example.com,1985,5,18
    ```

3. Create a Python script file named `send_birthday_email.py` and paste the script content into this file.

4. Create a `requirements.txt` file with the following content:
    ```
    pandas
    ```

5. Set up a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

6. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script, navigate to the project directory and execute the following command:

```sh
python send_birthday_email.py
