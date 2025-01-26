import customtkinter as ctk
from tkinter import filedialog
import file_sorter_class_1 as f1


class FileSorter:
    file_path_global: str = ""

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

        self.file_path_label_1 = ctk.CTkLabel(self.window, text="File Path: ")
        self.file_path_label_1.grid(row=0, column=0, **self.padding)
        self.file_path_button = ctk.CTkButton(self.window, text="Select folder", command=self.open_folder)
        self.file_path_button.grid(row=0, column=1, **self.padding)

        self.file_path_label_2 = ctk.CTkLabel(self.window, text="Not selected")
        self.file_path_label_2.grid(row=0, column=2, **self.padding)

        self.file_sorting_button = ctk.CTkButton(self.window, text="Sort selected folder", command=self.sort)
        self.file_sorting_button.grid(row=1, column=1, **self.padding)

    @staticmethod
    def sort():
        f1.main(FileSorter.file_path_global)

    def open_folder(self) -> None:
        folder_path = filedialog.askdirectory()
        FileSorter.file_path_global = folder_path
        if folder_path:
            self.file_path_label_2.configure(text=folder_path.rsplit("/")[-1])

    def run(self) -> None:
        self.window.mainloop()


def main() -> None:
    return None


if __name__ == "__main__":
    main()
