# Inventory System History

## Current State (Step 98)
- **Home Page**: Enhanced with red gradient navbar, sortable/filterable table, CSV buttons, total items metric (Steps 48-65, 72, 80, 82, 83).
- **Add Item Page**: Type-specific fields, ordered dates (Step 89).
- **Item Detail Page**: Fixed lookup errors, ordered dates (Steps 89, 91, 95).
- **Features**: Fully functional add items, students, checkout/checkin, CSV, navigation.
- **Files**: Modular structure, `prompt.md` and `history.md` replace `system_info.py` (Step 98).
- **Version Control**: GitHub primary source, pushes per change (Steps 96-97).
- **Resolved**: CSV import (Step 80), item types (Step 81), lookup errors (Step 95).
- **Unresolved**: Barcode incrementing (Steps 84-85).

## Pending Tasks
- **Fix Barcode Incrementing**: Ensure type-specific sequences (USD349-CB-00001, etc.).
- **Power Adapter Conditions**: Update to New, Good, Damaged - Usable, Broken, Retired, Unknown.
- **Bag Enhancements**: Add manufacturer field, simplify conditions.
- **Item Type Settings**: Create configuration area for fields per type.
- **Photos for All Items**: Add photo upload/storage.
- **Multiple Item Checkouts**: Allow one of each type with warnings.
- **Student Item View**: Show all items per student.
- **Improve Add Item Form**: Reduce clunkiness.
- **System Info Navbar Consistency**: Consider aligning with base.html.

## Change History
- **Step 1-33 (Pre-April 09, 2025)**: Initial setup with app.py, Chromebook features, raw HTML.
- **Step 34 (April 09, 2025)**: Bootstrap 5.3, blueprints, separated models.
- ...
- **Step 96 (April 15, 2025)**: GitHub setup, .gitignore configuration.
- **Step 97 (April 15, 2025)**: Updated system_info.py for GitHub as source, per-change pushes.
- **Step 98 (April 15, 2025)**: Refactored system_info.py into prompt.md (static prompt) and history.md (dynamic updates), added README.md with high-level overview; affected files: prompt.md, history.md, README.md, __init__.py, combine_docs.py.