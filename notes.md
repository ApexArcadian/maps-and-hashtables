# Course Schedule System

## What to Build
Read course data from CSV. Store in a dict. Search and display with a menu.

## Files to Create

1. **schedule_item.py** — Course data object
   - Fields: subject, catalog, section, component, session, units, tot_enrl, cap_enrl, instructor
   - `get_key()` returns Subject_Catalog_Section
   - `print()` displays course info

2. **schedule.py** — Manages all courses
   - `add_entry()` adds a course
   - `print()` shows all courses
   - `find_by_subject()` search by subject
   - `find_by_subject_catalog()` search by subject + number
   - `find_by_instructor_last_name()` search by instructor name
   - `load_from_csv()` reads the CSV file

3. **main.py** — User interface menu
   - Load CSV file
   - Show menu loop
   - Options: display all, search subject, search subject+catalog, search instructor, quit

## Test It
- Run `python main.py`
- Try each menu option
- Verify results make sense
