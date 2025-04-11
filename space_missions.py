# Space Missions

# Dataset of space missions
space_missions = [
    {"name": "Apollo 11", "agency": "NASA", "year": 1969, "destination": "Moon"},
    {"name": "Vostok 1", "agency": "Soviet Union", "year": 1961, "destination": "Low Earth Orbit"},
    {"name": "Mars Pathfinder", "agency": "NASA", "year": 1997, "destination": "Mars"},
    {"name": "Chang'e 4", "agency": "CNSA", "year": 2019, "destination": "Moon"},
    {"name": "Voyager 1", "agency": "NASA", "year": 1977, "destination": "Interstellar space"},
    {"name": "Shenzhou 5", "agency": "CNSA", "year": 2003, "destination": "Low Earth Orbit"},
]

# Display all missions
def list_missions():
    print("List of Space Missions:")
    for mission in space_missions:
        print(f"- {mission['name']} ({mission['year']}) by {mission['agency']} to {mission['destination']}")

# Filter missions by agency
def filter_by_agency(agency_name):
    print(f"\nMissions by {agency_name}:")
    for mission in space_missions:
        if mission["agency"].lower() == agency_name.lower():
            print(f"- {mission['name']} ({mission['year']}) to {mission['destination']}")

# Main function
def main():
    list_missions()
    print("\n")
    agency = input("Enter a space agency to filter missions (e.g., NASA, CNSA): ")
    filter_by_agency(agency)

if __name__ == "__main__":
    main()
