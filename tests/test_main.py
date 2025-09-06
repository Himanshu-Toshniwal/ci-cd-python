def test_add_note(temp_notes_app):
    note_id = temp_notes_app.add_note("Test Title", "Test Content")
    assert note_id == 1
    assert len(temp_notes_app.notes) == 1

def test_get_note(temp_notes_app):
    note_id = temp_notes_app.add_note("Test Title", "Test Content")
    note = temp_notes_app.get_note(note_id)
    assert note["title"] == "Test Title"
    assert note["content"] == "Test Content"

def test_update_note(temp_notes_app):
    note_id = temp_notes_app.add_note("Old Title", "Old Content")
    result = temp_notes_app.update_note(note_id, "New Title", "New Content")
    assert result == True
    note = temp_notes_app.get_note(note_id)
    assert note["title"] == "New Title"
    assert note["content"] == "New Content"

def test_delete_note(temp_notes_app):
    note_id = temp_notes_app.add_note("Test Title", "Test Content")
    temp_notes_app.delete_note(note_id)
    assert len(temp_notes_app.notes) == 0
    assert temp_notes_app.get_note(note_id) == None

def test_search_notes(sample_notes_app):
    results = sample_notes_app.search_notes("Python")
    assert len(results) == 1
    assert results[0]["title"] == "Python Tutorial"

def test_list_notes(sample_notes_app):
    notes = sample_notes_app.list_notes()
    assert len(notes) == 3
    assert notes[0]["title"] == "Python Tutorial"
