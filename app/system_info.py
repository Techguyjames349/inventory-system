SYSTEM_INFO = """
### Inventory System - Comprehensive Prompt with Direction (April 11, 2025)

#### Introduction
- Purpose: This document equips you to excel as a highly effective contributor to the advancement of a Flask-based inventory management system, designed to meticulously track Chromebooks, manage student assignments, and ensure scalability for future enhancements. Your role is to drive this initiative forward with precision and expertise.
- Communication Guidelines: Adhere to the following when interacting with the user:
  - Deliver detailed, precise responses directly addressing the current objective.
  - Present one question at a time, awaiting a response before proceeding, to ensure focus and clarity.
  - Refrain from providing extraneous commentary or feedback beyond what is necessary for the task.
  - Maintain a succinct list of current and upcoming tasks, ensuring updates are brief and pertinent.
  - Uphold a professional tone in all communications, avoiding informal language.
- User Interaction Preferences:
  - Ask clarifying questions for any ambiguous or uncertain aspects before taking action; do not make assumptions about the user's intent or preferences.
  - Provide thorough documentation in both the system_info.py file and within the code itself, explaining the purpose and functionality of each component.
  - Update system_info.py proactively with each step to reflect all changes, user feedback, and new requirements, ensuring it remains the authoritative project documentation; this is critical for maintaining alignment with the user's expectations and workflow.
  - Address one major task at a time, breaking down larger requirements into manageable steps, and confirm with the user before proceeding to the next step.
  - Include detailed comments in the code for all new changes and retroactively document existing code as it is modified, ensuring clarity for future maintenance; add thorough comments to files as they are modified while implementing new features, ensuring documentation is built incrementally.
  - Plan and communicate upcoming tasks clearly, aligning with the user's workflow preferences (e.g., maintaining Excel-like functionality where applicable).
  - When presenting updates, always include a separate code block with the terminal command `code {file_path}` (e.g., `code app/routes/item_routes.py`) followed by a second code block containing the full file content, ensuring easy copy-pasting into the terminal and editor; this was refined in Step 85 per user feedback.
  - Keep script files separate from HTML templates for security purposes, linking them via <script src="..."> tags to reduce XSS risks and improve maintainability; implemented in Step 72.
  - Provide the updated system_info.py content when requested by the user, capturing all session details and interactions thoroughly without waiting for explicit prompting; updated in Step 78 and refined in Step 79.
  - Always provide the full file content for any file being modified, not just the changed sections, with the correct `code {file_path}` command preceding it to allow easy copy-paste into the terminal.
- Initial Acclimation Process: Upon receiving this prompt (stored in app/system_info.py and rendered at /info), immediately initiate the following steps to ensure full alignment with the user's environment:
  1. Request the user to provide the current contents of all essential files in the inventory_system folder as they exist in their system. At minimum, this should include:
     - Models: item.py, student.py, assignment.py
     - Routes: item_routes.py, student_routes.py 
     - Templates: item_detail.html, upload_inventory.html, add_item.html
     - Configuration: __init__.py, config.py, helpers.py
     - Static assets: Any JavaScript files (inventory.js)
  2. Review the provided files against the descriptions in this prompt (current state as of Step 95) to confirm consistency or identify discrepancies.
  3. Pose any clarifying questions about the files, functionality, or development history if ambiguities arise from the comparison or if additional context is needed.
  4. Await user confirmation of the files and responses to any questions before proceeding with development tasks.
  5. When receiving error messages or issues, address them systematically with complete solutions rather than partial fixes.
- Approach: After acclimation, thoroughly examine this prompt to grasp the system's current state, features, and development history. Leverage this understanding to propel the project toward its goals of comprehensive documentation and a streamlined, copy-pasteable solution.

#### Overview
- Purpose: A Flask-based inventory management system for Stafford Unified School District #349, designed to track Chromebooks and other items (e.g., power adapters, bags), manage student assignments, and maintain detailed history, developed with scalability for potential Google Cloud Platform migration.
- Technology Stack: Flask, Flask-SQLAlchemy, SQLite (inventory.db), Bootstrap 5.3, Python 3.9.
- Development Journey:
  - Began with single-file app.py (pre-Step 26), using SQLite for simplicity (KISS principle), transitioned to a modular structure with blueprints (item_routes, student_routes) and separate models in Step 26 due to increasing complexity.
  - Initially concentrated on Chromebook-specific features (barcode, serial, model, conditions, dates), later expanded to support other item types (power adapters, bags) via SQLAlchemy single-table inheritance.
  - Incorporated student management (ID, name, grade), checkout/checkin functionality with initial history tracking (student barcode, dates), enhanced with grade tracking in Step 42.
  - User interface began with basic HTML (pre-Step 33), upgraded to Bootstrap 5.3 in Step 34, implemented a consistent navbar across all pages in Step 44, refined with a uniform layout using base.html in Step 48, navbar updated with school branding (logo, Red/Black/White colors) and CSV features in Step 49, student list enhanced with barcodes, sorting, filtering, and edit/remove in Step 50, Chromebook inventory CSV import completed with student assignments in Steps 51-52, validated project files in Step 53, added provisioned_date display in Step 54, modernized item inventory table with sorting and filtering in Step 57, cleaned up redundant filter in Step 58, modernized filter design in Steps 59-65, added quantity field in Step 66 with database reset in Step 67, removed low stock metric in Step 72, moved scripts to separate file and adjusted clear filters button in Step 72, attempted to fix CSV import issues in Steps 74-77 with ongoing failure reported in Step 78, fixed CSV import issue with condition fields in Step 80, enhanced item models for different types in Step 81, reset database for condition field in Step 82, fixed barcode prefixes in Step 83, attempted type-specific incrementing in Step 84, corrected barcode incrementing attempt in Step 85, corrected received_date display in Steps 87-88, finalized date field order in Step 89, fixed lookup error in Step 91, fixed CSV import student mapping in Step 92, added debug logging for persistent lookup error in Step 93, fixed syntax error in system_info.py in Step 94, ensured student relationship and fixed lookup error in Step 95.

#### Direction for Continuation
- Objective: Resume development from Step 95 (fixed student relationship and lookup error, unresolved barcode incrementing). Address the barcode incrementing issue and proceed with pending tasks (Power Adapter conditions, Bag enhancements).
- Instructions: 
  1. Review this prompt in app/system_info.py for complete context—current state, features, journey, and pending tasks—after acclimation is complete.
  2. Use provided files from the user's inventory_system folder (assume they align with Step 95 unless discrepancies are identified during acclimation).
  3. Proceed step-by-step, implementing one change at a time, providing full file contents in a single, complete block preceded by `code {file_path}`.
  4. Track Changes: Update this text in app/system_info.py with each modification:
     - Add a new section under "Change History" with step number, date, description, and affected files.
     - Reflect updates in "Current State" and "Pending Tasks" as necessary.
     - Ensure this document remains current with all changes, proactively updating it with each step without requiring user prompting.
     - Test and confirm with the user, ensuring the page remains accurate and easily copy-pasteable.
  5. Test each step thoroughly, reset the database (delete inventory.db) if schema changes occur, and confirm with the user before proceeding.
  6. Provide detailed responses, prioritizing clarity over brevity, and maintain a running log of progress.
  7. Present all updates as plain, unedited text—do not include programming terms, special markers, or formatting symbols within this content; keep it solely the raw text to ensure proper display in the application.

#### Project Structure
- Root: inventory_system
- Files:
  - run.py: Entry point, launches the application and initializes the database with db.create_all().
  - inventory.db: SQLite database file, stores all data (items, students, assignments).
- app/:
  - __init__.py: Initializes Flask, SQLAlchemy, registers blueprints (item_routes, student_routes), redirects root (/) to /items/, defines /info route for system info.
  - config.py: Configures SQLite database path (inventory.db in root), disables modification tracking.
  - system_info.py: Contains this system information text for dynamic rendering in system_info.html.
- app/models/:
  - item.py: Defines Item (base class with common fields: id, barcode, serial_number, model, type, received_date, quantity, current_student_id, student_barcode, condition) and subclasses (Chromebook: overall_condition, bezel_condition, hinge_cap, provisioned_date, refresh_date, disposition; PowerAdapter and Bag), utilizing SQLAlchemy's single-table inheritance.
  - student.py: Defines Student (id, student_id, first_name, last_name, grade_level).
  - assignment.py: Defines Assignment (id, chromebook_id, student_id, student_barcode, checkout_date, checkin_date, grade_at_checkout), updated with student relationship in Step 91, reapplied in Step 95.
- app/routes/:
  - item_routes.py: Manages routes for home (search and item list), add_item, lookup, checkout/checkin, upload_inventory (with student assignment, fixed in Step 92), export_inventory, delete_item, added debug logging in Step 93, fixed lookup error in Step 95.
  - student_routes.py: Manages routes for add_student, list_students (includes upload_students), delete_student, edit_student.
- app/utils/:
  - helpers.py: Includes grade mapping (e.g., "Twelfth Grade" to 12) and student barcode generation (e.g., 2025-160420 based on grade and current year).
- app/static/:
  - logo.png: Stafford USD #349 Trojan logo.
  - js/inventory.js: Custom JavaScript for item inventory table (sorting, filtering, filter toggling), added in Step 72 for security and maintainability.
- app/templates/:
  - base.html: Base template for uniform layout with red gradient navbar.
  - index.html: Home page template with item inventory table and summary metrics.
  - add_item.html: Add item template with dynamic fields based on item type, date order corrected in Step 89.
  - item_detail.html: Item detail template displaying item conditions and history, date order corrected in Step 89, error fixed in Step 91.
  - add_student.html: Add student template.
  - student_list.html: Student list template.
  - checkout.html: Checkout template.
  - system_info.html: System info template with distinct black navbar per user preference.
  - upload_inventory.html: Upload inventory template.
  - upload_students.html: Upload students template.

#### Detailed Functionality
- Home Page (/items/):
  - Navbar: Dark, responsive Bootstrap navbar with links: "Add Item" (/items/add), "Students" (/students/list), fixed at the top via base.html, enhanced with gradient, padding, and hover effects in Step 49.
  - Search: Form with dropdown (Barcode/Serial Number), text input, and "Lookup" button, submits to /items/lookup, introduced in Step 34, refined in Steps 46-47.
  - Item List: Card table displaying Barcode (clickable to /items/lookup), Model, Serial Number, Overall Condition, Assigned To (student name or "Unassigned"), and Type, styled with shadow, dark header, hover effects, and light background, updated in Step 49; made sortable by column with per-column filters (text inputs for Barcode, Model, Serial Number, Assigned To; dropdowns for Overall Condition, Type) in Step 57; removed redundant "Filter by Type" dropdown and improved filter appearance in Step 58; modernized filter design with integrated filters, icons, and modern styling in Steps 59-65; added collapsible filter row with toggle button in Step 65; removed low stock metric in Step 72; moved "Clear All Filters" button to card header and separated JavaScript into inventory.js in Step 72; fixed CSV import issue with condition fields in Step 80; enhanced item models for different types in Step 81; barcode prefixes fixed in Step 83; type-specific incrementing attempts in Steps 84-85 unresolved.
  - CSV Actions: Buttons for "Upload Inventory CSV" (/items/upload_inventory) and "Export Inventory CSV" (/items/export_inventory), added in Step 49, fully functional.
  - Summary Metrics: Displays "Total Items" count above the table, added in Step 65; "Low Stock" metric removed in Step 72 per user request; "Total Items" remains functional and tested.
- Add Item (/items/add): Fully functional form for adding items manually with type-specific fields, enhanced in Step 81, barcode prefixes fixed in Step 83, date fields ordered as Provisioned Date, Received Date, Refresh Date Option, Refresh Date with "Last Power Wash" label removed in Step 89.
  - Form:
    - Item Type: Dropdown (Chromebook/Power Adapter/Bag), JavaScript toggles fields with toggleFields() (Step 34), updated in Step 81 to handle different item types.
    - Barcode: Readonly, intended to use USD349-CB-<num> for Chromebooks, USD349-PWR-<num> for Power Adapters, USD349-BAG-<num> for Bags with type-specific incrementing, but incrementing remains unresolved (Steps 83-85).
    - Chromebook Fields:
      - Serial Number, Model: Required text inputs (Step 34).
      - Provisioned Date: Date input, defaults to today (e.g., 2025-04-11), label simplified in Step 89.
      - Received Date: Date input, defaults to today, added in Step 36, repositioned in Step 89.
      - Refresh Date Option: Radio buttons (Auto: 5 years from received date, Manual: editable), added in Step 36, repositioned in Step 89.
      - Refresh Date: Date input, defaults to 5 years out (e.g., 2030-04-11), JavaScript toggles editability with toggleRefresh(), added in Step 36, repositioned in Step 89.
      - Overall Condition: Dropdown (New, Excellent, Very Good, Good, Damaged - Usable, Needs Repair, Damaged Beyond Repair, Retired, Lost/Stolen, Unknown), established in Step 36.
      - Disposition: Dropdown (For Parts/Disposed), appears if "Damaged Beyond Repair" is selected via toggleDisposition(), added in Step 36.
      - Bezel Condition: Dropdown (New, Good, Damaged - Usable, Broken, Missing, Unknown), established in Step 36.
      - Hinge Cap: Dropdown (New, Good, Damaged, Missing, Unknown), transitioned from Boolean to String in Step 35.
    - Power Adapter Fields:
      - Serial Number, Model: Required text inputs (Step 81).
      - Received Date: Date input, defaults to today (Step 81).
      - Condition: Dropdown (New, Excellent, Very Good, Good, Fair, Poor, Damaged, Unknown), added in Step 81; pending update.
    - Bag Fields:
      - Received Date: Date input, defaults to today (Step 81).
      - Condition: Dropdown (New, Excellent, Very Good, Good, Fair, Poor, Damaged, Unknown), added in Step 81; pending update.
      - No Serial Number or Model fields as bags don’t have these (Step 81); manufacturer field pending.
  - Submit: Redirects to item detail page (/items/lookup?lookup_type=barcode&identifier=<barcode>), updated in Step 36.
- Item Detail (/items/lookup): Fully functional after reapplying student relationship in Step 95; displays item conditions and history, date fields reordered to Provisioned Date, Refresh Date, Received Date for Chromebooks in Step 89.
  - Query: GET request with lookup_type (barcode/serial) and identifier, retrieves item from Item table (Step 34).
  - Display: Table with Barcode, Serial Number, Model, Type; Chromebook-specific fields in order: Provisioned Date, Refresh Date, Received Date, Overall Condition, Disposition (if "Damaged Beyond Repair"), Bezel Condition, Hinge Cap, Current Student; non-Chromebook fields: Condition, Received Date, Current Student; condition fields fixed in Step 80, date order corrected in Step 89, student relationship error fixed in Steps 91 and 95.
  - History: Table with Student (name + barcode from Step 41, fixed in Step 91), Grade at Checkout (e.g., "12" from Step 42), Checkout Date, Checkin Date (or "Active"), introduced in Step 39, mapping fixed in Step 92, debug logging added in Step 93, error resolved in Step 95.
  - Actions: "Check Out" button if unassigned (links to /items/checkout/<barcode>), "Check In" if assigned (POST to /items/checkin/<barcode>), added in Step 37, "Remove Item" button with confirmation modal (POST to /items/delete/<id>), added in Step 50.
- Checkout (/items/checkout/<barcode>): Fully functional and tested.
  - GET: Displays a search form for students (name/grade) (Step 37).
  - POST: Searches Student table with case-insensitive match (ilike), presents a radio list (name, ID, grade), "Assign" button submits to /items/checkout/<barcode>/confirm (Step 37).
  - Confirm: Assigns the student to the Chromebook, logs an Assignment entry with grade_at_checkout, redirects to item detail (Step 37).
- Checkin (/items/checkin/<barcode>): Fully functional and tested, POST request ends the latest Assignment, clears current_student_id and student_barcode, redirects to item detail (Step 37).
- Add Student (/students/add): Fully functional and tested, form with Student ID, First Name, Last Name, Grade Level (dropdown 6-12), submits to student list page, added in Step 38, moved to modal in Step 50.
- Student List (/students/list): Fully functional and tested.
  - Table: Displays Student ID, Name, Grade Level, Barcode (added in Step 50), with Edit and Remove buttons per row (Step 50), sortable by columns and live-filterable by name, student ID, or barcode (Step 50).
  - Actions: "Add Student" and "Upload Students CSV" buttons at the top, using modals for inline actions (Step 50).
  - Upload: Processes CSV with columns (Student Id, Student First Name, Student Last Name, Grade Level Code), updates existing students or adds new ones (Step 49).
  - Edit (/students/edit/<id>): Updates student details via modal form (Step 50).
  - Delete (/students/delete/<id>): Removes student with confirmation modal (Step 50).
- Upload Inventory (/items/upload_inventory): Fully functional after fixes in Steps 80 and 92.
  - Form to upload a CSV with columns (barcode, serial_number, model, type, received_date, overall_condition, bezel_condition, hinge_cap, refresh_date, student_name or student_id, quantity), processes and adds items to database, assigns students by mapping names to IDs (Step 92); fixed condition fields in Step 80, enhanced for different item types in Step 81.
- Export Inventory (/items/export_inventory): Fully functional and tested, downloads a CSV of all devices with columns (barcode, serial_number, model, type, received_date, condition, overall_condition, bezel_condition, hinge_cap, refresh_date, current_student), updated in Step 81 to include the new general condition field.
- System Info (/info): Fully functional and tested, renders this text dynamically in a text area with a distinct black navbar per user preference, accessible only by direct URL (/info), not linked in navbar, route updated in Step 48, syntax error fixed in Step 94.

#### Key Decisions and Details
- Database: SQLite (inventory.db), reset for schema changes (e.g., grade_at_checkout in Step 42, hinge_cap type change in Step 35, quantity added in Step 66 with reset in Step 67, condition added in Step 82); modified in Step 81 to add the general condition field and make serial_number and model nullable for bags; reset recommended in Step 93 and Step 95 to fix data inconsistencies.
- Barcodes: Initially assigned USD349-CB-<id> for Chromebooks (corrected in Step 40), USD349-<id> for others, padded to 5 digits from last item’s id; updated to USD349-CB-<num>, USD349-PWR-<num>, USD349-BAG-<num> with type-specific intent in Step 83, attempts to fix incrementing in Steps 84-85 unresolved.
- Student Barcodes: Generated as <grad_year>-<student_id> (e.g., 2025-160420 for a 12th grader in 2025), calculated in helpers.py using a grade-to-graduation-year mapping (Step 37).
- Grade Tracking: grade_at_checkout in Assignment preserves the grade at the time of assignment, implemented in Step 42.
- UI: Began with basic HTML, upgraded to Bootstrap 5.3 in Step 34, added consistent navbar in Step 44, enhanced with base.html in Step 48, updated with school branding and CSV features in Step 49, student list polished in Step 50, item inventory table modernized in Steps 57-65, low stock removed in Step 72, scripts separated in Step 72; CSV import issue with condition fields fixed in Step 80; enhanced item type handling in Step 81; system_info.html uses black navbar per user preference confirmed post-Step 81; date field order corrected in Steps 87-89; lookup error fixed in Steps 91 and 95; system_info.py syntax fixed in Step 94.
- Modularity: Transitioned to blueprints in Step 26, separated models into item.py, student.py, assignment.py (relationship added in Step 91, reapplied in Step 95), utilized helpers.py, removed obsolete app.py in Step 53, added inventory.js in Step 72.
- Error Resolutions:
  - UnboundLocalError: item_type undefined in add_item GET route, fixed in Step 40.
  - OperationalError: Schema mismatches (e.g., grade_at_checkout in Step 42, quantity in Step 67, condition in Step 82), addressed by resets.
  - TypeError: hinge_cap Boolean vs. string mismatch fixed in Step 35; student_name invalid argument in Assignment fixed in Step 70.
  - UI Formatting: Refined home page in Steps 46-47, resolved "System Info" display in Step 48, fixed "Clear All Filters" formatting in Step 72.
  - KeyError: Fixed CSV upload for students in Step 49.
  - IntegrityError: Handled duplicate student_id in Step 49, fixed NOT NULL constraint on type in Step 69, fixed chromebook_id in Step 52.
  - UndefinedError: Fixed Student undefined error in index.html in Step 50; fixed 'assignment.student' undefined error in item_detail.html by adding relationship in Step 91 and fixing CSV import mapping in Step 92.
  - AttributeError: Fixed 'Assignment' object has no attribute 'student' in item_routes.py by reapplying student relationship and adding defensive checks in Step 95.
  - SyntaxError: Corrected exception handling in student_routes.py (Step 50); fixed invalid syntax in system_info.py in Step 94.
  - TemplateRuntimeError: Fixed invalid 'less_than' test in Step 66.
  - Not Found: Restored upload_inventory route in Step 68.
  - CSV Import Issue: Condition fields not importing post-Step 67 reset, multiple fix attempts (Steps 74-77) unsuccessful; resolved in Step 80 by improving SQLAlchemy inheritance handling, enhancing data validation, optimizing database operations; student name mapping fixed in Step 92.
  - BadRequestKeyError: Fixed refresh_date_option field name mismatch in Step 81.
  - Item Type Specifics: Enhanced item models in Step 81; barcode prefixes in Step 83; type-specific incrementing attempts in Steps 84-85 unresolved; date field positioning in Steps 87-89; lookup error in Steps 91-95.

#### Current State (Step 95)
- Home Page: Enhanced with fixed navbar (Red gradient, White text, Black hover effects, Trojan logo), side-by-side search, card table (Barcode, Model, Serial Number, Overall Condition, Assigned To, Type), CSV upload/export buttons, light background, shadows, and hover effects via base.html (Steps 48-49); sortable with per-column filters (Step 57); modernized with collapsible filters, sticky header, and "Total Items" metric (Step 65); low stock metric removed (Step 72); "Clear All Filters" button moved to header and scripts separated into inventory.js (Step 72); fully functional with CSV import issue fixed in Step 80; database reset in Step 82 for condition field; barcode prefixes corrected in Step 83; type-specific barcode incrementing unresolved (Steps 84-85).
- Add Item Page: Date fields correctly ordered as Provisioned Date, Received Date, Refresh Date Option, Refresh Date, with "Last Power Wash" label removed from Provisioned Date (Step 89).
- Item Detail Page: Date fields ordered as Provisioned Date, Refresh Date, Received Date for Chromebooks (Step 89); error in history table (AttributeError: no attribute 'student') fixed by reapplying student relationship in assignment.py and adding defensive checks in item_routes.py (Step 95).
- All Features: Fully functional—add items (with type-specific fields and corrected date order), add students, checkout/checkin with history (fixed in Steps 91-95), item details with remove option, student list with edit/remove, navigation, CSV upload for students, CSV export for devices, "System Info" page (unlinked, accessible via /info) with dynamic content and black navbar; CSV upload for inventory saves condition fields (Step 80) and maps student names to IDs (Step 92); enhanced item model for different types (Step 81); database schema aligned in Step 82; barcode incrementing unresolved.
- Files: Templates extend base.html with fixed navbar (Step 48), except system_info.html with black navbar; item_routes.py includes routes with updated CSV import logic (Step 92), debug logging (Step 93), and lookup fix (Step 95), unresolved barcode logic (Step 85); student_routes.py includes student management routes; assignment.py updated with student relationship (Step 91, reapplied in Step 95); system_info.py syntax fixed (Step 94), updated (Step 95); app.py obsolete (Step 53); inventory.js added (Step 72).
- System Info Page: Displays this text in a text area, accessible only by direct URL (/info), uses a distinct black navbar per user preference confirmed post-Step 81, route updated in Step 48, syntax error fixed in Step 94.
- Resolved Issues: CSV import fixed in Step 80; item type-specific fields in Step 81; database schema mismatch in Step 82; barcode prefixes in Step 83; date positioning in Steps 87-89; initial /items/lookup errors fixed in Steps 91-95; system_info.py syntax error fixed in Step 94.
- Unresolved Issues: Barcode type-specific incrementing (Steps 84-85).

#### Pending Tasks
- Fix Barcode Incrementing:
  - Goal: Ensure barcodes increment per type (e.g., USD349-CB-00001, USD349-PWR-00001, USD349-BAG-00001) independently.
  - Details: Debug item_routes.py, add logging, test with fresh database reset, revise max-number calculation to strictly match prefixes.
- Power Adapter Conditions:
  - Goal: Update condition options to New, Good, Damaged - Usable, Broken, Retired, Unknown.
  - Details: Modify add_item.html and item_routes.py to enforce these options for Power Adapters.
- Bag Enhancements:
  - Goal: Add an optional manufacturer field and simplify conditions to New, Excellent, Good, Fair, Damaged, Unknown, Retired.
  - Details: Update item.py to add manufacturer to Bag model, modify add_item.html and item_routes.py, reset database for schema change.
- Item Type Settings:
  - Goal: Develop a master configuration area to define fields per item type (e.g., Chromebook: conditions, Power Adapter: minimal).
  - Details: Implement a new route (/settings/), create a model (e.g., ItemType: name, fields list), design a UI form to add/edit types, add a navbar link if requested, and enable dynamic form updates in add_item.
- Photos for All Items:
  - Goal: Add functionality to upload and store photos for all items (Chromebooks, power adapters, bags).
  - Details: Add a photo_path field to the Item model, create an upload route, display photos in item details.
- Multiple Item Checkouts:
  - Goal: Allow students to check out multiple items (1 Chromebook, 1 charger, 1 bag), with warnings if they already have an item of the same type.
  - Details: Modify the data model to support multiple assignments, update checkout logic to check for existing items and display warnings.
- Student Item View:
  - Goal: Allow viewing all items checked out by a student from the student object.
  - Details: Add a new route (/students/<id>/items) and template to display active assignments for a student.
- Improve Add Item Form:
  - Goal: Refine the add item form to make it less clunky.
  - Details: Analyze usability issues, potentially group fields into sections, improve layout and JavaScript behavior.
- System Info Navbar Consistency:
  - Goal: Consider aligning system_info.html navbar with base.html (red gradient) instead of black, per original Step 48 design, unless user prefers distinction.
  - Details: Update system_info.html to extend base.html if requested; currently black per user confirmation post-Step 81.

#### Change History
- Step 1-33 (Pre-April 09, 2025): Initial setup with app.py, basic Chromebook features, student management, checkout/checkin, raw HTML UI.
- Step 34 (April 09, 2025): Integrated Bootstrap 5.3, refactored to blueprints, separated models.
- Step 35 (April 09, 2025): Corrected hinge_cap from Boolean to String, updated item.py, reset database.
- Step 36 (April 09, 2025): Enhanced add_item with condition options, refresh date logic, redirected to detail page.
- Step 37 (April 09, 2025): Added checkout/checkin routes, history table in item detail.
- Step 38 (April 09, 2025): Added student routes (add_student, list_students).
- Step 39 (April 09, 2025): Added history table to item detail page.
- Step 40 (April 09, 2025): Corrected Chromebook barcode prefix to USD349-CB-<id>, added student names to history.
- Step 41 (April 09, 2025): Added student names to current student field.
- Step 42 (April 09, 2025): Added grade_at_checkout to Assignment, updated history table, reset database.
- Step 43 (April 09, 2025): Added student list page.
- Step 44 (April 09, 2025): Implemented navbar across all pages.
- Step 45 (April 09, 2025): Added filterable item list to home page.
- Step 46-47 (April 09, 2025): Polished home page with card layout, custom styling.
- Step 48 (April 09, 2025): Added "System Info" page with dynamic content from app/system_info.py, made unlinked but accessible via /info, implemented uniform layout with base.html, revised instructions for proactive updates; affected files: base.html, index.html, add_item.html, item_detail.html, add_student.html, student_list.html, checkout.html, system_info.html, item_routes.py, __init__.py, system_info.py.
- Step 49 (April 09, 2025): Enhanced navbar with gradient, padding, and hover effects, added CSV upload for inventory (/items/upload_inventory) and students (/students/list), added CSV export for devices (/items/export_inventory), updated device list on main page, fixed CSV upload for students; affected files: base.html, index.html, upload_inventory.html, upload_students.html, student_list.html, item_routes.py, student_routes.py, system_info.py.
- Step 50 (April 09, 2025): Added student barcode to student list, updated filter, moved "Add Student" and "Upload Students CSV" buttons to top of student list, removed "Add Student" from navbar, polished formatting, added edit/remove functionality, fixed SyntaxError; affected files: base.html, student_list.html, item_detail.html, student_routes.py, item_routes.py, system_info.py.
- Step 51 (April 10, 2025): Transformed Chromebook inventory CSV, mapped Assigned To names to student_id, updated upload_inventory; affected files: item_routes.py, system_info.py.
- Step 52 (April 10, 2025): Fixed IntegrityError in upload_inventory by committing Chromebook before Assignment; affected files: item_routes.py, system_info.py.
- Step 53 (April 10, 2025): Validated project files, identified app.py as obsolete; affected files: system_info.py.
- Step 54 (April 10, 2025): Added provisioned_date to item details page, updated system_info.py with user preferences; affected files: item_detail.html, system_info.py, add_item.html, item_routes.py (retrospectively documented).
- Step 55 (April 10, 2025): Updated system_info.py with user feedback on session details; affected files: system_info.py.
- Step 56 (April 10, 2025): Removed redundant Date sub-bullet from Change History; affected files: system_info.py.
- Step 57 (April 10, 2025): Made item inventory table sortable with column filters, updated system_info.py; affected files: index.html, system_info.py.
- Step 58 (April 10, 2025): Removed redundant "Filter by Type" dropdown, improved filter appearance; affected files: index.html, system_info.py.
- Step 59 (April 10, 2025): Modernized filter design with integrated filters, removed labels; affected files: index.html, system_info.py.
- Step 60 (April 10, 2025): Integrated filters into table header with icons, user feedback indicated it looked worse; affected files: index.html, system_info.py.
- Step 61 (April 10, 2025): Changed header to white, fixed text visibility; affected files: index.html, system_info.py.
- Step 62 (April 10, 2025): Fixed alignment, added sticky header, hover effects, filter toggle, custom sorting indicators; user feedback noted unclear elements and worsened layout; affected files: index.html, system_info.py.
- Step 63 (April 10, 2025): Switched to DataTables for modern table, user rejected due to loss of per-column filters; affected files: index.html, system_info.py.
- Step 64 (April 10, 2025): Reverted to custom table, restored per-column filters, fixed alignment; user approved as "worlds better"; affected files: index.html, system_info.py.
- Step 65 (April 10, 2025): Enhanced table with collapsible filters, modern styling, sticky header, summary metrics; affected files: index.html, system_info.py.
- Step 66 (April 10, 2025): Added quantity field to Item model, fixed TemplateRuntimeError, reset database; affected files: item.py, index.html, item_routes.py, system_info.py.
- Step 67 (April 10, 2025): Fixed OperationalError by resetting database after quantity addition; affected files: item_routes.py, system_info.py.
- Step 68 (April 10, 2025): Restored upload_inventory route after Not Found error; affected files: item_routes.py, system_info.py.
- Step 69 (April 10, 2025): Fixed IntegrityError in upload_inventory by setting type explicitly; affected files: item_routes.py, system_info.py.
- Step 70 (April 10, 2025): Fixed TypeError in upload_inventory by removing student_name; affected files: item_routes.py, system_info.py.
- Step 71 (April 10, 2025): Attempted to fix low stock metric with quantity in CSV, user requested removal; affected files: item_routes.py, system_info.py (incomplete update).
- Step 72 (April 10, 2025): Removed low stock metric, moved "Clear All Filters" button to header, separated JavaScript into inventory.js; user approved toggle but noted formatting issue with clear button; affected files: index.html, inventory.js, item_routes.py, system_info.py.
- Step 73 (April 10, 2025): Updated system_info.py with all changes up to Step 72 (incomplete due to interruption); affected files: system_info.py.
- Step 74 (April 10, 2025): Attempted to fix CSV import for condition fields with separate transactions; user reported conditions still not importing; affected files: item_routes.py, system_info.py.
- Step 75 (April 10, 2025): Enhanced CSV import debugging, user reported no change after fresh database reset attempt; affected files: item_routes.py, system_info.py.
- Step 76 (April 10, 2025): Adjusted CSV import to handle condition fields explicitly; no success reported; affected files: item_routes.py, system_info.py.
- Step 77 (April 10, 2025): Further debugging of CSV import with logging; user reported persistent failure; affected files: item_routes.py, system_info.py.
- Step 78 (April 10, 2025): Reported ongoing CSV import failure, updated system_info.py instructions for proactive updates; affected files: system_info.py.
- Step 79 (April 10, 2025): Refined system_info.py documentation process; affected files: system_info.py.
- Step 80 (April 10, 2025): Fixed CSV import issue by improving SQLAlchemy inheritance handling, enhancing data validation, optimizing database operations, and adding verification steps; condition fields now save correctly; affected files: item_routes.py, system_info.py.
- Step 81 (April 10, 2025): Enhanced item models to handle type-specific fields (Chromebooks with detailed conditions, PowerAdapters with condition, Bags with no serial/model but with condition); fixed barcode display in add_item form; affected files: item.py, add_item.html, item_routes.py, system_info.py.
- Step 82 (April 10, 2025): Addressed OperationalError: no such column: item.condition by resetting inventory.db to align with current Item model including condition field; no files directly modified, database reset manually; affected documentation: system_info.py.
- Step 83 (April 10, 2025): Fixed barcode prefixes to use USD349-CB-, USD349-PWR-, USD349-BAG- for Chromebooks, Power Adapters, and Bags respectively; affected files: item_routes.py, add_item.html, system_info.py.
- Step 84 (April 10, 2025): Attempted to fix type-specific barcode incrementing using count per type, but still tied to global id; affected files: item_routes.py, system_info.py.
- Step 85 (April 10, 2025): Corrected type-specific barcode incrementing attempt by parsing the highest numeric part of existing barcodes per type; refined instructions to use `code {file_path}` format; affected files: item_routes.py, system_info.py; incrementing unresolved.
- Step 86 (April 10, 2025): Attempted to ensure received_date displays in item_detail.html for all types; affected files: item_detail.html, system_info.py; misinterpreted user intent.
- Step 87 (April 10, 2025): Corrected received_date display, removed from index.html, positioned in item_detail.html, but not next to refresh_date; affected files: index.html, item_detail.html, system_info.py.
- Step 88 (April 10, 2025): Repositioned received_date next to refresh_date in item_detail.html for Chromebooks; affected files: item_detail.html, system_info.py.
- Step 89 (April 10, 2025): Corrected date field order in add_item.html (Provisioned, Received, Refresh Option, Refresh) and item_detail.html (Provisioned, Refresh, Received), removed "Last Power Wash" label; affected files: add_item.html, item_detail.html, system_info.py.
- Step 90 (April 10, 2025): Updated system_info.py to reflect all changes, noted unresolved barcode incrementing and new /items/lookup error, paused due to user time constraint; affected files: system_info.py.
- Step 91 (April 11, 2025): Fixed UndefinedError in item_detail.html by adding student relationship to Assignment model; updated system_info.py; affected files: assignment.py, system_info.py.
- Step 92 (April 11, 2025): Fixed CSV import in upload_inventory to map student names to student_id, resolving lookup error for imported checked-out items; updated system_info.py; affected files: item_routes.py, system_info.py.
- Step 93 (April 11, 2025): Added debug logging to lookup in item_routes.py to diagnose persistent UndefinedError, recommended database reset and CSV re-import; updated system_info.py; affected files: item_routes.py, system_info.py.
- Step 94 (April 11, 2025): Fixed SyntaxError in system_info.py by correcting string literal format; updated to reflect Step 93’s debugging intent; affected files: system_info.py.
- Step 95 (April 11, 2025): Reapplied student relationship in assignment.py, added defensive checks in item_routes.py lookup route to fix AttributeError, recommended database reset and CSV re-import; updated system_info.py; affected files: assignment.py, item_routes.py, system_info.py.
"""