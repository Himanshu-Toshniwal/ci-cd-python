import pytest
import tempfile
import os
from src.main import NotesApp

@pytest.fixture
def temp_notes_app():
    """Create a temporary notes app for testing"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        app = NotesApp(tmp.name)
        yield app
        os.unlink(tmp.name)

@pytest.fixture
def sample_notes_app():
    """Create a notes app with sample data"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        app = NotesApp(tmp.name)
        app.add_note("Python Tutorial", "Learn Python basics")
        app.add_note("Shopping List", "Milk, Bread, Eggs")
        app.add_note("Meeting Notes", "Discuss project timeline")
        yield app
        os.unlink(tmp.name)