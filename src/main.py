import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()
    
    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_notes(self):
        with open(self.filename, 'w') as f:
            json.dump(self.notes, f, indent=2)
    
    def add_note(self, title, content):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.notes.append(note)
        self.save_notes()
        return note["id"]
    
    def get_note(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                return note
        return None
    
    def update_note(self, note_id, title=None, content=None):
        note = self.get_note(note_id)
        if note:
            if title:
                note["title"] = title
            if content:
                note["content"] = content
            note["updated_at"] = datetime.now().isoformat()
            self.save_notes()
            return True
        return False
    
    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self.save_notes()
        return True
    
    def list_notes(self):
        return self.notes
    
    def search_notes(self, query):
        results = []
        for note in self.notes:
            if query.lower() in note["title"].lower() or query.lower() in note["content"].lower():
                results.append(note)
        return results

def main():
    app = NotesApp()
    
    while True:
        print("\n=== Notes App ===")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. View Note")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Search Notes")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        if choice == '1':
            title = input("Enter title: ")
            content = input("Enter content: ")
            note_id = app.add_note(title, content)
            print(f"Note added with ID: {note_id}")
        
        elif choice == '2':
            notes = app.list_notes()
            if notes:
                for note in notes:
                    print(f"\nID: {note['id']}")
                    print(f"Title: {note['title']}")
                    print(f"Content: {note['content'][:50]}...")
            else:
                print("No notes found.")
        
        elif choice == '3':
            note_id = int(input("Enter note ID: "))
            note = app.get_note(note_id)
            if note:
                print(f"\nTitle: {note['title']}")
                print(f"Content: {note['content']}")
                print(f"Created: {note['created_at']}")
            else:
                print("Note not found.")
        
        elif choice == '4':
            note_id = int(input("Enter note ID: "))
            title = input("Enter new title (or press Enter to skip): ")
            content = input("Enter new content (or press Enter to skip): ")
            if app.update_note(note_id, title or None, content or None):
                print("Note updated successfully.")
            else:
                print("Note not found.")
        
        elif choice == '5':
            note_id = int(input("Enter note ID: "))
            app.delete_note(note_id)
            print("Note deleted successfully.")
        
        elif choice == '6':
            query = input("Enter search query: ")
            results = app.search_notes(query)
            if results:
                for note in results:
                    print(f"\nID: {note['id']}")
                    print(f"Title: {note['title']}")
                    print(f"Content: {note['content'][:50]}...")
            else:
                print("No matching notes found.")
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
