import random
import time
from tqdm import tqdm

# Function to generate random variables
def generate_variables():
    luck = random.randint(1, 100)
    skill = random.randint(1, 100)
    total_levels = random.randint(1, 1000)
    money = random.randint(1, 294739)
    team = random.randint(0, 4)
    security = random.randint(1, 100000)
    risk = random.randint(1, 10000000)

    return luck, skill, total_levels, money, team, security, risk

# Loading screen
def loading_screen():
    print("Loading...")
    for _ in tqdm(range(100), desc="Progress", unit="%", dynamic_ncols=True):
        time.sleep(0.05)

# Timer function
def start_timer():
    start_time = time.time()
    return start_time


# Display stats for 3 seconds
def display_stats(luck, skill, money, team, security, risk):
    print("\nStats Variables:")
    print(f"Luck: {luck}")
    print(f"Skill: {skill}")
    print(f"Money: {money}")
    print(f"Team: {team}")
    print(f"Security: {security}")
    print(f"Risk: {risk}")
    time.sleep(3)

# Convert variables to percentages
def convert_to_percentages(luck, skill, team, security, risk):
    max_values = {'luck': 100, 'skill': 100, 'team': 4, 'security': 100000, 'risk': 10000000}

    luck_percentage = (luck / max_values['luck']) * 100
    skill_percentage = (skill / max_values['skill']) * 100
    team_percentage = (team / max_values['team']) * 100
    security_percentage = (security / max_values['security']) * 100
    risk_percentage = (risk / max_values['risk']) * 100

    return luck_percentage, skill_percentage, team_percentage, security_percentage, risk_percentage

# User options
def user_options():
    print("\nOptions:")
    print("1. Hack")
    print("2. Train")
    print("3. Change IP")
    print("4. Upgrade")

    choice = input("Choose an option (1-4): ")
    return choice

# Train option
def train(skill):
    increase = random.randint(11, 12)
    new_skill = min(skill + increase, 99)
    print(f"Training successful! Skill increased to {new_skill}.")
    return new_skill

# Change IP option
def change_ip(risk):
    decrease = min(500, risk - 1)
    new_risk = max(risk - decrease, 1)
    print(f"IP changed successfully! Risk decreased to {new_risk}.")
    return new_risk

# Upgrade option
def upgrade(security, max_security):
    increase = random.randint(1, 1000)
    new_security = min(security + increase, max_security)
    print(f"Upgrade successful! Security increased to {new_security}.")
    return new_security

# Hack option
def hack(luck_percent, skill_percent, team_percent, security_percent, risk_percent, current_level, total_levels):
    skill_check = random.randint(1, 100)

    max_values_sum = luck_percent + skill_percent + team_percent + security_percent + risk_percent
    current_values_sum = (
        random.uniform(0, 100) + skill_percent + team_percent + security_percent + risk_percent
    )

    success_chance = (current_values_sum / max_values_sum) * 100

    security_check = random.randint(1, 100)
    combined_percentage = security_percent + risk_percent

    if skill_check <= success_chance:
        if combined_percentage < security_check:
            print("Security breach detected! Level reset to 1.")
            return 1, 0  # Reset level to 1 and return 0 as the hack was unsuccessful
        else:
            print("Hack successful! Level increased by 1.")
            return current_level + 1, 1  # Increment level by 1 and return 1 as the hack was successful
    else:
        print("Hack failed! Risk increased by 60, Security decreased by 3.")
        return current_level, 0  # Return 0 as the hack was unsuccessful

# Main function
def main():
    loading_screen()
    print("\nLoading complete!")

    # Generate random variables
    luck, skill, total_levels, money, team, security, risk = generate_variables()

    # Display generated variables for 3 seconds
    display_stats(luck, skill, money, team, security, risk)

    # Insert your lines to print here
    print("Hack everyone as quick as possible without getting caught. Timer starts now.")
    start_time = start_timer()  # Start the timer

    # Convert variables to percentages
    luck_percent, skill_percent, team_percent, security_percent, risk_percent = convert_to_percentages(
        luck, skill, team, security, risk
    )

    # Repeat levels until completed
    current_level = 1
    while current_level <= total_levels:
        print(f"\nLevel {current_level} of {total_levels}")

        # User options
        choice = user_options()

        # Process user choice with a delay of 3 seconds for each action
        if choice == '1':
            current_level, hack_success = hack(
                luck_percent, skill_percent, team_percent, security_percent, risk_percent, current_level, total_levels
            )
            if hack_success:
                print(f"Level {current_level} of {total_levels}")
            else:
                print(f"Current Level: {current_level}")
        elif choice == '2':
            skill = train(skill)
            print(f"Current Level: {current_level}")
        elif choice == '3':
            risk = change_ip(risk)
            print(f"Current Level: {current_level}")
        elif choice == '4':
            security = upgrade(security, 104802)
            print(f"Current Level: {current_level}")

    speed = int(time.time() - start_time)
    print(f"\nCongratulations! You completed all levels!")
    print(f"Total time elapsed: {speed} seconds")

if __name__ == "__main__":
    main()
