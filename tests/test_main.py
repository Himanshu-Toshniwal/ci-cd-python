import os
import tempfile
from src.main import NotesApp

def test_add_note():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        app = NotesApp(tmp.name)
        note_id = app.add_note("Test Title", "Test Content")
        assert note_id == 1
        assert len(app.notes) == 1
        os.unlink(tmp.name)

def test_get_note():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        app = NotesApp(tmp.name)
        note_id = app.add_note("Test Title", "Test Content")
        note = app.get_note(note_id)
        assert note["title"] == "Test Title"
        assert note["content"] == "Test Content"
        os.unlink(tmp.name)

def test_update_note():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        app = NotesApp(tmp.name)
        note_id = app.add_note("Old Title", "Old Content")
        result = app.update_note(note_id, "New Title", "New Content")
        assert result == True
        note = app.get_note(note_id)
        assert note["title"] == "New Title"
        assert note["content"] == "New Content"
        os.unlink(tmp.name)

def test_delete_note():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        app = NotesApp(tmp.name)
        note_id = app.add_note("Test Title", "Test Content")
        app.delete_note(note_id)
        assert len(app.notes) == 0
        assert app.get_note(note_id) == None
        os.unlink(tmp.name)

def test_search_notes():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        app = NotesApp(tmp.name)
        app.add_note("Python Tutorial", "Learn Python basics")
        app.add_note("Java Guide", "Java programming concepts")
        results = app.search_notes("Python")
        assert len(results) == 1
        assert results[0]["title"] == "Python Tutorial"
        os.unlink(tmp.name)

def test_list_notes():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        app = NotesApp(tmp.name)
        app.add_note("Note 1", "Content 1")
        app.add_note("Note 2", "Content 2")
        notes = app.list_notes()
        assert len(notes) == 2
        assert notes[0]["title"] == "Note 1"
        assert notes[1]["title"] == "Note 2"
        os.unlink(tmp.name)
