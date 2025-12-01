# Medical Chatbot 🏥

An intelligent medical chatbot powered by Google's Gemini AI, LangChain, and Pinecone vector database. This application provides accurate medical information by leveraging Retrieval-Augmented Generation (RAG) to answer health-related questions based on medical documents.

## 🌟 Features

- **AI-Powered Responses**: Uses Google Gemini 2.5 Pro for intelligent medical question answering
- **RAG Architecture**: Retrieval-Augmented Generation ensures accurate, context-aware responses
- **Vector Search**: Pinecone vector database for efficient similarity search
- **Modern UI**: Beautiful, responsive chat interface with animations and glassmorphism effects
- **Real-time Interaction**: Instant responses with typing indicators and smooth animations
- **Document Processing**: Automatically processes PDF medical documents for knowledge base

## 📋 Prerequisites

- Python 3.10 or higher
- Conda (Anaconda or Miniconda)
- Google API Key (for Gemini AI)
- Pinecone API Key (for vector database)

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/JoelJohnsonThomas/Medical-Chatbot.git
cd Medical-Chatbot
```

### Step 2: Create a Conda Environment
Create a new Conda environment named `Medical-Chatbot` with Python 3.10:
```bash
conda create -n Medical-Chatbot python=3.10 -y
```

### Step 3: Activate the Environment
Activate the newly created environment:
```bash
conda activate Medical-Chatbot
```

### Step 4: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Step 1: Set Up Environment Variables
Create a `.env` file in the root directory with your API keys:
```env
PINECONE_API_KEY=your_pinecone_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

**How to get API keys:**
- **Google API Key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to create your API key
- **Pinecone API Key**: Sign up at [Pinecone](https://www.pinecone.io/) and get your API key from the dashboard

### Step 2: Prepare Medical Documents
Place your medical PDF documents in the `data/` directory. These documents will be used to build the knowledge base.

## 📊 Data Indexing

Before running the chatbot, you need to create the vector index from your medical documents:

```bash
python store_index.py
```

This script will:
1. Load PDF documents from the `data/` directory
2. Split documents into manageable chunks
3. Generate embeddings using HuggingFace's sentence-transformers
4. Create/update the Pinecone vector index named "medical-chatbot"

**Note**: This step only needs to be run once, or when you add new documents to the knowledge base.

## 🎯 Running the Application

### Start the Flask Server
```bash
python app.py
```

The application will start on `http://localhost:5000`

### Access the Chatbot
Open your web browser and navigate to:
```
http://localhost:5000
```

You can now start asking medical questions!

## 📁 Project Structure

```
Medical-Chatbot/
├── app.py                      # Flask application and API endpoints
├── store_index.py              # Script to create Pinecone vector index
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API keys)
├── data/                       # Medical PDF documents
├── src/
│   ├── helper.py              # Helper functions for PDF loading and processing
│   └── prompt.py              # System prompts for the AI model
├── templates/
│   └── chat.html              # Chat interface HTML
└── static/
    └── style.css              # Styling for the chat interface
```

## 🛠️ Technology Stack

- **Backend Framework**: Flask 3.1.1
- **AI Model**: Google Gemini 2.5 Pro
- **LLM Framework**: LangChain 0.3.26
- **Vector Database**: Pinecone
- **Embeddings**: HuggingFace sentence-transformers (all-MiniLM-L6-v2)
- **Document Processing**: PyPDF 5.6.1
- **Frontend**: HTML, CSS, JavaScript with modern animations

## 🔧 Key Components

### RAG Pipeline
1. **Document Loading**: PDFs are loaded from the `data/` directory
2. **Text Splitting**: Documents are split into 500-character chunks with 20-character overlap
3. **Embedding**: Text chunks are converted to 384-dimensional vectors
4. **Vector Storage**: Embeddings are stored in Pinecone for similarity search
5. **Retrieval**: Top 3 most relevant chunks are retrieved for each query
6. **Generation**: Gemini AI generates responses based on retrieved context

### API Endpoints
- `GET /`: Renders the chat interface
- `POST /get`: Processes user messages and returns AI responses

## 💡 Usage Tips

- Ask specific medical questions for best results
- The chatbot uses a concise response format (max 3 sentences)
- If the chatbot doesn't know an answer, it will honestly say so
- Responses are based on the medical documents in your knowledge base

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Joel Johnson Thomas**
- GitHub: [@JoelJohnsonThomas](https://github.com/JoelJohnsonThomas)

## 🙏 Acknowledgments

- Google Gemini AI for powerful language understanding
- LangChain for the RAG framework
- Pinecone for vector database infrastructure
- HuggingFace for embedding models