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
- Git

## ⚙️ Setup and Installation

Follow these step-by-step instructions to set up the project on your local machine.

### 1. Clone the Repository

Open your terminal and clone the project:

```bash
git clone https://github.com/Ashutosh-Jarag/aeroleads_assignments.git
```

### 2. Navigate to the Project Directory

```bash
cd aeroleads_assignments/blog_generator
```

### 3. Create a Virtual Environment (Recommended)

Creating a virtual environment isolates your project dependencies and prevents conflicts with other Python projects.

Create the environment:

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

You should see `(venv)` appear in your terminal prompt, indicating the environment is active.

### 4. Install Dependencies

Install all required packages from the requirements file:

```bash
pip install -r requirements.txt
```

## 🔑 Gemini API Key Configuration

This application requires a Gemini API Key to function.

### Getting Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Create API key"** and follow the prompts
4. Copy the generated key immediately and store it securely

### Setting Up the Environment Variable

1. Create a `.env` file in the `blog_generator` directory (at the same level as `requirements.txt` and `generator.py`)
2. Add the following line to the `.env` file, replacing the placeholder with your actual API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

The application uses `python-dotenv` to automatically load this key when the script runs.

## ▶️ Running the Application

With your virtual environment activated and API key configured, run the blog generator:

```bash
python generator.py
```

### What the Script Does

1. **Reads Input** – Prompts you for a blog topic, keywords, or other parameters
2. **Calls Gemini** – Sends a request to the Google Gemini API with your input
3. **Generates Output** – Displays the generated blog post in the terminal or saves it to a file

### Deactivating the Virtual Environment

When you're finished, deactivate the virtual environment:

```bash
deactivate
```

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

## 📚 Additional Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [python-dotenv Documentation](https://python-dotenv.readthedocs.io/)

## 📄 License

This project is part of the AeroLeads assignments repository.

---

**Happy blogging! 🚀**
