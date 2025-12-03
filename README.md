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

The application will start on `http://localhost:8080`

### Access the Chatbot
Open your web browser and navigate to:
```
http://localhost:8080
```

You can now start asking medical questions!

## 🚀 AWS CI/CD Deployment with GitHub Actions

Deploy your Medical Chatbot to AWS EC2 with automated CI/CD using GitHub Actions, Docker, and Amazon ECR.

### 📋 Deployment Overview

The deployment architecture follows this workflow:
1. **Build** Docker image from source code
2. **Push** Docker image to Amazon ECR (Elastic Container Registry)
3. **Deploy** Pull image from ECR to EC2 instance
4. **Run** Launch Docker container on EC2

### Prerequisites

- AWS Account with appropriate permissions
- GitHub repository for the project
- Basic familiarity with AWS services (EC2, ECR, IAM)

---

### Step 1: Create IAM User for Deployment

Create an IAM user with programmatic access for GitHub Actions to interact with AWS services.

1. **Login to AWS Console** and navigate to **IAM** (Identity and Access Management)

2. **Create New User**:
   - Click **Users** → **Add users**
   - Enter username (e.g., `github-actions-deploy`)
   - Select **Access key - Programmatic access**

3. **Attach Policies**:
   Add the following managed policies to grant necessary permissions:
   - ✅ `AmazonEC2ContainerRegistryFullAccess` - For pushing/pulling Docker images
   - ✅ `AmazonEC2FullAccess` - For managing EC2 instances

4. **Save Credentials**:
   - Download and securely store the **Access Key ID** and **Secret Access Key**
   - ⚠️ You won't be able to view the secret key again!

---

### Step 2: Create Amazon ECR Repository

Set up a container registry to store your Docker images.

1. **Navigate to Amazon ECR** in AWS Console

2. **Create Repository**:
   - Click **Create repository**
   - Repository name: `medicalbot`
   - Keep default settings (Private repository)
   - Click **Create repository**

3. **Save Repository URI**:
   - Copy the repository URI (e.g., `315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot`)
   - You'll need this for GitHub secrets

---

### Step 3: Launch and Configure EC2 Instance

Create an Ubuntu EC2 instance to host your application.

#### 3.1 Launch EC2 Instance

1. **Navigate to EC2** in AWS Console
2. **Launch Instance**:
   - Name: `medical-chatbot-server`
   - AMI: **Ubuntu Server 22.04 LTS**
   - Instance type: `t2.large` (or larger based on needs)
   - Create or select a key pair for SSH access
   - **Security Group**: Configure inbound rules:
     - SSH (22) - Your IP
     - HTTP (80) - Anywhere
     - Custom TCP (8080) - Anywhere (for the application)
3. **Launch** the instance

#### 3.2 Install Docker on EC2

Connect to your EC2 instance via SSH and run the following commands:

```bash
# Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add ubuntu user to docker group
sudo usermod -aG docker ubuntu

# Activate the changes to groups
newgrp docker

# Verify Docker installation
docker --version
```

---

### Step 4: Configure EC2 as Self-Hosted Runner

Set up your EC2 instance as a GitHub Actions self-hosted runner.

1. **Navigate to GitHub Repository**:
   - Go to **Settings** → **Actions** → **Runners**

2. **Add New Runner**:
   - Click **New self-hosted runner**
   - Select **Linux** as the operating system
   - Follow the provided commands

3. **Run Commands on EC2**:
   SSH into your EC2 instance and execute the commands provided by GitHub (example):

   ```bash
   # Download the runner
   mkdir actions-runner && cd actions-runner
   curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
   tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz
   
   # Configure the runner
   ./config.sh --url https://github.com/YOUR_USERNAME/Medical-Chatbot --token YOUR_TOKEN
   
   # Install and start the runner as a service
   sudo ./svc.sh install
   sudo ./svc.sh start
   ```

4. **Verify Runner Status**:
   - Check GitHub repository settings to confirm the runner shows as "Idle" (active)

---

### Step 5: Configure GitHub Secrets

Add required secrets to your GitHub repository for the CI/CD workflow.

1. **Navigate to Repository Settings**:
   - Go to **Settings** → **Secrets and variables** → **Actions**

2. **Add Repository Secrets**:
   Click **New repository secret** and add each of the following:

   | Secret Name | Description | Example Value |
   |-------------|-------------|---------------|
   | `AWS_ACCESS_KEY_ID` | IAM user access key ID | `AKIAIOSFODNN7EXAMPLE` |
   | `AWS_SECRET_ACCESS_KEY` | IAM user secret access key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
   | `AWS_DEFAULT_REGION` | AWS region for ECR and EC2 | `us-east-1` |
   | `ECR_REPO` | ECR repository name | `medicalbot` |
   | `PINECONE_API_KEY` | Pinecone API key | Your Pinecone API key |
   | `GOOGLE_API_KEY` | Google Gemini API key | Your Google API key |

---

### Step 6: Understanding the CI/CD Workflow

The `.github/workflows/cicd.yaml` file defines the automated deployment pipeline:

#### **Continuous Integration Job**
Triggered on every push to the `main` branch:
1. Checkout code from repository
2. Configure AWS credentials
3. Login to Amazon ECR
4. Build Docker image from Dockerfile
5. Tag image as `latest`
6. Push image to ECR

#### **Continuous Deployment Job**
Runs after successful CI job:
1. Configure AWS credentials
2. Login to Amazon ECR
3. Pull the latest Docker image from ECR
4. Run Docker container on EC2 with environment variables
5. Expose application on port 8080

---

### Step 7: Deploy the Application

#### Trigger Deployment

Simply push your code to the `main` branch:

```bash
git add .
git commit -m "Deploy to AWS"
git push origin main
```

#### Monitor Deployment

1. **GitHub Actions**:
   - Navigate to **Actions** tab in your repository
   - Watch the workflow execution in real-time
   - Check for any errors in the logs

2. **Access Application**:
   - Once deployment completes, access your chatbot at:
   ```
   http://YOUR_EC2_PUBLIC_IP:8080
   ```
   - Find your EC2 public IP in the AWS EC2 console

---

### 🏗️ Deployment Architecture

```
┌─────────────────┐
│  Developer      │
│  Push to main   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│     GitHub Actions Workflow         │
│  ┌──────────────────────────────┐  │
│  │  Continuous Integration      │  │
│  │  • Build Docker Image        │  │
│  │  • Push to Amazon ECR        │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │  Continuous Deployment       │  │
│  │  • Pull from ECR             │  │
│  │  • Deploy to EC2             │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│     Amazon ECR                      │
│  Docker Image Repository            │
│  (medicalbot:latest)                │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│     EC2 Instance (Ubuntu)           │
│  • Self-hosted GitHub Runner        │
│  • Docker Container Running         │
│  • Application on Port 8080         │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│     Users Access Application        │
│  http://EC2_IP:8080                 │
└─────────────────────────────────────┘
```

---

### 🔧 Troubleshooting

#### Docker Permission Denied
```bash
# If you get permission errors, ensure user is in docker group
sudo usermod -aG docker $USER
newgrp docker
```

#### ECR Authentication Issues
```bash
# Manually login to ECR to test credentials
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URI
```

#### Port Already in Use
```bash
# Check what's using port 8080
sudo lsof -i :8080

# Stop existing container
docker ps
docker stop CONTAINER_ID
```

#### Check Running Containers
```bash
# View all running containers
docker ps

# View container logs
docker logs CONTAINER_ID

# Access container shell
docker exec -it CONTAINER_ID /bin/bash
```

#### Environment Variables Not Loading
- Verify all GitHub secrets are correctly set
- Check the workflow file for proper secret references
- Ensure `.env` file is not needed (secrets are passed via workflow)

---

## 📁 Project Structure

```
Medical-Chatbot/
├── .github/
│   └── workflows/
│       └── cicd.yaml          # GitHub Actions CI/CD workflow
├── app.py                      # Flask application and API endpoints
├── store_index.py              # Script to create Pinecone vector index
├── Dockerfile                  # Docker container configuration
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
- **Deployment**: Docker, AWS EC2, Amazon ECR, GitHub Actions

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