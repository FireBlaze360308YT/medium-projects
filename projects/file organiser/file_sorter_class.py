import customtkinter as ctk
from tkinter import filedialog


class FileSorter:
    def __init__(self):
        # Window object
        self.window = ctk.CTk()
        self.window.title("File Sorter")
        self.window.geometry("640x360")
        self.window.resizable(False, False)
        print("Window Created")

        # Window initialization
        self.padding: dict = {"padx": 20, "pady": 10}
        print("Window initialized")

        self.file_path_label = ctk.CTkLabel(self.window, text="File Path: ")
        self.file_path_label.grid(row=0, column=0, **self.padding)
        self.file_path_button = ctk.CTkButton(self.window, text="Select folder", command=self.open_folder)
        self.file_path_button.grid(row=0, column=1, **self.padding)

        self.daje = ctk.CTkLabel(self.window, text="Not selected")
        self.daje.grid(row=0, column=2, **self.padding)

    def open_folder(self) -> None:
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.daje.configure(text=folder_path.rsplit("/")[-1])

    def run(self) -> None:
        self.window.mainloop()


def main() -> None:
    return None


if __name__ == "__main__":
    main()
