"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word to /output/entry.txt: the funniest, truest
description of home Wi-Fi as it is actually lived.
"""

import os

WORD = "Hideandseek"  # 11 chars. The network appears in the list, then
# vanishes the moment you try to connect — it literally plays
# hide-and-seek with you. Instantly understood, no explanation
# needed, and fresher than Slow / Laggy / Flaky.


def main() -> None:
    # Gate guard: the entry must be 1-20 chars, a single word.
    assert 1 <= len(WORD) <= 20, "entry must be 1-20 characters"
    assert WORD.split() == [WORD], "entry must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
