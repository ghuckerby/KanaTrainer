import random

points = 0
streak = 0
higheststreak = 0

hiragana = {
    "あ":"a", "い":"i", "う":"u", "え":"e", "お":"o",
    "か":"ka", "き":"ki", "く":"ku", "け":"ke", "こ":"ko",
    "さ":"sa", "し":"shi", "す":"su", "せ":"se", "そ":"so",
    "た":"ta", "ち":"chi", "つ":"tsu", "て":"te", "と":"to",
    "な":"na", "に":"ni", "ぬ":"nu", "ね":"ne", "の":"no",
    "は":"ha", "ひ":"hi", "ふ":"fu", "へ":"he", "ほ":"ho",
    "ま":"ma", "み":"mi", "む":"mu", "め":"me", "も":"mo",
    "や":"ya", "ゆ":"yu", "よ":"yo",
    "ら":"ra", "り":"ri", "る":"ru", "れ":"re", "ろ":"ro",
    "わ":"wa", "を":"wo",
    "ん":"n",
}
katakana = {
    "ア":"a", "イ":"i", "ウ":"u", "エ":"e", "オ":"o",
    "カ":"ka", "キ":"ki", "ク":"ku", "ケ":"ke", "コ":"ko",
    "サ":"sa", "シ":"shi", "ス":"su", "セ":"se", "ソ":"so",
    "タ":"ta", "チ":"chi", "ツ":"tsu", "テ":"te", "ト":"to",
    "ナ":"na", "ニ":"ni", "ヌ":"nu", "ネ":"ne", "ノ":"no",
    "ハ":"ha", "ヒ":"hi", "フ":"fu", "ヘ":"he", "ホ":"ho",
    "マ":"ma", "ミ":"mi", "ム":"mu", "メ":"me", "モ":"mo",
    "ヤ":"ya", "ユ":"yu", "ヨ":"yo",
    "ラ":"ra", "リ":"ri", "ル":"ru", "レ":"re", "ロ":"ro",
    "ワ":"wa", "ヲ":"wo",
    "ン":"n",
}

selection = "K"

while (selection.upper() != "N"):

    selection = input("Katakana (K), Hiragana(H) or Stop(N)?")

    if selection.upper() == "K":

        kana, romaji = random.choice(list(katakana.items()))
        answer = input("What's the romaji for: ", kana)
        if (answer.lower() == romaji):
            print("Correct!")
            points += 1
            streak += 1
            if streak > higheststreak:
                higheststreak = streak
            print("Points: ", points, "Streak: ", streak, "Highest streak: ", higheststreak)
        else:
            print("Incorrect, no points!")
            print("Your streak has been reset!")

    elif selection.upper() == "H":

        kana, romaji = random.choice(list(hiragana.items()))
        answer = input("What's the romaji for: ", kana)
        if (answer.lower() == romaji):
            print("Correct!")
            points += 1
            streak += 1
            if streak > higheststreak:
                higheststreak = streak
            print("Points: ", points, "Streak: ", streak, "Highest streak: ", higheststreak)
        else:
            print("Incorrect, no points!")
            print("Your streak has been reset!")

print("You got: ", points, "points!")
print("Your highest streak was: ", higheststreak, "!")