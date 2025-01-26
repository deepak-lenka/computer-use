# Computer Use Automation 🤖

A Python-based browser automation project that demonstrates autonomous web navigation and interaction using LangChain and Playwright. This project showcases how AI can be used to automate complex web interactions with natural language instructions.

## Features 🌟
- AI-powered browser automation using GPT-4
- Natural language task descriptions
- Automatic error handling and retries
- Visual interaction tracking
- State verification and validation

## Requirements 📋
- Python 3.13.1 or higher
- OpenAI API key
- Playwright browsers

## Installation 🔧

1. Clone the repository:
```bash
git clone https://github.com/deepak-lenka/computer-use.git
cd computer-use
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Unix/macOS
```

3. Install dependencies:
```bash
pip install langchain-openai playwright python-dotenv
```

4. Install Playwright browsers:
```bash
playwright install
```

5. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file with your OpenAI API key
```

## Usage 🚀

Run the example script:
```bash
python3 agent.py
```

## Example Task 📝

```python
task = """
1. Navigate directly to YouTube.com/@OpenAI
2. Wait for page load and handle cookie consent
3. Click the 'Videos' tab
4. Find the most recent upload
5. Play and verify video playback
"""
```

## Project Structure 📁
- `agent.py`: Main script containing the automation logic
- `browser_use`: Browser automation module
- `.env`: Configuration file for API keys
- `agent_history.gif`: Visual recording of the automation

## Contributing 🤝
Feel free to open issues or submit pull requests for improvements!

## License 📄
[MIT License](LICENSE)

## YouTube Automation Example ▶️

**Task:**  
"Navigate to OpenAI's YouTube channel, play latest video, verify playback"

### Execution Flow 🔄
1. **Direct Navigation**  
   `https://www.youtube.com/@OpenAI` loaded successfully

2. **Content Selection**  
   - Clicked 'Videos' tab (index 33)
   - Selected latest upload "Using saved prompts in Operator" (index 45)

3. **Playback Handling**  
   - Initial play button click failed (index 17)
   - Retry logic activated:
     ```python
     {"click_element":{"index":13}}
     {"click_element":{"index":14}}  # Success!
     ```

4. **Verification**  
   - ✅ Time progress bar movement
   - ✅ Audio/video sync
   - ❌ Error messages

### Key Features Demonstrated 🛠️
```python
{
  "error_handling": "Automatic retry on failed clicks",
  "state_verification": "Playback confirmation checks",
  "memory": "Persistent context between steps",
  "visual_tracking": "AgentHistory.gif generated"
}
```