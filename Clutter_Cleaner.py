import os

def main_menu():
    print("""=============================
     Folder Clutter Cleaner
=============================

1. Create your Project
2. Set a Password
3. Enter the Folder Path
4. Rename all files
5. Rename files of a specific extension
6. Show file extensions in the folder
7. Show total number of files
8. Move files into folders by type
9. Exit

=============================
""")

class ClutterCleaner:
    def __init__(self, project_name):
        self.count = 0
        self.password = "admin"
        self.files_count = 0
        self.files_extensions_list = []
        self.files_list = []
        self.project_name = project_name.strip()

    def update_files_list(self):
        self.files_list = os.listdir()

    def get_path(self, folder_path):
        os.chdir(folder_path)
        self.update_files_list()
        print("✅ Path Entered Successfully!")

    def rename_all_files(self, default_name):
        self.count = 0
        self.update_files_list()
        for file in self.files_list:
            if os.path.isfile(file):
                name, ext = os.path.splitext(file)
                self.count += 1
                os.rename(file, f"{default_name}_{self.count}{ext}")
        self.update_files_list()
        print("✅ All files renamed successfully!")

    def rename_files(self, ext, default_file_name):
        self.count = 0
        self.update_files_list()
        renamed = False
        for file in self.files_list:
            if os.path.isfile(file):
                _, file_ext = os.path.splitext(file)
                if file_ext == ext:
                    self.count += 1
                    os.rename(file, f"{default_file_name}_{self.count}{ext}")
                    renamed = True
        if renamed:
            print(f"✅ All files with '{ext}' renamed successfully!")
        else:
            print(f"⚠️ No files with extension '{ext}' found.")
        self.update_files_list()

    def files_extensions(self):
        self.update_files_list()
        self.files_extensions_list = []
        for file in self.files_list:
            if os.path.isfile(file):
                _, ext = os.path.splitext(file)
                if ext and ext not in self.files_extensions_list:
                    self.files_extensions_list.append(ext)
        print(f"📂 Files Extensions: {self.files_extensions_list}")

    def file_count_by_numbers(self):
        self.update_files_list()
        self.files_count = 0
        for file in self.files_list:
            if os.path.isfile(file):
                self.files_count += 1
        print(f"📊 Total Number of Files: {self.files_count}")

    def move_file_to_folder(self, folder_name, ext):
        self.update_files_list()
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"📂 '{folder_name}' Folder Created Successfully!")
        else:
            print(f"ℹ️ '{folder_name}' Already Exists!")

        moved = False
        for file in self.files_list:
            if os.path.isfile(file):
                _, file_ext = os.path.splitext(file)
                if file_ext == ext:
                    os.replace(file, os.path.join(folder_name, file))
                    moved = True
        if moved:
            print(f"✅ Files with extension '{ext}' moved to '{folder_name}' successfully.")
        else:
            print(f"⚠️ No files with extension '{ext}' found to move.")
        self.update_files_list()


# Main Program Loop
my_clutter = None
while True:
    main_menu()
    try:
        user_choice = int(input("👉 Enter your choice: ").strip())
        if user_choice < 1 or user_choice > 9:
            raise Exception("Invalid Input! (Numbers must be between 1 and 9)")
    except ValueError:
        print("❌ Error: Only Integers are allowed!")
    except Exception as e:
        print(f"❌ Error: {e}")
    else:
        if user_choice == 1:
            my_clutter = ClutterCleaner(input("Enter the name of your Project: "))
            print(f"🎉 Project '{my_clutter.project_name}' Created Successfully!")
        elif user_choice == 2:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Set Password!")
            else:
                my_clutter.password = input("Enter your password here: ").strip()
                print("🔑 Password Set Successfully!")
        elif user_choice == 3:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Enter the Folder Path!")
            else:
                my_clutter.get_path(input("Enter Path of the Folder: ").strip())
        elif user_choice == 4:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Rename Files!")
            else:
                my_clutter.rename_all_files(input("Enter a Default Name for all Files: ").strip())
        elif user_choice == 5:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Rename Specific Files!")
            else:
                my_clutter.rename_files(
                    input("Enter the Extension of File (with dot, e.g. .png): ").strip(),
                    input("Enter a Default Name for all Files: ").strip()
                )
        elif user_choice == 6:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Check File Extensions!")
            else:
                my_clutter.files_extensions()
        elif user_choice == 7:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Count the Number of Files!")
            else:
                my_clutter.file_count_by_numbers()
        elif user_choice == 8:
            if my_clutter is None:
                print("⚠️ Error: Create a Project First to Move Files to a Folder!")
            else:
                my_clutter.move_file_to_folder(
                    input("Enter the Folder Name: ").strip(),
                    input("Enter the Extension of File (with dot, e.g. .jpg): ").strip()
                )
        elif user_choice == 9:
            if my_clutter is None:
                print("👋 Thanks for using the program! Exiting...")
                break
            else:
                user_password = input("Enter your password: ").strip()
                if user_password == my_clutter.password:
                    print("✅ Correct Password! Exiting...")
                    break
                else:
                    print("❌ Incorrect Password!")