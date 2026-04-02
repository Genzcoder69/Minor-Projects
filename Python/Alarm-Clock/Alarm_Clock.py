import datetime
import time
import winsound

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S"), now.strftime("%I:%M %p")

def play_alarm():
    print("\n" + "=" * 40)
    print("   ALARM RINGING! WAKE UP!")
    print("=" * 40)
    for i in range(10):
        winsound.Beep(1000, 500)
        winsound.Beep(800, 300)
        time.sleep(0.2)
    print("\nAlarm stopped. Have a great day!")

def validate_time_input(time_str):
    for fmt in ("%H:%M:%S", "%H:%M"):
        try:
            return datetime.datetime.strptime(time_str, fmt).time()
        except ValueError:
            continue
    return None

def run_alarm_clock():
    print("=" * 40)
    print("        PYTHON ALARM CLOCK")
    print("=" * 40)

    # Show current system time
    current_24, current_12 = get_current_time()
    print(f"\nCurrent System Time : {current_24}  ({current_12})")

    # Take alarm input
    print("\nSet Your Alarm")
    print("Format: HH:MM  or  HH:MM:SS  (24-hour)")
    print("Example: 07:30  or  14:45:00")

    while True:
        alarm_input = input("\n -> Enter Alarm time: ").strip()
        alarm_time = validate_time_input(alarm_input)
        if alarm_time is None:
            print("Invalid format! Please use HH:MM or HH:MM:SS")
            continue
        now_time = datetime.datetime.now().time()
        if alarm_time <= now_time:
            print("That time has already passed. Please enter a future time.")
            continue
        break

    alarm_display = alarm_time.strftime("%H:%M:%S")
    alarm_12hr = datetime.datetime.strptime(alarm_display, "%H:%M:%S").strftime("%I:%M:%S %p")

    print(f"\nAlarm set for : {alarm_display}  ({alarm_12hr})")
    print("Waiting for alarm... (Press Ctrl+C to cancel)\n")

    try:
        while True:
            now = datetime.datetime.now()
            now_time_str = now.strftime("%H:%M:%S")
            alarm_time_str = alarm_time.strftime("%H:%M:%S")

            # FIX: Cast to int explicitly to avoid float formatting error
            alarm_dt = datetime.datetime.combine(datetime.date.today(), alarm_time)
            remaining_seconds = int((alarm_dt - now).total_seconds())

            hours_left = remaining_seconds // 3600
            mins_left  = (remaining_seconds % 3600) // 60
            secs_left  = remaining_seconds % 60

            print(
                f"\r Current Time: {now_time_str}  |  "
                f"Time Left: {hours_left:02d}:{mins_left:02d}:{secs_left:02d}   ",
                end="",
                flush=True
            )
            # Trigger alarm
            if now_time_str == alarm_time_str:
                play_alarm()
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled by user.")

if __name__ == "__main__":
    run_alarm_clock()
