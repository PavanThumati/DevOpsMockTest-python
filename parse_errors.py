import re
import json

log_path = "/tmp/timestamp.log"
output_path = "errors.json"

# Regex to match ERROR lines and extract timestamp + message
pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+-\s*ERROR\s+-\s+(.*)$")

errors = []

with open(log_path, "r") as f:
    for line in f:
        match = pattern.match(line)
        if match:
            timestamp, message = match.groups()
            errors.append({"timestamp": timestamp, "error": message})

# Save to JSON
with open(output_path, "w") as f:
    json.dump(errors, f, indent=4)

print(f"Extracted {len(errors)} error(s) and saved to {output_path}")

