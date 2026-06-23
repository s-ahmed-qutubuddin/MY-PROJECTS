print("AI Powered World Tour Chat-Bot")
print("Please Provide The Details Below so I could give you the best destination")
budget = input("What is Your Budget? (low/medium/high): ").lower()
continent = input("Which continent would you prefer? (oceania/europe/asia/south america/north america): ").lower()
season = input("Select the season? (summer/winter/autumn/spring): ").lower()

while True:

    if budget == "low":              

        if continent == "asia":
            if season in ("summer", "winter"):
                print("Thailand")
                break
            else:
                print("Vietnam")
                break
        elif continent == "europe":
            if season in ("spring", "winter"):
                print("Georgia")
                break
            else:
                print("Hungary")
                break
        elif continent == "north america":
            if season in ("autumn", "summer"):
                print("Nicaragua")
                break
            else:
                print("panama")
                break
        elif continent == "south america":
            if season in ("spring", "winter"):
                print("Colombia")
                break
            else:
                print("Peru")
                break
        elif continent == "oceania":
            print("Fiji")
            break

    elif budget == "medium":
        
        if continent == "asia":
            if season in ("summer", "winter"):
                print("China")
                break
            else:
                print("Malaysia")
                break
        elif continent == "europe":
            if season in ("autumn", "winter"):
                print("France")
                break
            else:
                print("Luxembourg")
                break
        elif continent == "oceania":
            if season in ("summer", "spring"):
                print("Fiji")
                break
            else:
                print("Australia")
                break
        elif continent == "north america":
            if season in ("autumn", "spring"):
                print("Mexico")
                break
            else:
                print("Jamaica")
                break
        elif continent == "south america":
            if season in ("summer", "spring"):
                print("Brazil")
                break
            else:
                print("Uruguay")
                break
    elif budget == "high":
        if continent == "asia":
            if season in ("summer", "spring"):
                print("Japan")
                break
            else:
                print("South Korea")
                break
        elif continent == "oceania":
            if season in ("summer", "spring"):
                print("New Zealand")
                break
            else:
                print("French Polynesia")
                break
        elif continent == "europe":
            if season in ("winter", "spring"):
                print("Switzerland")
                break
            else:
                print("France")
                break
        elif continent == "south america":
            if season in ("winter", "autumn"):
                print("Brazil")
                break
            else:
                print("Venezuela")
                break
        elif continent == "north america":
            print("Canada")
            break
    else:
        print("Invalid budget entered.")
        break