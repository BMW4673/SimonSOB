##Read.Me
#MEMBERSHIP BASIS
    #Miles (annual miles flown and lifetime miles flown)
    #Segments (annual segments flown)
    #Dollars (annual dollars spent).
#ANNUAL MEMBERSHIP TIERS
    #None (<25k mi or <30seg and $3k)
    #Sapphire (25K mi or 30seg and $3K)
    #Emerald (50k mi or 60seg and $7k)
    #Ruby (75k mi or 90seg and $15k)
    #Diamond (>=100k mi or >=120seg and $24K)
#LIFETIME MEMBERSHIP TIERS
    #None (<3M mi)
    #Emerald (>=1M mi)
    #Ruby (2M mi)
    #Diamond (3M mi)
#BENEFITS
    #Sapphire (Bags = 0, Upgrades = Business, Lounge = No, Discount = 15%)
    #Emerald (Bags = 1, Upgrades = Business, Lounge = No, Discount = 20%)
    #Ruby (Bags = 2, Upgrads = First Class, Lounge = No, Discount = 25%)
    #Diamond (Bags = 3, Upgrades = First Class, Lounge = Yes, Discount = 30%)
    
#User Input Variables
    #FirstName: "What is your first name"
    #AnnualMiles: "How many miles have you flown this year?"
    #AnnualSegments: "How many segments have you flown this year?"
    #AnnualDollars: "How much money have you spen this year (USD)?"
    #LifetimeMiles: "How many lifetime miles have you flown?"
    #LoungeCheck: "Is your next flight to (or through) the Chicago airport?"
    #TicketPrice: "How much will a Coach Class ticket for your next flight cost (USD)?"

#Calculated Variables
    #annualMemberMi
    #annualMemberSegandDollar
    #annualTierAssign
    #liftimeTierAssign

#Dictionary Benefits
TIERS = ["None", "Sapphire", "Emerald", "Ruby", "Diamond"]
TIER_RANK = {t : i for i, t in enumerate(TIERS)} #None = 0 ... Diamond = 4

BENEFITS = {
    "None":     {"bags": 0, "upgrades": "None",           "lounge": False, "discounts": 0.00},
    "Sapphire": {"bags": 0, "upgrades": "Business Class", "lounge": False, "discounts": 0.15},
    "Emerald":  {"bags": 1, "upgrades": "Business Class", "lounge": False, "discounts": 0.20}
    "Ruby":     {"bags": 2, "upgrades": "First Class",    "lounge": False, "discounts": 0.25},
    "Diamond":  {"bags": 3, "upgrades": "First Class",    "lounge": True,  "discounts": 0.30},
}

#Data Validation
def validate_string(value: str) -> str:
    """Ensure the input is a non-empty string, then validate type."""
    val = value.strip()
    if val == "":
        raise ValueError("String cannot be empty")
    return val

def ask_str(prompt: str) -> str:
    while True:
        try:
            return validate_string(input(prompt))
        except ValueError as e:
            print ("Error", e, "Please try again.\n")

def validate_integer(value: str) -> int:
    """Ensure the input can be parsed as an integer, then validate type."""
    val = value.strip()
    try:
        return int(val)
    except ValueError:
        raise ValueError(f"Expected integer, got {value!r}")

def ask_int(prompt: str) -> int:
    while True:
        try:
            return validate_integer(input(prompt))
        except ValueError as e:
            print ("Error", e, "Please enter an whole number (integer).\n")

def validate_float(value: str) -> float:
    """Ensure the input can be parsed as a float, then validate type."""
    val = value.strip()
    try:
        return float(val)
    except ValueError:
        raise ValueError(f"Expected float, got {value!r}")
    
def ask_float(prompt: str) -> float:
    while True:
        try:
            return validate_float(input(prompt))
        except ValueError as e:
            print ("Error", e, "Please enter a dollar value. \n")

def validate_boolean(value: str) -> bool:
    """Ensure the input can be parsed as a boolean (Y/N), then validate type."""
    val = value.strip().lower()
    if val in {"y", "yes", "true", "t", "1"}:
        return True
    if val in {"n", "no", "false", "f", "0"}:
        return False
    raise ValueError(f"Expected Y/N, got {value!r}")

def ask_bool(prompt: str) -> bool:
    while True:
        try:
            return validate_boolean(input(prompt))
        except ValueError as e:
            print ("Error", e, "Please respond with Y or N.\n")

#Data Entry
fName = ask_str("What is your first name? ")
annualMiles = ask_int("How many miles have you flown this year? ")
annualSegments = ask_int("How many segments have you flown this year? ")
annualDollars = ask_float("How much money have you spent this year (USD)? $")
lifetimeMiles = ask_int("How many lifetime miles have you flown? ")
loungeCheck = ask_bool("Is your next flight to (or through) the Chicago airport? (yes/no)")
ticketPrice = ask_float("How much will a Coach Class ticket for your next flight cost? $")

#Annual Tier Logic
#Calculations
annualDollars = ticketPrice+annualDollars
if ticketPrice >=0.01:
    annualSegments = annualSegments+1
def best_tier(annual: str, lifetime: str) -> str:
    """Pick the higher of annual vs lifetime by rank."""
    return annual if TIER_RANK[annual] >= TIER_RANK[lifetime] else lifetime

#Annual Membership Tier by Miles
if annualMiles >= 100000:
    annualMemberMi = "Diamond"
elif annualMiles > 75000:
    annualMemberMi = "Ruby"
elif annualMiles > 50000:
    annualMemberMi = "Emerald"
elif annualMiles > 25000:
    annualMemberMi = "Sapphire"
else:
    annualMemberMi = "None"
    
#Annual Membership Tier by Segment and Dollars
if annualSegments >= 120 and annualDollars > 24000:
    annualMemberSegandDollar = "Diamond"
elif annualSegments > 90 and annualDollars > 15000:
    annualMemberSegandDollar = "Ruby"
elif annualSegments > 60 and annualDollars > 7000:
    annualMemberSegandDollar = "Emerald"
elif annualSegments > 30 and annualDollars > 3000:
    annualMemberSegandDollar = "Sapphire"
else:
    annualMemberSegandDollar = "None"

#Annual Tier Assignment
if annualMemberMi == "Diamond" and annualMemberSegandDollar == "Diamond":
    annualTierAssign = "Diamond"
elif annualMemberMi == "Ruby" and annualMemberSegandDollar == "Ruby":
    annualTierAssign = "Ruby"
elif annualMemberMi == "Emerald" and annualMemberSegandDollar == "Emerald":
    annualTierAssign = "Emerald"
elif annualMemberMi == "Sapphire" and annualMemberSegandDollar == "Sapphire":
    annualTierAssign = "Sapphire"
else:
    annualTierAssign = "None"

#Lifetime Tier Logic
if lifetimeMiles >= 3000000:
    lifetimeTierAssign = "Diamond"
elif lifetimeMiles >= 2000000:
    lifetimeTierAssign = "Ruby"
elif lifetimeMiles >= 1000000:
    lifetimeTierAssign = "Emerald"
else:
    lifetimeTierAssign = "None"

#Tier Logic Calculation
effectiveTier = best_tier(annualTierAssign, lifetimeTierAssign)
benefit = BENEFITS[effectiveTier]

#Apply discount to ticket price
discountPct = benefit["discount"]
discountAmt = ticketPrice * discountPct
finalPrice = ticketPrice - discountPct

#Display Results to User
#Display to Input Summary
print(
    f"{fName}, this year you have flown "
    f"{annualSegments:,} flights for "
    f"{annualMiles:,} miles and spent "
    f"${annualDollars:,.0f} with Python Airlines. "
    f"Lifetime, you have flown {lifetimeMiles:,} miles."
)

#Display Lifetime Tier if Assigned - This needs to be corrected
if lifetimeTierAssign != "None":
    print(f"You have acheived lifetime frequent-flier status at the {lifetimeTierAssign} level!")
    
#Display Annual Tier if Assigned
if annualTierAssign != "None"
    print(f"This year, you have achieved annual frequent-flier stauts at the {annualTierAssign} level!")
else:
    print(f"This year, you have achieved annual frequent-flier status at the {annualTierAssign} level!")
if annualTierAssign == "None":
    print(f"You are on your way to achieveing annual frequent-flier status with Python Airlines!")
print ()

#Rewards Summary
print("You have unlocked the following rewards: ")
print(f" - {benefit['bags']} free checked bags per flight.")
print(f" - Free seat upgrades to {benefit['upgrade']}.")
print(f" - Free access to the club loung next time flying to/through in Chicago.")
if benefit["lounge"]:
    print(f" - Enjoy free access to the club loung in Chicago on your next/upcoming flight!")
print(f" - Your upcoming flight ticket price of ${ticketPrice:,.2f} "was reduced by {int(discountPct to [finalPrice:,.2f}).")
  ##This is where I stopped, Slide 15.   
#End of program