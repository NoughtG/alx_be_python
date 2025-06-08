from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Display current date and time
    current_date = display_current_datetime()
    
    # Prompt user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        if days < 0:
            print("Please enter a non-negative number of days.")
            return
        # Calculate and display future date
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
