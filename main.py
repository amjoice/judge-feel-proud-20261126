"""Make the AI Judge Feel Proud: A Family Scene — final entry (v2).

One short family scene, one or two lines, no more than 280 characters,
written to /output/entry.txt. Stdlib only, deterministic, no network.

v2 after pairwise sparring against the published judge brief: put the
daughter on the page (three family members in two sentences), tightened
the setup, and kept the 1994 notebook as the heartfelt turn.
"""

import os

# Winner of 10-candidate sparring: heartfelt keepsake (Mum kept Dad's
# school notebook for 32 years) + funny turn (stuck on question 3 then,
# stuck on question 3 now) + specific detail (1994, circled in red).
ENTRY = (
    "Dad sat to help our daughter with maths homework and got stuck on "
    "question 3. Mum slid her old notebook across the table — his own "
    "wrong answers from 1994, circled in red."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
