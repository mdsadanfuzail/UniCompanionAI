
# StudyBuddyAU

StudyBuddyAU is a chatbot application designed to assist students of a specific university in understanding and navigating their syllabus, rules, and regulations. The chatbot utilizes advanced AI models to simplify complex university-related documents and provide personalized answers to student queries. This project aims to make students' lives easier by providing quick access to critical university information.

## Features

- **Curriculum Assistance**: Helps students understand the syllabus for different courses and subjects.
- **Rules & Regulations**: Provides easy-to-understand explanations of university rules and regulations.
- **Personalized Answers**: Uses advanced AI models to give accurate, context-based responses to student questions.
- **Text-based Interface**: A user-friendly text-based interface for easy communication with the chatbot.

## Tech Stack

- **Programming Language**: Python
- **Libraries/Frameworks**:
  - [LangChain](https://www.langchain.com/) for building the pipeline
  - [Cohere API](https://cohere.ai/) for Natural Language Processing (NLP)
  - [Chroma](https://www.trychroma.com/) for vector storage and retrieval
  - [OpenAI](https://openai.com/) for chatbot model integration
  - [Docx2txt](https://github.com/Alir3z4/docx2txt) for parsing DOCX files
- **Database**: Chroma (Vector store for document retrieval)
- **Hosting**: GitHub (for version control)

## Installation

To run StudyBuddyAU locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/StudyBuddyAU.git
   ```

2. Navigate to the project folder:
   ```bash
   cd StudyBuddyAU
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
   - Once vectorstore is created make VECTORSTORE_EXISTS=true


## Usage

Once the environment is set up, you can run the chatbot application:

1. Run the main application:
   ```bash
   python main.py
   ```

2. The application will prompt you to ask questions about your university's syllabus, rules, and regulations. You can interact with the chatbot by typing questions.

## Project Structure

- `main.py`: The main entry point for running the chatbot application.
- `pipeline.py`: Contains the RAG pipeline setup, including the integration with Cohere API and document retrieval.
- `loaders.py`: Handles loading and processing of university-specific documents (e.g., syllabus, regulations) in DOCX format.
- `vectorstore.py`: Manages the Chroma vector store for efficient document retrieval.
- `requirements.txt`: Lists the Python dependencies for the project.
- `.env`: Contains environment variables like API keys (ensure this file is not publicly accessible).
- `README.md`: This file.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to Cohere for providing the powerful LLM used in this project.
- Thanks to LangChain for helping to streamline the creation of the RAG pipeline.
