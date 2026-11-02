print("Welcome to the Community Waste Management System")
continuechoice = "Yes"
while continuechoice == "Yes":
    print("Enter your community Name")
    communityName = input()
    wasteCategory = ""
    while wasteCategory != "Low" and wasteCategory != "Medium" and wasteCategory != "High":
        print("Enter waste category (Low, Medium, High):")
        wasteCategory = input()
    if wasteCategory == "Low":
        recommendation = "Normal Waste Collection"
    else:
        if wasteCategory == "Medium":
            recommendation = "Scheduled Waste Collection"
        else:
            if wasteCategory == "High":
                recommendation = "Urgent Waste Collection"
    print("Community Name: " + communityName)
    print("Waste Category: " + wasteCategory)
    print("Collection Recommendation: " + recommendation)
    print("Do you want to record another waste report? (Yes/No)")
    continuechoice = input()
print("Thank you for using the Community Waste Management System.")
