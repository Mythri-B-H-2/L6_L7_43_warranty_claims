
def parse_claim(text):
    if not isinstance(text, str):
        raise ValueError("Claim must be a string")

    parts = text.split(':')
    if len(parts) != 2:
        raise ValueError("Claim must contain plan:months")

    plan, months = parts

    if not plan.strip():
        raise ValueError("Warranty plan cannot be empty")

    try:
        months = float(months)
    except ValueError:
        raise ValueError("Months must be a valid number")

    if not months >= 0 or months == float('inf') or months != months:
        raise ValueError("Months must be a finite non-negative number")

    return plan.strip().title(), months


def age_average(ages_csv):
    if not isinstance(ages_csv, str) or not ages_csv.strip():
        raise ValueError("Ages must be a non-empty CSV string")

    try:
        values = [int(r.strip()) for r in ages_csv.split(',')]
    except ValueError:
        raise ValueError("All ages must be valid integers")

    if any(age < 0 for age in values):
        raise ValueError("Ages cannot be negative")

    return sum(values) // len(values)


def payable_charge(text):
    if not isinstance(text, str):
        raise ValueError("Charge must be a string")

    parts = text.split('|')
    if len(parts) != 2:
        raise ValueError("Input must contain charge|discount")

    try:
        charge = float(parts[0])
        discount = float(parts[1])
    except ValueError:
        raise ValueError("Charge and discount must be valid numbers")

    if not (0 <= charge < float('inf') and
            0 <= discount < float('inf')):
        raise ValueError("Charge and discount must be finite non-negative numbers")

    total = charge * 1.18 - discount
    return max(total, 0)


def main():
    print("==== Running parse_claim ====")
    user_input = input("Enter plan:age in months (e.g. standard:30): ")
    try:
        result = parse_claim(user_input)
        print("Plan and Age:", result)
    except ValueError as e:
        print("Invalid claim:", e)

    print("\n==== Running age_average ====")
    user_input = input("Enter product ages as CSV (e.g. 12,24,36): ")
    try:
        result = age_average(user_input)
        print("Average Age:", result)
    except ValueError as e:
        print("Invalid ages:", e)

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 1500|200): ")
    try:
        result = payable_charge(user_input)
        print("Payable Charge:", result)
    except ValueError as e:
        print("Invalid charge:", e)


if __name__ == "__main__":
    main()
