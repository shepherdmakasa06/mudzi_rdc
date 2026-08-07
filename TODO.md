# TODO - Governance dropdown admin editing

Goal: Make Council, Management and Awards editable in the admin panel.

- [x] 1. Create `app/models/award.py` (Award model)
- [x] 2. Register the Award model in `app/models/__init__.py`
- [x] 3. Add seed data for awards in `app/content_seed.py`
- [x] 4. Add `AwardAdminView` and register it in `app/admin/views.py`
- [x] 5. Update `/awards` route in `app/routes/main.py`
- [x] 6. Update `app/templates/public/awards.html` to render awards from DB
- [x] 7. Verify the app runs and the admin Awards screen appears
