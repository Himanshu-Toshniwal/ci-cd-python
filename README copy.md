# Python Notes App with CI/CD Pipeline

A simple yet powerful command-line notes application built with Python, featuring complete CI/CD pipeline using GitHub Actions.

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, Delete notes
- **Search Functionality**: Find notes by title or content
- **JSON Storage**: Persistent data storage in JSON format
- **Interactive CLI**: User-friendly command-line interface
- **Timestamps**: Track creation and modification times
- **CI/CD Pipeline**: Automated testing and deployment

## 📁 Project Structure

```
ci-cd-pipeline-getting-started/
├── .github/
│   └── workflows/
│       └── python-app.yml     # CI/CD pipeline configuration
├── src/
│   └── main.py                # Main application code
├── tests/
│   └── test_main.py           # Unit tests
├── conftest.py                # Pytest fixtures
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ci-cd-pipeline-getting-started
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Running the Application
```bash
python src/main.py
```

### Menu Options
1. **Add Note** - Create a new note
2. **View All Notes** - List all saved notes
3. **View Note** - Display specific note by ID
4. **Update Note** - Modify existing note
5. **Delete Note** - Remove note by ID
6. **Search Notes** - Find notes by keyword
7. **Exit** - Close the application

### Example Usage
```
=== Notes App ===
1. Add Note
2. View All Notes
3. View Note
4. Update Note
5. Delete Note
6. Search Notes
7. Exit

Enter choice (1-7): 1
Enter title: Python Tutorial
Enter content: Learn Python basics and advanced concepts
Note added with ID: 1
```

## 🧪 Testing

### Run Tests
```bash
pytest
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Test Coverage
The project includes comprehensive tests for:
- Adding notes
- Retrieving notes
- Updating notes
- Deleting notes
- Searching notes
- Listing all notes

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for automated CI/CD:

### Pipeline Steps
1. **Code Checkout** - Get latest code
2. **Python Setup** - Install Python 3.10
3. **Dependencies** - Install required packages
4. **Linting** - Code quality check with flake8
5. **Testing** - Run unit tests with pytest
6. **Deployment** - Deploy on main branch

### Workflow Triggers
- Push to `main` branch
- Pull requests to `main` branch

## 📊 Data Storage

Notes are stored in JSON format with the following structure:
```json
[
  {
    "id": 1,
    "title": "Sample Note",
    "content": "This is a sample note content",
    "created_at": "2024-01-01T12:00:00.000000",
    "updated_at": "2024-01-01T12:00:00.000000"
  }
]
```

## 🏗️ Architecture

### NotesApp Class
- `__init__(filename)` - Initialize with JSON file
- `add_note(title, content)` - Create new note
- `get_note(note_id)` - Retrieve specific note
- `update_note(note_id, title, content)` - Modify note
- `delete_note(note_id)` - Remove note
- `list_notes()` - Get all notes
- `search_notes(query)` - Find matching notes

## 🔧 Development

### Prerequisites
- Python 3.10+
- pytest for testing

### Code Style
- Follows PEP 8 standards
- Linted with flake8
- Maximum line length: 127 characters

### Contributing
1. Fork the repository
2. Create feature branch
3. Make changes
4. Run tests
5. Submit pull request

## 📝 License

This project is open source and available under the MIT License.

## 🚀 Future Enhancements

- [ ] Note categories/tags
- [ ] Export to different formats
- [ ] Note encryption
- [ ] Web interface
- [ ] Database integration
- [ ] User authentication

---

**Built with ❤️ using Python and GitHub Actions**