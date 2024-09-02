# GPT message wrapper

## Overview

This project is a Python-based HTTP server that processes POST requests to generate responses using OpenAI's ChatGPT API. The server takes a user message, wraps it in a predefined prompt, and then sends it to the ChatGPT API. The API's response is returned in a structured JSON format.

## Features

- Receives POST requests on the `/message` endpoint.
- Validates the incoming JSON payload to ensure it contains the required fields: `user_id`, `message`, and `msg_id`.
- Sends a formatted message to the ChatGPT API and returns the API's response in a JSON structure.

## Setup

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.6 or higher
- Pip (Python package installer)
- An [OpenAI API Key](https://platform.openai.com/)

### Installation

1. **Clone the repository:**

   First, clone the project repository to your local machine using the following command:

   ```bash
   git clone https://github.com/aleksanyanV/gpt_message_wrapper.git
   cd python_test_task

2. **Create and activate a virtual environment:**

    Next, create and activate a virtual environment to manage your dependencies:
    ```bash
      python3 -m venv venv
      source venv/bin/activate

3.  **Install the required Python packages:**
    ```bash
      pip install -r requirements.txt

4.  **Set up environment variables:**
    ```bash
     Rename the .env.example file to .env:

5.  **Run the application:**
    ```bash
     python3 app/main.py

## Usage

Once the server is running, you can interact with it by sending POST requests to the `/message` endpoint. Below are examples of how to do this using `curl` and Postman.

### Example Request Using `curl`

You can use the following `curl` command in your terminal to send a POST request to the server:

```bash
curl -X POST http://localhost:8080/message \
-H "Content-Type: application/json" \
-d '{
  "user_id": "1234",
  "message": "Hello, how are you?",
  "msg_id": "msg001"
}'
