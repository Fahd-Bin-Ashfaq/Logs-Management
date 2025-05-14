## 📄 **MetaScan - File Metadata Viewer**

---

### 📌 **Overview**

MetaScan is a simple yet powerful Python-based desktop application that allows users to scan any folder and extract metadata from all files within it. This includes details like file type, size, permissions, and timestamps. The extracted metadata can be exported as a CSV file for further analysis.

---

### ⚙️ **Features**

* 📁 Select and scan any folder
* 🔢 Extract metadata for all files:

  * File Name
  * File Type (e.g., Word, PDF, Image, etc.)
  * File Size in KB
  * File Permissions
  * Created Date
  * Modified Date
  * Accessed Date
* 📄 Export metadata as a CSV file
* ↕ Sort data by any column in the table
* 🚀 Lightweight and beginner-friendly

---

### 📆 **Technologies Used**

| Technology      | Purpose                     |
| --------------- | --------------------------- |
| Python          | Programming language        |
| Tkinter         | GUI Interface               |
| OS module       | File handling and traversal |
| CSV module      | Exporting data to CSV       |
| stat & datetime | Permissions and timestamps  |

---

### 🚀 **Running the Application**

#### From Source:

```bash
python MetaScan.py
```

#### Compiled Version:

Just double-click `MetaScan.exe` (created using PyInstaller).

---

### 🚧 **How to Deploy (Convert to .exe)**

To compile this script into an executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile MetaScan.py
```

The `.exe` file will be found in the `dist/` folder.

---

### 🧑‍💻 **Developer**

* **Fahad Ahmed**
  Software Engineering Student, Sindh Madressatul Islam University

---

### 📄 **License**

This project is open-source and available for educational and personal use. Feel free to modify and distribute with proper credit.
