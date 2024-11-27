import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Funktion zur Auswahl des Ordners
def select_folder():
    folder_path = filedialog.askdirectory(title="Wählen Sie einen Ordner")
    return folder_path

# Funktion zum Löschen von Dateien, die älter als das angegebene Datum sind
def delete_old_files(folder_path, date_threshold):
    # Wandelt das eingegebene Datum in ein datetime-Objekt um
    threshold = datetime.strptime(date_threshold, "%Y-%m-%d")
    
    # Durchläuft alle Dateien im Ordner
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Überspringt Unterordner
        if os.path.isdir(file_path):
            continue
        
        # Holt sich das Änderungsdatum der Datei
        file_mtime = os.path.getmtime(file_path)
        file_date = datetime.fromtimestamp(file_mtime)
        
        # Wenn das Änderungsdatum älter als das angegebene Datum ist, wird die Datei gelöscht
        if file_date < threshold:
            os.remove(file_path)
            print(f"Datei gelöscht: {filename}")

# Hauptprogramm
def main():
    # Tkinter-Root-Fenster, das für den Dialog geöffnet wird
    root = tk.Tk()
    root.withdraw()  # Fenster nicht anzeigen
    
    # Datumseingabe durch den Benutzer
    date_input = input("Geben Sie das Datum ein (YYYY-MM-DD): ")
    
    # Ordner auswählen
    folder_path = select_folder()
    if not folder_path:
        print("Kein Ordner ausgewählt. Programm beendet.")
        return
    
    # Alte Dateien löschen
    delete_old_files(folder_path, date_input)
    print("Vorgang abgeschlossen.")

if __name__ == "__main__":
    main()
