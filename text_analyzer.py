import re
from collections import Counter


def analyze_text(text):
    characters = len(text)
    sentences = len(re.findall(r"[.!?]+", text))

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    word_count = len(words)

    if word_count == 0:
        print("No valid words found.")
        return

    longest_word = max(words, key=len)
    average_word_length = sum(len(word) for word in words) / word_count

    word_frequency = Counter(words)
    most_common_word, frequency = word_frequency.most_common(1)[0]

    # Simple complexity score
    score = (
        average_word_length * 8
        + (word_count / max(sentences, 1)) * 2
    )

    score = min(100, round(score))

    print("\n" + "=" * 40)
    print("       TEXT ANALYSIS REPORT")
    print("=" * 40)

    print(f"Characters        : {characters}")
    print(f"Words             : {word_count}")
    print(f"Sentences         : {sentences}")
    print(f"Longest Word      : {longest_word}")
    print(f"Average Word Length: {average_word_length:.2f}")
    print(f"Most Common Word  : {most_common_word}")
    print(f"Word Frequency    : {frequency}")

    print("-" * 40)
    print(f"Complexity Score  : {score}/100")

    if score >= 80:
        print("Level             : Very Complex")
    elif score >= 60:
        print("Level             : Complex")
    elif score >= 40:
        print("Level             : Moderate")
    else:
        print("Level             : Simple")

    print("=" * 40)


def main():
    print("TEXT COMPLEXITY ANALYZER")
    print("Enter your text below.")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    text = " ".join(lines)

    analyze_text(text)


if __name__ == "__main__":
    main()
