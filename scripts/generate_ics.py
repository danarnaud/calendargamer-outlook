import json
from datetime import datetime

with open("data/events.json", "r", encoding="utf-8") as f:
    events = json.load(f)

lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Gamer Hub//PT-BR//EN"
]

for event in events:
    start = event["start"].replace("-", "")
    end = event["end"].replace("-", "")

    lines.extend([
        "BEGIN:VEVENT",
        f"UID:{event['uid']}",
        f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
        f"DTSTART;VALUE=DATE:{start}",
        f"DTEND;VALUE=DATE:{end}",
        f"SUMMARY:{event['title']}",
        f"DESCRIPTION:{event['description']}",
        "END:VEVENT"
    ])

lines.append("END:VCALENDAR")

with open("docs/gamer.ics", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("ICS gerado com sucesso.")
