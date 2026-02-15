
import re
from datetime import date

class PersonalAgent:

    def __init__(self):
        self.today = date.today()
        self.month_map = {
            'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
            'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
        }

    def _parse_date(self, raw):
        raw = raw.strip().lower()

        numeric = r'^(\d{1,2})[-/\.](\d{1,2})[-/\.](\d{2,4})$'
        textual = r'^(\d{1,2})\s+([a-z]{3,})\s+(\d{4})$'

        m = re.match(numeric, raw)
        if m:
            a,b,y = m.groups()
            year = int(y) if len(y)==4 else (2000+int(y))
            try:
                return date(year, int(a), int(b))
            except:
                try:
                    return date(year, int(b), int(a))
                except:
                    return None

        m = re.match(textual, raw)
        if m:
            d, month_str, y = m.groups()
            month = self.month_map.get(month_str[:3])
            if month:
                try:
                    return date(int(y), month, int(d))
                except:
                    return None
        return None

    def compute_age(self, birth):
        years = self.today.year - birth.year
        if (self.today.month, self.today.day) < (birth.month, birth.day):
            years -= 1
        return years

    def mood_reply(self, text):
        if re.search(r'\b(happy|great|awesome|fine)\b', text, re.I):
            return "That’s wonderful to hear!"
        if re.search(r'\b(sad|bad|awful|upset)\b', text, re.I):
            return "I hope things improve soon."
        return "Thanks for sharing your thoughts."

    def launch(self):
        name = input("Your full name: ").strip()
        print("Hello,", name.split()[-1])

        while True:
            bd = input("Enter your birth date: ")
            parsed = self._parse_date(bd)
            if parsed:
                print("Age:", self.compute_age(parsed))
                break
            print("Invalid format. Try again.")

        mood = input("How are you today? ")
        print(self.mood_reply(mood))

if __name__ == "__main__":
    PersonalAgent().launch()
