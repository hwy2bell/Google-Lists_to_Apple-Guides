# Google-Lists_to_Apple-Guides
Python script to clean Google Lists copy/paste and generate Apple Maps search links. Works alongside an Apple Shortcut for quick transfer of saved locations.

This repository contains a Python script and an Apple Shortcut that work together to transfer places saved in **Google Maps** to **Apple Maps** quickly and efficiently.

## 📌 Overview
If you have a list of places saved in **Google Maps** and want to transfer them to **Apple Maps**, this tool will automate the process. Instead of manually searching for each location, this script:
1. **Extracts** the places from a copied Google Maps list, not Takeout or JSON data.
2. **Cleans** the list by removing unnecessary text (notes and weird characters).
3. **Generates** Apple Maps search links.
4. **Automates** the opening of links in Apple Maps, making it easy to save them.

---

## 📖 How It Works

### Step 1: Copy Your Google Maps List
1. Open **Google Maps**.
2. Tap **"Saved"** and select the list you want to transfer.
3. Tap the **three dots (⋮)** in the top-right corner.
4. Select **"Edit List"**.
5. Starting with the **first place name**, select **all** the text, including **name, address, and notes**.
6. **Copy** the text.

### Step 2: Prepare the Input File
1. Open `input.txt` in this repository.
2. Paste the copied text from Google Maps into `input.txt`.
3. Save the file.

### Step 3: Run the Python Script
1. Run the script to clean the data and generate Apple Maps links:
   ```bash
   python generate_apple_maps_links.py
2. The script will generate a file named `apple_maps_links.txt`.
3. Open the file to verify that all locations have been converted into Apple Maps links.

### Step 4: Open the Links in Apple Maps
1. Run the **Apple Shortcut** (linked below).
2. When prompted, select the `apple_maps_links.txt` file.
3. **Apple Maps will open each place**, allowing you to save it.
4. After saving, **navigate back to Shortcuts**, and it will automatically bring up the next map link.
5. Repeat until all locations are transferred.

---

## 🛠 Installation & Requirements

### 📌 Requirements
- **Python 3.x** installed on your computer (free to install).
- An **iPhone, iPad, or Mac** with the **Shortcuts app** installed.
- The **Apple Shortcut** (linked below).

### 📥 Install the Apple Shortcut
You can use this **Apple Shortcut** to process the cleaned links automatically:

👉 **[Install the Shortcut](https://www.icloud.com/shortcuts/01d548c82135425eab3de7420e0b72aa)**

---

## 📜 License
This project is licensed under the **MIT License**, meaning you’re free to use, modify, and distribute it as you see fit.

---

## 🤝 Contributing
If you have ideas for improvements, feel free to submit a pull request or open an issue!
