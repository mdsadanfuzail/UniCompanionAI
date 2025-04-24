# UniCompanionAI

UniCompanionAI is a chatbot application designed to assist students of a specific university in understanding and navigating their syllabus, rules, and regulations. The chatbot utilizes advanced AI models to simplify complex university-related documents and provide personalized answers to student queries. This project aims to make students' lives easier by providing quick access to critical university information.

## Features

- **Curriculum Assistance**: Helps students understand the syllabus for different courses and subjects.
- **Rules & Regulations**: Provides easy-to-understand explanations of university rules and regulations.
- **Personalized Answers**: Uses advanced AI models to give accurate, context-based responses to student questions.
- **Text-based Interface**: A user-friendly text-based interface for easy communication with the chatbot.

## Tech Stack

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - [LangChain](https://www.langchain.com/) for building the RAG pipeline
  - [Cohere API](https://cohere.ai/) for chatbot model integration
  - [Chroma](https://www.trychroma.com/) for vector storage and retrieval
  - [Gradio](https://www.gradio.app/) for creating a web interface to interact with the chatbot

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
     COHERE_API_KEY="your_cohere_api_key_here"
     ```

## Usage

### Running the Application

1. Run the Chatbot.py

2. Use the Gradio frontent to interact with chatbot.

## Project Structure

```
UniCompanionAI/
|
├── chromadb                 # Chroma Vector Database
├── Ingestion.py             # Contains the data ingestion using RAG
├── app.py                   # Main chatbot application
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., COHERE_API_KEY)
├── README.md                # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to Cohere for providing the powerful LLM used in this project.
- Thanks to LangChain for helping to streamline the creation of the RAG pipeline.
- Thanks to Gradio for providing an intuitive and interactive UI for seamless user-chatbot communication.
