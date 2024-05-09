# FastAPI with OpenAI Assistant API Integration

## Overview

This project demonstrates how to integrate FastAPI with OpenAI's Assistant API, utilizing Server-Sent Events (SSE) for real-time streaming of responses. The application allows creating interactive sessions with an OpenAI Assistant, handling real-time data streaming, and showcasing how asynchronous communication can enhance user interaction.

## Features

- Assistant Setup: Configures OpenAI Assistant API.
- Thread Management: Create and manage conversation threads.
- Real-time Streaming: Utilize SSE for streaming from the OpenAI Assistant.
- Functionality Extension: Placeholder for future function calling integration.

## Getting Started

### Prerequisites

- Python 3.10+
- FastAPI
- Uvicorn (for running the application)
- OpenAI Python client

### Installation

Clone the repository:

```bash
git clone https://github.com/xbreid/fastapi-assistant-streaming.git
cd fastapi-assistant-streaming
```

Install required packages:

```bash
pip install -r requirements.txt
```

Set up environment variables:
Create a .env file in the project root directory and add your OpenAI API key and Assistant ID:

```bash
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ASSISTANT_ID=your_assistant_id_here
```

### Running the Application

Start the FastAPI Development Server:

```bash
fastapi dev main.py
```

### Testing Endpoints

Check the Health:

```bash
curl -X 'GET' --url 'http://localhost:8000/'
```

Get the Assistant:

```bash
curl -X 'GET' --url 'http://localhost:8000/api/v1/assistant'
```

Create a thread:

```bash
curl -X POST http://localhost:8000/api/v1/assistant/threads -H "Content-Type: application/json"
```

Send a message:

```bash
curl -N -X POST \
-H "Accept: text/event-stream" -H "Content-Type: application/json" \
-d '{"text": "Hello! Please introduce yourself", "thread_id": "thread_abc123" }' \
http://localhost:8000/api/v1/assistant/chat
```

## Contributing

Contributions are always welcome!

## License

Distributed under the MIT License. See LICENSE for more information.
