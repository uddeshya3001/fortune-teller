# fortune.py - Version v1.1

import random

def main():
    print("🔮 Welcome to Uddeshya Aagre's Fortune Teller (20JE1035) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

    fortunes = {
        "happy": [
            "🌟 Your fortune: Great things await you, Uddeshya! Keep smiling. 🌟",
            "🎉 Your joy is contagious. Let it shine today!"
        ],
        "sad": [
            "💧 Your fortune: Even the darkest night will end, and the sun will rise. 🌅",
            "😢 Hang in there. Brighter days are closer than you think."
        ],
        "neutral": [
            "🌀 Your fortune: Balance is key. Stay steady, and success will follow.",
            "⚖️ Neither high nor low — you're ready to go with the flow."
        ],
        "stressed": [
            "🔥 Your fortune: Pressure makes diamonds. You’ve got this!",
            "💆‍♂️ Take a breath, Uddeshya. Peace is just a pause away."
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("🤔 I can't read your mood. Try happy, sad, neutral, or stressed.")

if __name__ == "__main__":
    main()
