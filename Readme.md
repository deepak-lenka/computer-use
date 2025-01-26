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