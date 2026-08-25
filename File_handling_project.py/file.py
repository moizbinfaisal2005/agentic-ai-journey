from pydantic import BaseModel
from typing import List
from google import genai
import os
from dotenv import load_dotenv

# 1. Define schema
class ActionItem(BaseModel):
    task: str
    owner: str

class ActionItems(BaseModel):
    items: List[ActionItem]

# 2. Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key="api_key")

# 3. Read meeting notes
with open("meeting.txt", "r", encoding="utf-8") as f:
    document = f.read()

# 4. Ask LLM to extract structured action items
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
    Here is a meeting transcript:
    {document}

    Extract action items from these meeting notes.
    Each item must have:
    - task (string)
    - owner (string)

    Respond ONLY in valid JSON like:
    {{
      "items": [
        {{ "task": "Prepare Q3 budget draft by Friday", "owner": "Sarah" }},
        {{ "task": "Follow up with vendor on shipment delays", "owner": "Ali" }}
      ]
    }}
    """
)

# print("Raw response text:", repr(response.text))

import json
import re

raw = response.text.strip()

# # Remove leading ```json or '''json fences if present
clean = re.sub(r"^(```json|'''json)\s*", "", raw)
clean = re.sub(r"(```|''')$", "", clean).strip()

data = json.loads(clean)

with open("summary.txt", "w", encoding="utf-8") as f:
    for item in data["items"]:
        f.write(f"{item['owner']}: {item['task']}\n")

with open("action_items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("action_items.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

for item in loaded["items"]:
    print(f"{item['owner']} → {item['task']}")











   
 


