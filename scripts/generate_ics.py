from datetime import datetime

with open("gamer.ics", "w", encoding="utf-8") as f:
    f.write(
f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Gamer Hub//PT-BR//EN

BEGIN:VEVENT
UID:teste-python
DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}
DTSTART;VALUE=DATE:20260610
DTEND;VALUE=DATE:20260611
SUMMARY:Evento criado pelo Python
DESCRIPTION:Primeiro evento gerado automaticamente.
END:VEVENT

END:VCALENDAR
"""
)

print("Calendário gerado.")
