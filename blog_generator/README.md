# 📝 Blog Generator

A Python-based application designed to automatically generate blog content using the Google Gemini API.

## 🚀 Project Structure

```
blog_generator/
├── .env                  # Environment file to store your API Key (ignored by git)
├── requirements.txt      # List of required Python packages
├── generator.py          # Core script for blog generation
└── README.md             # Documentation
```

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- Git (for Git method only)

---

# 📥 Installation Guide

Choose one of the two methods below to get started with the project.

---

## Method 1: Download Normally (Direct Download)

### ✅ Step 1: Get Your API Key First

Before downloading, obtain your Gemini API key:

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Create API key"** and follow the prompts
4. Copy and securely store the generated key

### ⬇️ Step 2: Download the Repository

1. Visit the [GitHub repository](https://github.com/Ashutosh-Jarag/aeroleads_assignments)
2. Click the green **"Code"** button at the top right
3. Select **"Download ZIP"** from the dropdown menu
4. Save and extract the ZIP file to your desired location

### 📁 Step 3: Navigate to the Project Directory

Extract the downloaded ZIP file and open your terminal in the `blog_generator` folder:

```bash
cd path/to/aeroleads_assignments/blog_generator
```

Replace `path/to/` with the actual path where you extracted the files.

### 🔧 Step 4: Create a Virtual Environment

Creating a virtual environment isolates your project dependencies:

```bash
python -m venv venv
```

Activate the environment:

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows (Command Prompt):**

```bash
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

You should see `(venv)` in your terminal prompt.

### 📦 Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Step 6: Configure Your API Key

1. Create a `.env` file in the `blog_generator` directory (at the same level as `requirements.txt` and `generator.py`)
2. Add the following line, replacing with your actual API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

Save the file.

### ▶️ Step 7: Run the Application

```bash
python generator.py
```

The script will:
1. Read your input (blog topic, keywords, etc.)
2. Send a request to the Google Gemini API
3. Display the generated blog post or save it to a file

### ⏹️ Step 8: Deactivate Virtual Environment

When finished:

```bash
deactivate
```

---

## Method 2: Using Git (Recommended for Developers)

### ✅ Step 1: Get Your API Key First

Before cloning, obtain your Gemini API key:

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Create API key"** and follow the prompts
4. Copy and securely store the generated key

### 📥 Step 2: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/Ashutosh-Jarag/aeroleads_assignments.git
```

This creates a folder named `aeroleads_assignments` with all project files.

### 📁 Step 3: Navigate to the Project Directory

```bash
cd aeroleads_assignments/blog_generator
```

### 🔧 Step 4: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows (Command Prompt):**

```bash
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

You should see `(venv)` in your terminal prompt.

### 📦 Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Step 6: Configure Your API Key

1. Create a `.env` file in the `blog_generator` directory (at the same level as `requirements.txt` and `generator.py`)
2. Add the following line, replacing with your actual API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

Save the file.

### ▶️ Step 7: Run the Application

```bash
python generator.py
```

The script will:
1. Read your input (blog topic, keywords, etc.)
2. Send a request to the Google Gemini API
3. Display the generated blog post or save it to a file

### 🔄 Step 8: (Optional) Keep Your Repository Updated

To pull the latest changes from the repository:

```bash
git pull origin main
```

### ⏹️ Step 9: Deactivate Virtual Environment

When finished:

```bash
deactivate
```

---

## 📋 Requirements

The project uses the following Python packages (specified in `requirements.txt`):

- `google-genai` – Google Gemini API client
- `python-dotenv` – For loading environment variables from `.env`

## 🐛 Troubleshooting

**Issue: "ModuleNotFoundError" when running the script**
- Ensure your virtual environment is activated and all dependencies are installed with `pip install -r requirements.txt`

**Issue: "API key not found" error**
- Verify the `.env` file exists in the correct directory
- Check that `GEMINI_API_KEY` is set correctly with your actual key
- Restart your terminal after creating the `.env` file

**Issue: "Permission denied" on macOS/Linux**
- Try running `chmod +x generator.py` to make the script executable

**Issue: Git command not found**
- Install Git from [git-scm.com](https://git-scm.com) if using the Git method

**Issue: Python command not found**
- Ensure Python 3.8+ is installed: [python.org](https://www.python.org/downloads/)

## 📊 Comparison: Download vs Git

| Feature | Download (ZIP) | Git Clone |
|---------|---|---|
| **Ease of Use** | Simple, no Git knowledge needed | Requires Git familiarity |
| **Updates** | Manual re-download required | One command (`git pull`) |
| **Version Control** | No history tracking | Full commit history available |
| **Collaboration** | Not ideal for contributions | Perfect for contributing changes |
| **File Size** | Slightly smaller (no `.git` folder) | Includes `.git` metadata |

## 📚 Additional Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
- [Git Documentation](https://git-scm.com/doc)
- [Python Installation Guide](https://www.python.org/downloads/)

## 📄 License

This project is part of the AeroLeads assignments repository.

---

**Happy blogging! 🚀**
