from textblob import TextBlob; from dataclasses import dataclass
@dataclass 
class Mood: e: str; s: float
def g(t, s): return Mood(":)" if (p := TextBlob(t).sentiment.polarity) >= s else ":(" if p <= -s else ":/", p)
def run_bot(): [print("You:", (t := input("Enter text for analysis: ")), "->", g(t, 0.3)) for _ in iter(int, 1)]
