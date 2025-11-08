# 📝 AI Blog Generator

The AI Blog Generator is a powerful tool that leverages Google's Gemini AI, LangChain, and LangGraph to automatically generate high-quality, SEO-friendly blog posts from a list of titles.

## ✨ Features

-   **Bulk Blog Generation**: Input multiple blog titles and generate them all at once.
-   **LangGraph Integration**: Utilizes a simple LangGraph workflow for content generation.
-   **Web Interface**: A user-friendly web interface for easy interaction.
-   **File Storage**: Automatically saves each generated blog post as a Markdown file.
-   **SEO-Friendly**: Prompts are designed to generate content that is optimized for search engines.

## 🛠️ Prerequisites

-   Python 3.8+
-   A Google AI Studio API key.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd aeroleads/blog_generator
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a file named `.env` in the `blog_generator` directory and add your Google API key:

```env
GOOGLE_API_KEY="your_google_api_key"
```

### 5. Run the Application

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

## 💡 How to Use

1.  Open your web browser and go to `http://127.0.0.1:5000`.
2.  In the text area, enter the titles of the blogs you want to generate, with each title on a new line.
3.  Click "Generate Blogs".
4.  The generated articles will be displayed on the page and saved as individual `.md` files in the `blog/` directory.

## 📄 Project Structure

```
blog_generator/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Web interface
├── blog/               # Directory for generated blog files
└── .env                # Environment variables (create this file)
```