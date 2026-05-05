# Plan: Course Schedule System with Hashtable-Based Search

## TL;DR
Build a Python-based course scheduling system that reads summer course data from a CSV file, stores it in a dictionary using `Subject_Catalog_Section` keys, and provides search/filtering capabilities via a menu interface. Three modules: `ScheduleItem` (dataclass), `Schedule` (dict-based storage + search methods), and `main.py` (menu-driven CLI).

## Steps

### Phase 1: Data Model Setup
1. **Create `schedule_item.py`** – Define `ScheduleItem` dataclass with fields: Subject, Catalog, Section, Component, Session, Units, TotEnrl, CapEnrl, Instructor
   - Implement `get_key()` method returning `f"{subject}_{catalog}_{section}"`
   - Implement `print()` method for formatted output (tab-separated, matching example format)
   
2. **Create `schedule.py`** – Define `Schedule` class with:
   - `__init__()` – initialize internal dictionary `self.items = {}`
   - `add_entry(item: ScheduleItem)` – add item to dict using `item.get_key()` as key
   - `print_header()` – static/class method printing column headers: "Subject  Catalog  Section  Component  Session  Units  TotEnrl  CapEnrl  Instructor"
   - `print()` – call `print_header()` then iterate dict calling `item.print()` on each value
   - `find_by_subject(subject: str) -> list` – list comprehension filtering items by subject (case-insensitive recommended)
   - `find_by_subject_catalog(subject: str, catalog: str) -> list` – list comprehension filtering by both
   - `find_by_instructor_last_name(last_name: str) -> list` – list comprehension searching instructor field for last_name (substring match simplest approach)

### Phase 2: CSV Loading
3. **Implement CSV reading in `schedule.py`** – Add `load_from_csv(filename: str)` method to Schedule class
   - Open file with `encoding='utf-8-sig'` to handle BOM
   - Use `csv.DictReader` to parse rows
   - For each row, extract the 9 required fields (Subject, Catalog, Section, Component, Session, Units, TotEnrl, CapEnrl, Instructor)
   - Convert Units, TotEnrl, CapEnrl to integers
   - Create `ScheduleItem` object and call `add_entry()`
   - On any error (file not found, malformed row): raise exception (crash with error message per user preference)

### Phase 3: Main Program & Menu
4. **Create `main.py`** – CLI menu-driven interface
   - Instantiate `Schedule` object
   - Call `schedule.load_from_csv('STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv')` (exact filename per user preference)
   - Loop menu until user quits:
     - Print options: (1) Display all, (2) Search by subject, (3) Search by subject+catalog, (4) Search by instructor, (5) Quit
     - Prompt user for choice
     - For options 1-4: call appropriate method, print results (or filtered results)
     - For option 5: exit loop
   - Use `schedule.print()` for option 1, filtered output for others using list comprehension results

### Phase 4: Testing & Verification
5. **Test with sample data**
   - Load CSV and verify all records read correctly (count rows)
   - Test each search function with known data (e.g., search "BIO", search "BIO"+"141", search "Abrahams")
   - Verify output formatting matches example (column alignment, spacing)
   - Test menu loop: start program, run a search, quit
   - Verify no crashes on normal operations

## Relevant Files
- [STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv](STEM%20-%20Summer%202022%20Schedule%20of%20Classes%20as%20of%2005-02-22.csv) — Data source; use exact filename in code; contains 25 columns (9 needed)
- `schedule_item.py` — Define ScheduleItem dataclass with get_key() and print() methods
- `schedule.py` — Define Schedule class with dict storage, load_from_csv(), search/filter methods
- `main.py` — Entry point; instantiate Schedule, load CSV, run menu loop

## Verification
1. **Load CSV** – Run `python main.py`, verify "Display all" prints all courses without errors; confirm row count
2. **Subject search** – Search "BIO" → verify all returned items have Subject="BIO" (e.g., BIO 141, 142, etc.)
3. **Subject+Catalog search** – Search "BIO"+"141" → verify only BIO 141 rows returned (may have multiple sections)
4. **Instructor search** – Search "Abrahams" → verify all Abrahams courses returned; spot-check instructor field contains "Abrahams"
5. **Format verification** – Compare printed output with example format in instructions (tab-separated, proper column alignment)
6. **Menu loop** – Verify menu re-displays after each search; "Quit" cleanly exits

## Decisions
- **CSV filename**: Use exact full filename "STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv" (not renamed)
- **Instructor search**: Implement simplest approach = substring match on entire Instructor field (e.g., search "Abrahams" finds all rows with "Abrahams" anywhere in the field)
- **Error handling**: Crash with exception on CSV errors (file not found, malformed rows) per user preference
- **Menu loop**: Continuous loop until user selects "Quit"
- **Filtering**: All search methods return lists (no printing within search methods); printing happens in main.py
- **Key format**: `Subject_Catalog_Section` (e.g., "BIO_141_D01") as dict key to ensure uniqueness

## Further Considerations
1. **Output formatting** – Ensure alignment: The example shows fixed-width columns. Consider using Python string formatting (ljust/rjust) or f-strings with width specifiers to match exact spacing in instructions.
2. **Case sensitivity** – Recommend case-insensitive searches (convert input and data to lowercase for comparison) for better UX, but simplest approach is case-sensitive. User can specify if needed.
3. **Duplicate handling** – Each unique Subject_Catalog_Section is a distinct key; no duplicates expected in dict, but CSV may have rows with same key (rare edge case).
