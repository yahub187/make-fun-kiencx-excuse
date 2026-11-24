import os

LINE = (
    "I missed the deadline because the final 1% is a subtask I delegated "
    "to myself — and I'm still waiting on myself to deliver it."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
