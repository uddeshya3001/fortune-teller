# fortune.py - Version v1.0

def main():
    print("🔮 Welcome to Uddeshya Aagre's Fortune Teller (20JE1035) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Uddeshya! Keep smiling. ✨")
    elif mood == "sad":
        print("🌧️ Your fortune: Even the darkest night will end, and the sun will rise. 🌞")
    elif mood == "neutral":
        print("🌗 Your fortune: Balance is key. Stay steady, and success will follow. ⚖️")
    else:
        print("🤔 I can't read your mood. Try happy, sad, or neutral.")

if __name__ == "__main__":
    main()
