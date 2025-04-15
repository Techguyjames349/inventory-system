# Stafford USD #349 Inventory System

A Flask-based inventory management system for Stafford Unified School District #349, designed to track Chromebooks, power adapters, and bags, manage student assignments, and maintain detailed history.

## Overview
This system streamlines inventory management for school assets. It allows administrators to:
- Add and track items with type-specific details (e.g., Chromebook conditions, bag simplicity).
- Manage student checkouts and checkins with history tracking.
- Import and export inventory via CSV files.
- Filter and sort item and student lists for easy access.
- View system documentation at `/info` (direct URL).

Built with Flask, Flask-SQLAlchemy, SQLite, and Bootstrap 5.3, it’s designed for scalability, with potential for Google Cloud Platform migration.

## Status
Actively developed as of April 15, 2025 (Step 98). Detailed documentation is available in `app/docs/prompt.md` (core guidelines) and `app/docs/history.md` (update log).

## Next Steps
Refer to `app/docs/prompt.md` for development guidelines and `app/docs/history.md` for the latest changes.