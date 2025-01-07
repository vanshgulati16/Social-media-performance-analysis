# Social Buzz Analyst 📊 

An AI-powered chatbot that provides detailed social media analytics and performance insights using natural language processing.

## Project Description
This project implements an intelligent chat interface that helps users analyze and optimize their social media performance. The assistant provides detailed insights, metrics analysis, and actionable recommendations for improving social media engagement and reach.

## Tech Stack
- **Frontend**: 
  - Streamlit (UI Framework)
  - HTML/CSS (Custom styling)

- **Backend**:
  - Python 3.11
  - LangFlow (AI Flow Management)
  - AstraDB (Database)

- **AI/ML**:
  - Google Generative AI (Gemini 1.5)
  - Embeddings Processing


## Project Flow
1. User inputs questions about social media performance
2. Request processed through LangFlow API
3. Google Generative AI analyzes the query
4. Response processed
5. Data presented in an intuitive chat interface
6. Insights stored in AstraDB for future reference

## Features
- Real-time chat interface
- Structured response formatting
- Session state management
- Detailed social media metrics analysis
- Custom styling and responsive design

## Setup and Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install streamlit requests
   ```
3. Put your credentials in ```.env```
    ```
    BASE_API_URL = "BASE_API_URL"
    LANGFLOW_ID = "LANGFLOW_ID"
    FLOW_ID = "FLOW_ID"
    APPLICATION_TOKEN = "APPLICATION_TOKEN"
    ```
3. Run the application:
   ```bash
   streamlit run chatbot.py
   ```

## Team Name
Bava

## Team Members
- Vansh Gulati
- Hrishav Basu 
