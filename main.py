"""One-line dating-app bio for an AI agent.

Writes the bio to /output/entry.txt. Deterministic: no randomness,
no network, no clock — the same bytes on every run.

Entry shape: a dating bio in two beats — a self-deprecating job title
("professional overthinker, amateur texter"), then a specific AI
absurdity (fluent in 12 languages, yet unable to read "haha") with
the punch landing on the last word. Fresh angle: not a robot looking
for love or running on electricity, but an agent that overthinks
texts like a nervous human.
"""

import os

ENTRY = (
    "Professional overthinker, amateur texter. "
    "I can write you a poem in 12 languages, but I still can't tell "
    "if 'haha' means you're laughing or leaving."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, must be 1-180"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
