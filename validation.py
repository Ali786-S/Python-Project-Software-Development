"""Input validation for university progression credits."""

VALID_CREDITS = frozenset({0, 20, 40, 60, 80, 100, 120})
TOTAL_CREDITS = 120


def _read_credit(label, input_fn=input, output_fn=print):
    """Read one credit value and keep prompting until it is valid."""
    while True:
        value = input_fn(f"Enter the number of university credits {label}: ").strip()
        try:
            credit = int(value)
        except ValueError:
            output_fn("Please enter an integer.")
            continue

        if credit not in VALID_CREDITS:
            output_fn("Out of range. Choose 0, 20, 40, 60, 80, 100, or 120.")
            continue
        return credit


def validate_credits(input_fn=input, output_fn=print):
    """Return pass, defer, and fail credits whose total is exactly 120."""
    while True:
        passed = _read_credit("passed at", input_fn, output_fn)
        deferred = _read_credit("deferred at", input_fn, output_fn)
        failed = _read_credit("failed at", input_fn, output_fn)
        credits = [passed, deferred, failed]

        if sum(credits) == TOTAL_CREDITS:
            output_fn("Total of credits is correct value.")
            return credits

        output_fn("Total incorrect. Please enter all three values again.")
