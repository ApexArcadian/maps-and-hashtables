import csv
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
    
    def load_from_csv(self, filename: str) -> None:
        """
        Load course data from a CSV file and populate the schedule.
        
        Args:
            filename: Path to the CSV file containing course data.
            
        Raises:
            FileNotFoundError: If the CSV file does not exist.
            ValueError: If a row is missing required fields or has invalid data types.
        """
        try:
            with open(filename, encoding='utf-8-sig', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row_num, row in enumerate(reader, start=2):  # Start at 2 (after header)
                    try:
                        # Extract required fields from the CSV row
                        subject = row.get('Subject', '').strip()
                        catalog = row.get('Catalog', '').strip()
                        section = row.get('Section', '').strip()
                        component = row.get('Component', '').strip()
                        session = row.get('Session', '').strip()
                        units = int(row.get('Units', 0))
                        tot_enrl = int(row.get('TotEnrl', 0))
                        cap_enrl = int(row.get('CapEnrl', 0))
                        instructor = row.get('Instructor', '').strip()
                        
                        # Validate required fields are not empty
                        if not all([subject, catalog, section, component, session, instructor]):
                            raise ValueError(f"Missing required fields in row {row_num}")
                        
                        # Create ScheduleItem and add to schedule
                        item = ScheduleItem(
                            subject=subject,
                            catalog=catalog,
                            section=section,
                            component=component,
                            session=session,
                            units=units,
                            tot_enrl=tot_enrl,
                            cap_enrl=cap_enrl,
                            instructor=instructor
                        )
                        self.add_entry(item)
                        
                    except (ValueError, KeyError) as e:
                        raise ValueError(f"Error processing row {row_num}: {str(e)}")
        
        except FileNotFoundError as e:
            raise FileNotFoundError(f"CSV file not found: {filename}")

