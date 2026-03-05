# 🚀 Smart AI File Organizer

An intelligent Python application that automatically organizes files into folders using rule-based and AI-based classification.  
It also includes a graphical interface for easy file management.

---

## 📌 Features

✔ Automatic file organization  
✔ AI-based file categorization  
✔ Drag & Select folder using GUI  
✔ Duplicate file handling  
✔ Modular project structure  
✔ Easy to extend and automate  

---

## 🛠 Tech Stack

- Python
- Tkinter (GUI)
- OS module
- Shutil module

---

## 📂 Project Structure

```
smart-file-organizer
│
├── main.py              # CLI version
├── gui.py               # GUI application
├── organizer.py         # File organization logic
├── ai_classifier.py     # AI categorization logic
├── config.py            # File type configuration
├── logger.txt           # Activity logs
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/smart-file-organizer.git
```

Navigate into the project

```
cd smart-file-organizer
```

Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### CLI Version

```
python main.py
```

This will organize files in your **Downloads folder**.

---

### GUI Version

```
python gui.py
```

Then:

1. Click **Select Folder**
2. Choose the folder
3. Files will be organized automatically

---

## 🤖 AI File Categorization

The system classifies files using simple intelligent rules.

Example:

| File Name | Category |
|-----------|----------|
| invoice_2024.pdf | Finance |
| resume_john.pdf | Career |
| photo.png | Images |

---

## 📸 Example Output

Before:

```
Downloads
│
├── invoice.pdf
├── photo.jpg
├── resume.pdf
```

After:

```
Downloads
│
├── Finance
│   └── invoice.pdf
│
├── Images
│   └── photo.jpg
│
└── Career
    └── resume.pdf
```

---

## 💡 Future Improvements

- Drag & Drop folder support
- Machine Learning based classification
- Real-time folder monitoring
- Cloud backup integration

---

## 👨‍💻 Author

**Krisha Thakar**

Python Developer | Data Science Enthusiast

---

⭐ If you found this project useful, please give it a star!