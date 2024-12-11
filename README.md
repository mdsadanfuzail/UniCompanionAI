# UniCompanionAI

UniCompanionAI is a chatbot application designed to assist students of a specific university in understanding and navigating their syllabus, rules, and regulations. The chatbot utilizes advanced AI models to simplify complex university-related documents and provide personalized answers to student queries. This project aims to make students' lives easier by providing quick access to critical university information.

## Features

- **Curriculum Assistance**: Helps students understand the syllabus for different courses and subjects.
- **Rules & Regulations**: Provides easy-to-understand explanations of university rules and regulations.
- **Personalized Answers**: Uses advanced AI models to give accurate, context-based responses to student questions.
- **Text-based Interface**: A user-friendly text-based interface for easy communication with the chatbot.
- **API Integration**: Exposes endpoints for interacting with the chatbot via FastAPI.

## Tech Stack

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - [FastAPI](https://fastapi.tiangolo.com/) for building the backend API
  - [LangChain](https://www.langchain.com/) for building the RAG pipeline
  - [Cohere API](https://cohere.ai/) for chatbot model integration
  - [Chroma](https://www.trychroma.com/) for vector storage and retrieval
  - [Docx2txt](https://github.com/Alir3z4/docx2txt) for parsing DOCX files
- **Database**: Chroma (Vector store for document retrieval)
- **Hosting**: GitHub (for version control)

## Installation

To run UniCompanionAI locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/UniCompanionAI.git
   ```

2. Navigate to the project folder:
   ```bash
   cd UniCompanionAI
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with your **Cohere API Key**:
   - Create a `.env` file in the root directory of the project.
   - Add the following content:
     ```
     API_KEY=your_cohere_api_key_here
     VECTORSTORE_EXISTS=false
     ```
   - Once the vectorstore is created, set `VECTORSTORE_EXISTS=true`.

## Usage

### Running the Application

1. Start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8006`.

## Project Structure

```
UniCompanionAI/
|
├── backend/                 # Contains the backend folder
│   ├── app.py               # Contains FastAPI application instance and API routes
│   ├── main.py              # Entry point for running the FastAPI application
│   ├── pipeline.py          # Setup for the RAG pipeline (Cohere API and document retrieval)
│   ├── loaders.py           # Handles loading and processing of university-specific documents
│   ├── vectorstore.py       # Manages Chroma vector store for document retrieval and storage
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., Cohere API Key, VECTORSTORE_EXISTS)
├── README.md                # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to Cohere for providing the powerful LLM used in this project.
- Thanks to LangChain for helping to streamline the creation of the RAG pipeline.
- Thanks to FastAPI for enabling a robust and user-friendly backend for this application.
