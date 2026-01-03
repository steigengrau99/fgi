import requests
import json
from datetime import datetime

URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resp = requests.get(URL, headers=headers)
data = resp.json()

fg = data["fear_and_greed"]

output = {
    "timestamp": datetime.utcnow().isoformat(),
    "score": fg["score"],
    "rating": fg["rating"],
    "previous_close": fg["previous_close"],
    "one_week_ago": fg["last_week"],
    "one_month_ago": fg["last_month"]
}

with open("fear_greed.json", "w") as f:
    json.dump(output, f, indent=2)
