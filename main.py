from schedule import Schedule


def print_results(items: list) -> None:
    """
    Print a list of ScheduleItem objects in formatted output.
    
    Args:
        items: A list of ScheduleItem objects to print.
    """
    if not items:
        print("No courses found.\n")
        return
    
    Schedule.print_header()
    for item in items:
        item.print()
    print()


def main():
    """Main entry point for the Course Schedule System."""
    # Initialize and load schedule
    schedule = Schedule()
    
    try:
        schedule.load_from_csv('STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv')
        print(f"Successfully loaded {len(schedule.items)} courses.\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Main menu loop
    while True:
        print("=" * 70)
        print("COURSE SCHEDULE SYSTEM")
        print("=" * 70)
        print("1. Display all courses")
        print("2. Search by subject")
        print("3. Search by subject and catalog number")
        print("4. Search by instructor last name")
        print("5. Quit")
        print("=" * 70)
        
        choice = input("Enter your choice (1-5): ").strip()
        print()
        
        if choice == '1':
            # Display all courses
            schedule.print()
        
        elif choice == '2':
            # Search by subject
            subject = input("Enter subject code (e.g., BIO): ").strip()
            if subject:
                results = schedule.find_by_subject(subject)
                print(f"\nCourses for subject '{subject}': ({len(results)} found)\n")
                print_results(results)
            else:
                print("Subject code cannot be empty.\n")
        
        elif choice == '3':
            # Search by subject and catalog
            subject = input("Enter subject code (e.g., BIO): ").strip()
            catalog = input("Enter catalog number (e.g., 141): ").strip()
            if subject and catalog:
                results = schedule.find_by_subject_catalog(subject, catalog)
                print(f"\nCourses for {subject} {catalog}: ({len(results)} found)\n")
                print_results(results)
            else:
                print("Subject and catalog number cannot be empty.\n")
        
        elif choice == '4':
            # Search by instructor
            last_name = input("Enter instructor last name (e.g., Abrahams): ").strip()
            if last_name:
                results = schedule.find_by_instructor_last_name(last_name)
                print(f"\nCourses taught by '{last_name}': ({len(results)} found)\n")
                print_results(results)
            else:
                print("Instructor last name cannot be empty.\n")
        
        elif choice == '5':
            # Quit
            print("Thank you for using the Course Schedule System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == '__main__':
    main()
