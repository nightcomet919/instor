import os
import random
from datetime import datetime, timedelta

# Initial Git user name and email
git_user_name = "nightcomet919"
git_user_email = "nightcomet919@outlook.com"


# Input commit period
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Input repo link
repo_link = input("Enter repo link: ")

start_date = datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.strptime(end_date, "%Y-%m-%d")

# Calculate total days
total_days = (end_date - start_date).days + 1

# Set commit frequency (randomized per day)
commit_frequency_min = 1  # minimum commits per day
commit_frequency_max = 6  # maximum commits per day

now = datetime.now()

f = open("commit.txt", "w")
# os.system(f"git config user.name {git_user_name}")
# os.system(f"git config user.email {git_user_email}")
os.system("git init")

pointer = 0
ctr = 1

while total_days > 0:
    # Randomize commit frequency for this day
    daily_commit_frequency = random.randint(commit_frequency_min, commit_frequency_max)
    if  daily_commit_frequency > 4 :
        daily_commit_frequency = 0

    for _ in range(daily_commit_frequency):
        f = open("commit.txt", "a+")
        l_date = start_date + timedelta(days=pointer)
        formatdate = l_date.strftime("%Y-%m-%d")
        hour = random.randint(0, 23)  # random hour
        minute = random.randint(0, 59)  # random minute
        second = random.randint(0, 59)  # random second
        commit_time = f"{hour}:{minute}:{second}"
        f.write(f"commit ke {ctr}: {formatdate} {commit_time}\n")
        f.close()
        os.system("git add .")
        os.system(f"git commit --date=\"{formatdate} {commit_time}\" -m \"commit ke {ctr}\"")
        print(f"commit ke {ctr}: {formatdate} {commit_time}")
        ctr += 1
    
    pointer += 1
    total_days -= 1

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")