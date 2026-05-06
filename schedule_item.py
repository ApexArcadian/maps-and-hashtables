from dataclasses import dataclass


@dataclass
class ScheduleItem:
    """Represents a single course entry in the schedule."""
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str
    
    def get_key(self) -> str:
        """
        Return a unique key for this schedule item.
        Format: Subject_Catalog_Section (e.g., "BIO_141_D01")
        """
        return f"{self.subject}_{self.catalog}_{self.section}"
    
    def print(self) -> None:
        """Print formatted course information (tab-separated columns)."""
        print(f"{self.subject}\t{self.catalog}\t{self.section}\t{self.component}\t"
              f"{self.session}\t{self.units}\t{self.tot_enrl}\t{self.cap_enrl}\t{self.instructor}")
