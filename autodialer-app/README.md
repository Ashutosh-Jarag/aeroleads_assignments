# 📞 AI AutoDialer

The AI AutoDialer is a Flask-based web application that automates the process of making introductory sales calls. It uses Twilio for making calls and Google's Gemini AI to generate dynamic, personalized call scripts.

## ✨ Features

-   **Web Interface**: Simple and intuitive web form to input lead details.
-   **Dynamic Script Generation**: Uses Google's Gemini AI to create a unique call script for each lead based on their name and the product.
-   **Automated Calling**: Integrates with Twilio to automatically place calls.
-   **Call Logging**: Records every call attempt and its status in a `call_logs.csv` file.

## 🛠️ Prerequisites

-   Python 3.8+
-   A Twilio account with a phone number.
-   A Google AI Studio API key.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd aeroleads/autodialer-app
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a file named `.env` in the `autodialer-app` directory and add your credentials:

```env
TWILIO_ACCOUNT_SID="your_twilio_account_sid"
TWILIO_AUTH_TOKEN="your_twilio_auth_token"
TWILIO_PHONE="your_twilio_phone_number"
GOOGLE_API_KEY="your_google_api_key"
```

### 5. Run the Application

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

##  usage

1.  Open your web browser and navigate to `http://127.0.0.1:5000`.
2.  Fill in the lead's name, phone number, and the product you are promoting.
3.  Click "Start Call".
4.  The application will generate a script, make the call, and log the result.

## 📄 Project Structure

```
autodialer-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── call_logs.csv       # Log of all calls made
├── templates/
│   └── index.html      # Web interface
└── .env                # Environment variables (create this file)
```
