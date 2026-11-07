import math

def parse_plan(text):
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    plan, gb = parts[0].strip(), parts[1]
    try:
        gb = float(gb)
    except ValueError:
        return None
    if not plan or not math.isfinite(gb) or gb < 0:
        return None
    return plan.title(), gb

def usage_average(usage_csv):
    if not isinstance(usage_csv, str):
        return None
    try:
        values = [int(r) for r in usage_csv.split(',')]
    except ValueError:
        return None
    if not values or any(v < 0 for v in values):
        return None
    return sum(values) // len(values)

def payable_bill(text):
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        bill, discount = float(parts[0]), float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(bill) and math.isfinite(discount)) or bill < 0 or discount < 0:
        return None
    total = bill * 1.18 - discount
    if not math.isfinite(total):
        return None
    return max(total, 0)

def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter plan:data in GB (e.g. standard:5): ")
    result = parse_plan(user_input)
    print("Plan and Data:", result if result is not None else "Invalid input")

    print("\n==== Running usage_average ====")
    user_input = input("Enter daily usage in MB as CSV (e.g. 300,450,800): ")
    result = usage_average(user_input)
    print("Average Usage:", result if result is not None else "Invalid input")

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 399|50): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result if result is not None else "Invalid input")

if __name__ == "__main__":
    main()
