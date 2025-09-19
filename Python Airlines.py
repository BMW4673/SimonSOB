# =========================
# PSEUDOCODE OVERVIEW
# =========================
# 1. Collect user input (name, miles, segments, dollars, lifetime miles, lounge, ticket price).
# 2. Update totals (add ticket price to annual spend, increment segment count if ticket purchased).
# 3. Determine annual tier by miles.
# 4. Determine annual tier by segments + dollars.
# 5. Assign overall annual tier (whichever is higher).
# 6. Determine lifetime tier by lifetime miles.
# 7. Compare annual vs lifetime to determine effective tier.
# 8. Display summary of miles, spend, and lifetime.
# 9. Display achievements (annual, lifetime).
# 10. If effective tier is not None, display rewards.

# =========================
# CONSTANTS / CONFIG
# =========================

ALL_TIERS = ["None", "Sapphire", "Emerald", "Ruby", "Diamond"]
TIER_RANK = {tier_name: i for i, tier_name in enumerate(ALL_TIERS)}  # None=0 … Diamond=4

BENEFITS = {
    "None":     {"bags": 0, "upgrade": "None",           "lounge": False, "discount": 0.00},
    "Sapphire": {"bags": 0, "upgrade": "Business Class", "lounge": False, "discount": 0.15},
    "Emerald":  {"bags": 1, "upgrade": "Business Class", "lounge": False, "discount": 0.20},
    "Ruby":     {"bags": 2, "upgrade": "First Class",    "lounge": False, "discount": 0.25},
    "Diamond":  {"bags": 3, "upgrade": "First Class",    "lounge": True,  "discount": 0.30},
}

# =========================
# VALIDATION + PROMPTS
# =========================

print("Welcome to Python Airlines Membership System!\n")

def validate_string(value: str) -> str:
    val = value.strip()
    if val == "":
        raise ValueError("Input cannot be blank")
    return val

def ask_str(prompt: str) -> str:
    while True:
        try:
            return validate_string(input(prompt))
        except ValueError as e:
            print("Error:", e, "\n")

def validate_integer(value: str) -> int:
    try:
        return int(value.strip())
    except ValueError:
        raise ValueError(f"Expected integer, got {value!r}")

def ask_int(prompt: str) -> int:
    while True:
        try:
            return validate_integer(input(prompt))
        except ValueError as e:
            print("Error:", e, "Please enter a whole number.\n")

def validate_float(value: str) -> float:
    try:
        return float(value.strip())
    except ValueError:
        raise ValueError(f"Expected number, got {value!r}")

def ask_float(prompt: str) -> float:
    while True:
        try:
            return validate_float(input(prompt))
        except ValueError as e:
            print("Error:", e, "Please enter a numeric dollar amount.\n")

def ask_bool(prompt: str) -> bool:
    while True:
        val = input(prompt + " [Y/N]: ").strip().lower()
        if val in {"y","yes","true","t","1"}: return True
        if val in {"n","no","false","f","0"}: return False
        print("Error: Please answer Y or N.\n")

# =========================
# BUSINESS LOGIC (no globals)
# =========================

def miles_to_tier(annual_miles: int) -> str:
    thresholds = [0, 25_000, 50_000, 75_000, 100_000]
    tier_names = ["None", "Sapphire", "Emerald", "Ruby", "Diamond"]
    current_tier = "None"
    for i in range(len(thresholds)):
        if annual_miles >= thresholds[i]:
            current_tier = tier_names[i]
    return current_tier

def seg_dollar_to_tier(segments: int, dollars: float) -> str:
    if segments >= 120 and dollars > 24_000:
        return "Diamond"
    elif segments > 90 and dollars > 15_000:
        return "Ruby"
    elif segments > 60 and dollars > 7_000:
        return "Emerald"
    elif segments > 30 and dollars > 3_000:
        return "Sapphire"
    else:
        return "None"

def assign_annual_tier(miles_tier_name: str, seg_dol_tier_name: str) -> str:
    if miles_tier_name == "Diamond" or seg_dol_tier_name == "Diamond":
        return "Diamond"
    elif miles_tier_name == "Ruby" or seg_dol_tier_name == "Ruby":
        return "Ruby"
    elif miles_tier_name == "Emerald" or seg_dol_tier_name == "Emerald":
        return "Emerald"
    elif miles_tier_name == "Sapphire" or seg_dol_tier_name == "Sapphire":
        return "Sapphire"
    else:
        return "None"

def assign_lifetime_tier(lifetime_miles: int) -> str:
    if lifetime_miles >= 3_000_000:
        return "Diamond"
    elif lifetime_miles >= 2_000_000:
        return "Ruby"
    elif lifetime_miles >= 1_000_000:
        return "Emerald"
    else:
        return "None"

def pick_effective_tier(annual: str, lifetime: str) -> str:
    return annual if TIER_RANK[annual] >= TIER_RANK[lifetime] else lifetime

# =========================
# PRESENTATION HELPERS
# =========================

def print_summary(fname, seg, miles, annual_dollars, lifetime):
    print(
        f"{fname}, this year you have flown {seg:,} flights for {miles:,} miles "
        f"and spent ${annual_dollars:,.0f} with Python Airlines."
    )
    print(f"Lifetime, you have flown {lifetime:,} miles.\n")

def print_achievements(annual, lifetime):
    if lifetime != "None" and annual != "None":
        print(f"You have achieved lifetime frequent-flier status at the {lifetime} level!")
        print(f"This year, you have also achieved annual frequent-flier status at the {annual} level!\n")
    elif lifetime != "None":
        print(f"You have achieved lifetime frequent-flier status at the {lifetime} level!")
        print("This year, you have not yet achieved an annual frequent-flier status.\n")
    elif annual != "None":
        print(f"This year, you have achieved annual frequent-flier status at the {annual} level!\n")
    else:
        print("You have not yet achieved lifetime or annual frequent-flier status.\n")

def print_rewards(eff_tier: str, ticket_price: float):
    if eff_tier == "None":
        return
    b = BENEFITS[eff_tier]
    discount_pct  = b["discount"]
    discount_amt  = ticket_price * discount_pct
    final_price   = ticket_price - discount_amt

    print(f"As a {eff_tier} member, you have unlocked the following rewards:")
    print(f" - {b['bags']} free checked bags per flight.")
    print(f" - Free seat upgrades to {b['upgrade']}.")
    if b["lounge"]:
        print(" - Enjoy free access to the club lounge in Chicago on your next/upcoming flight!")
    print(
        f" - Your upcoming flight ticket price of ${ticket_price:,.2f} "
        f"was reduced by {int(discount_pct*100)}% (${discount_amt:,.2f}) to ${final_price:,.2f}."
    )

# =========================
# MAIN
# =========================

def main():
    fName           = ask_str("What is your first name? ")
    annualMiles     = ask_int("How many miles have you flown this year? ")
    annualSegments  = ask_int("How many segments have you flown this year? ")
    annualDollars   = ask_float("How much money have you spent this year (USD)? $")
    lifetimeMiles   = ask_int("How many lifetime miles have you flown? ")
    loungeCheck     = ask_bool("Is your next flight to (or through) the Chicago airport?")
    ticketPrice     = ask_float("How much will a Coach Class ticket for your next flight cost? $")

    # Update totals
    annualDollars += ticketPrice
    if ticketPrice >= 0.01:
        annualSegments += 1

    # Tier assignments
    annualMemberMi           = miles_to_tier(annualMiles)
    annualMemberSegandDollar = seg_dollar_to_tier(annualSegments, annualDollars)
    annualTierAssign         = assign_annual_tier(annualMemberMi, annualMemberSegandDollar)
    lifetimeTierAssign       = assign_lifetime_tier(lifetimeMiles)
    effTier                  = pick_effective_tier(annualTierAssign, lifetimeTierAssign)

    # Output
    print_summary(fName, annualSegments, annualMiles, annualDollars, lifetimeMiles)
    print_achievements(annualTierAssign, lifetimeTierAssign)
    if effTier != "None":
        print_rewards(effTier, ticketPrice)
    else:
        print(f"{fName}, you have not yet unlocked rewards. Keep flying with Python Airlines!")

if __name__ == "__main__":
    main()