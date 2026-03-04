Here’s a **cleaned-up, properly formatted version** of your README that’s ready to use — fixed Markdown formatting and headings:

````markdown
# My Weather Agent

This project runs `my_weather_agent`, a Python-based agent that fetches weather information using Google and Weather APIs.

---

## ⚡ Prerequisites

Before running the agent, make sure to **set your API keys** in your environment:

```bash
export GOOGLE_API_KEY="your_google_api_key_here"
export WEATHER_API_KEY="your_weather_api_key_here"
````

> Replace the values with your actual API keys.

---

## 🐍 Setup

1. **Create a virtual environment:**

```bash
python -m venv venv
```

2. **Activate the virtual environment:**

```bash
# macOS / Linux
source venv/bin/activate

# Windows
# venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Agent

Start the agent using `adk`:

```bash
adk run my_weather-agent
```

The agent will now be live and ready to fetch weather information for requested locations.

---

## 📌 Notes

* Ensure both `GOOGLE_API_KEY` and `WEATHER_API_KEY` are valid.
* The agent relies on network connectivity to call external APIs.
* For development, you can run multiple queries; make sure to respect the API rate limits.

---

## 🛠 Troubleshooting

* **Invalid API Key:** Double-check that you exported the correct key.
* **Dependencies missing:** Run `pip install -r requirements.txt` again inside the activated virtual environment.
* **Agent not starting:** Ensure `adk` is installed and available in your PATH.