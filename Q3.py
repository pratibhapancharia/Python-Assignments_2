'''3. Build a small command-line app to track quiz scores,stored in a CSV file.'''
import csv
import sys

def load_scores(path: str) -> list[tuple[str, int]]:
    """
    Load and parse scores from a CSV file.
    """
    records: list[tuple[str, int]] = []
    try:
        with open(path, newline='', encoding='utf-8') as f:
            for lineno, row in enumerate(csv.reader(f), 1):
                if len(row) != 2:
                    print(f" Skipping line {lineno}: {row}")
                    continue
                name, score_str = row
                try:
                    score = int(score_str)
                except ValueError:
                    print(f"⚠️ Invalid score on line {lineno}: {score_str}")
                    continue
                records.append((name, score))
    except FileNotFoundError:
        pass  # starting fresh
    return records

def add_score(records: list[tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))

def save_scores(path: str, records: list[tuple[str, int]]) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(records)

def top_n(records: list[tuple[str, int]], n: int) -> list[tuple[str, int]]:
    return sorted(records, key=lambda r: r[1], reverse=True)[:n]

def main() -> None:
    SCORE_FILE = "scores.csv"
    records = load_scores(SCORE_FILE)

    while True:
        print("\n1) Show Top N\n2) Add Score\n3) Exit")
        choice = input("Choice [1-3]: ").strip()
        if choice == '1':
            try:
                n = int(input("Enter N: "))
                assert n > 0
            except (ValueError, AssertionError):
                print("❗Enter a positive integer.")
                continue
            top = top_n(records, n)
            print("🏆 Top Scores:", *[f"{name}:{score}" for name, score in top], sep="\n")
        elif choice == '2':
            name = input("Name: ").strip()
            if not name:
                print("❗Name can't be blank.")
                continue
            try:
                score = int(input("Score (int): "))
            except ValueError:
                print("❗Score must be an integer.")
                continue
            add_score(records, name, score)
            save_scores(SCORE_FILE, records)
            print(f"✅ Added {name}:{score}")
        elif choice == '3':
            print("👋 Goodbye!")
            sys.exit(0)
        else:
            print("❗Invalid choice, please pick 1–3.")

if __name__ == "__main__":
    main()
