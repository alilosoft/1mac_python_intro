import datetime


def format_time_hh_mm(time):
    hours = time.days * 24 + time.seconds // 3600
    minutes = (time.seconds // 60) % 60
    time_str = "%.2dh:%.2dm" % (hours, minutes)
    return time_str


start_course_date = datetime.date.today()  # The day you want to start/resume the courses from
deadline = datetime.date(2018, 06, 20)   # The last day to finish courses
days_to_deadline = (deadline - start_course_date).days + 1  # Number of days available to finish the courses
if days_to_deadline < 0:
    print "You have missed the deadline"
    exit()

# Calculating the time remaining to complete the course
# Replace hours and minutes with your values for each course
time_to_study = datetime.timedelta(hours=0, minutes=0)  # Mindset
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Getting Set Up with Python
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Introduction to Serious Programming
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Work Session: Basic Debugging
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Variables & Strings
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Work Session: String Manipulation
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Input -> Function -> Output
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Work Session: Print vs Return
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Control Flow: If Statements & While Loops 4:30
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Deep Debugging
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Work Session: Mad Libs Generator
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Structured Data: Lists & For Loops
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # How to Solve Problems
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Work Session: Mad Libs Continued
# time_to_study += datetime.timedelta(hours=0, minutes=0)  # Getting Started
# time_to_study += datetime.timedelta(hours=1, minutes=50)  # Mini-Project: Take a Break
# time_to_study += datetime.timedelta(hours=2, minutes=0)  # Mini-Project: Secret Message
time_to_study += datetime.timedelta(hours=3, minutes=30)  # Mini-Project: Draw Turtles
time_to_study += datetime.timedelta(hours=1, minutes=0)  # Mini-Project: Send a Text
time_to_study += datetime.timedelta(hours=1, minutes=0)  # Mini-Project: Profanity Editor
time_to_study += datetime.timedelta(hours=4, minutes=0)  # Movie Website Creation
time_to_study += datetime.timedelta(hours=1, minutes=0)  # Advanced Class Making
time_to_study += datetime.timedelta(hours=1, minutes=15)  # What is Version Control?
time_to_study += datetime.timedelta(hours=1, minutes=15)  # Create A Git Repo
time_to_study += datetime.timedelta(hours=2, minutes=0)  # Review a Repo's History
time_to_study += datetime.timedelta(hours=1, minutes=30)  # Add Commits To A Repo
time_to_study += datetime.timedelta(hours=2, minutes=30)  # Tagging, Branching, and Merging
time_to_study += datetime.timedelta(hours=1, minutes=0)  # Undoing Changes
time_to_study += datetime.timedelta(hours=2, minutes=0)  # Working With Remotes
time_to_study += datetime.timedelta(hours=1, minutes=15)  # Working On Another Developer's Repository
time_to_study += datetime.timedelta(hours=2, minutes=0)  # Staying In Sync With A Remote Repository

if time_to_study.total_seconds() == 0 and days_to_deadline > 0:
    mess = "Great! You have D days remaining to deadline, do some practice, revision && relax ;)"
    print mess.replace("D", str(days_to_deadline))
else:
    mess = "You have D days remaining to finish the course before " + str(deadline)
    print mess.replace("D", str(days_to_deadline))
    mess = "And you have T of course/quiz materials to finish!"
    print mess.replace("T", format_time_hh_mm(time_to_study))
    time_by_day = time_to_study / days_to_deadline
    if time_by_day.days == 0:
        mess = "So, you have to study at least T a day to finish in time, do your best!"
        print mess.replace("T", format_time_hh_mm(time_by_day))
    else:
        print "Sorry! No way to do it legally, do more effort next time!"

