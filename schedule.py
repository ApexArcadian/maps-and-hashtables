from schedule_item import ScheduleItem


class Schedule:
    """Manages a collection of ScheduleItem objects stored in a dictionary."""
    
    def __init__(self):
        """Initialize the schedule with an empty dictionary."""
        self.items = {}
    
    def add_entry(self, item: ScheduleItem) -> None:
        """
        Add a ScheduleItem to the schedule using its unique key.
        
        Args:
            item: A ScheduleItem object to add to the schedule.
        """
        key = item.get_key()
        self.items[key] = item
    
    @staticmethod
    def print_header() -> None:
        """Print the column headers for the schedule."""
        print("Subject\tCatalog\tSection\tComponent\tSession\tUnits\tTotEnrl\tCapEnrl\tInstructor")
    
    def print(self) -> None:
        """Print all schedule items in formatted output."""
        self.print_header()
        for item in self.items.values():
            item.print()
    
    def find_by_subject(self, subject: str) -> list:
        """
        Find all courses matching the given subject.
        
        Args:
            subject: The subject code to search for (e.g., "BIO").
            
        Returns:
            A list of ScheduleItem objects matching the subject.
        """
        return [item for item in self.items.values() if item.subject.upper() == subject.upper()]
    
    def find_by_subject_catalog(self, subject: str, catalog: str) -> list:
        """
        Find all courses matching the given subject and catalog number.
        
        Args:
            subject: The subject code (e.g., "BIO").
            catalog: The catalog number (e.g., "141").
            
        Returns:
            A list of ScheduleItem objects matching both subject and catalog.
        """
        return [item for item in self.items.values() 
                if item.subject.upper() == subject.upper() and item.catalog == catalog]
    
    def find_by_instructor_last_name(self, last_name: str) -> list:
        """
        Find all courses taught by an instructor matching the given last name.
        Uses substring matching on the instructor field.
        
        Args:
            last_name: The instructor's last name to search for (e.g., "Abrahams").
            
        Returns:
            A list of ScheduleItem objects taught by instructors matching the name.
        """
        return [item for item in self.items.values() if last_name.upper() in item.instructor.upper()]
