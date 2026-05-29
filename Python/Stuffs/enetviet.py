import asyncio
import ctypes
import psutil
import time
import tkinter as tk
import subprocess
import threading
from tkinter import messagebox

# ================= CONFIG =================
PASSWORD = "imnick"

TARGET_APPS = [
    "chrome.exe",
    "discord.exe",
    "steam.exe"
]

# ================= STATE =================
class LockState:import shutil
from datetime import datetime
import os
from colorama import Fore
import json
from colorama import Fore, Style, init
from datetime import timedelta
init(autoreset=True)  # Tự động reset màu sau mỗi lần print, không cần reset thủ công



script_dir = os.path.dirname(os.path.realpath(__file__))            # → "/home/tuaan/Desktop/.../Task-Deadline manager/TASK_FILE"                                                                   
                       
TASK_FILE = os.path.join(script_dir, "tasks.json")  

today = datetime.now().strftime("%Y-%m-%d")  # Lấy ngày hôm nay dạng "YYYY-MM-DD"

def clear():
    # Xóa màn hình terminal — "cls" cho Windows, "clear" cho Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")

# Lấy độ rộng terminal để căn giữa text cho đẹp
width = shutil.get_terminal_size().columns

def add_task():
    # Đọc danh sách task hiện có từ file, nếu file không tồn tại thì tạo list rỗng
    try:
        updated_task = []
        with open(TASK_FILE, "r") as file:
            updated_task = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        updated_task = []

    while True: 
        clear()
        print("Please enter your TASK name!".center(width))
        task_name = input(">>>")
        task_name_lower = task_name.lower()  # Chuyển về chữ thường để tránh trùng lặp kiểu "Math" vs "math"

        if is_duplicate(task_name_lower):  # Kiểm tra task đã tồn tại chưa
            clear()
            print(f"There is another task that named {task_name_lower} - You have 2 options: ".center(width))
            print(f"1. Set a new task with new deadline ")
            print(f"2. Set a new deadline for task: '{task_name_lower}'")
            
            replace_or_setnew = input(">>>")

            if replace_or_setnew == "1": 
                continue  # Quay lại đầu vòng lặp để nhập tên task mới
                clear()   # Dòng này không bao giờ chạy (unreachable sau continue)
            elif replace_or_setnew == "2": 
                clear()
                print("Opsie! There are 2 new options:")
                print(f"1. Add more time to {task_name_lower} ")
                print(f"2. Set a new deadline for task: '{task_name_lower}'")
                choice = input(">>>")
                clear()
            else:
                print("Invalid choice!")
                input()
                continue      
            
            if choice == "1":
                # Tìm deadline hiện tại của task để hiển thị cho user
                for task in updated_task:
                    if task['name'] == task_name_lower:
                        current_deadline = task['deadline']
                        break
                
                extra_days = int(input(f"Current deadline: {current_deadline}\nHow many days to add? "))

                # Cộng thêm số ngày vào deadline cũ bằng timedelta
                for task in updated_task:
                    if task['name'] == task_name_lower:
                        old = datetime.fromisoformat(task['deadline'])
                        task["deadline"] = str(old + timedelta(days=extra_days))
                        
                with open(TASK_FILE, 'w') as file: 
                    json.dump(updated_task, file, indent=4)  # Lưu lại file với indent=4 cho dễ đọc
                        
                print(f"Added {extra_days} day(s) to {task_name_lower} sucessfully! ")
                
            elif choice == "2":
                # Vòng lặp validate định dạng deadline nhập vào
                while True:
                    new_deadline = input(f"Enter new deadline (Ex: 14/01/2013-23:00): ")
                    try:
                        deadline_parsed = datetime.strptime(new_deadline, "%d/%m/%Y-%H:%M")  # Parse chuỗi → datetime object
                        break  # Nhập đúng format → thoát vòng lặp
                    except ValueError:
                        print("Wrong format!")
                
                try: 
                    # Tìm task theo tên và cập nhật deadline mới
                    for task in updated_task:
                        if task["name"] == task_name_lower:
                            task["deadline"] = str(deadline_parsed)
                    with open(TASK_FILE, 'w') as file: 
                        json.dump(updated_task, file, indent=4)
                    print(f"Task {task_name_lower} has been updated!")

                except FileNotFoundError:
                    print("File not found!")

            input()
            break

        # Nếu task chưa tồn tại → nhập deadline mới
        while True:
            print(f"Please enter deadline for '{task_name_lower}'. Ex: 14/01/2013-23:00".center(width))
            task_deadline = input(">>>")
            try:
                deadline = datetime.strptime(task_deadline, "%d/%m/%Y-%H:%M")  # Validate format
                break  # Nhập đúng → thoát
        
            except ValueError as e:
                print(f"Error found: {e}")

        print(f"Saved your task: {repr(task_deadline)}".center(width))
        save_task(task_name_lower, deadline)  # Lưu task mới vào file
        break


def is_duplicate(task_name_lower):
    # Kiểm tra xem task_name đã tồn tại trong file chưa
    # Trả về True nếu trùng, False nếu không
    try: 
        with open(TASK_FILE, 'r') as file:
            existing_task = json.load(file)
    except FileNotFoundError:
        return False  # File chưa có → chắc chắn không trùng
    except json.JSONDecodeError:
        return False  # File rỗng hoặc lỗi → không trùng
    
    for task in existing_task:
        if task['name'] == task_name_lower:
            return True  # Tìm thấy trùng → trả về True
    return False  # Loop xong không thấy → không trùng
    

def save_task(task_name_lower, deadline):
    # Đọc danh sách task cũ, thêm task mới vào, rồi ghi lại file
    try:
        with open(TASK_FILE, 'r') as file:
            updated_tasks = json.load(file)
    except FileNotFoundError:
        updated_tasks = []  # File chưa tồn tại → bắt đầu list mới
    except json.JSONDecodeError:
        updated_tasks = []  # File lỗi → bắt đầu list mới

    
    # Append task mới vào list với 3 field: name, deadline, done
    updated_tasks.append({
        "name": task_name_lower,
        "deadline": str(deadline),
        "done": False  # Task mới luôn chưa done
    })

    with open(TASK_FILE, 'w') as file:
        json.dump(updated_tasks, file, indent=4)


def list_file():
    clear()
    
    
    # Đọc toàn bộ task từ file
    try:
        with open(TASK_FILE, 'r') as file: 
            list_tasks = json.load(file)     
    except FileNotFoundError:
        list_tasks = []
    except json.JSONDecodeError:
        list_tasks = []

    keyword = input("Search (Enter to skip): ".center(width)).lower()

    if keyword != "":
        results = []                             # Tạo list rỗng chứa kết quả tìm kiếm
        for task in list_tasks:                  # Loop qua từng task
            if keyword in task["name"]:          # Nếu keyword có trong tên task
                results.append(task)             # Thêm task đó vào results
        list_tasks = results                     # Ghi đè list_tasks = chỉ còn task khớp keyword
    # Nếu keyword == "" (user bấm Enter) → bỏ qua filter, giữ nguyên list_tasks đầy đủ

    
    
    # In danh sách task với màu theo số ngày còn lại
    for task in list_tasks:
        name = task["name"]
        done = task["done"]  # True hoặc False
        deadline = datetime.fromisoformat(task["deadline"])  # Chuyển chuỗi → datetime object
        delta = deadline - datetime.now()  # Tính khoảng cách từ bây giờ đến deadline
        day_left = delta.days
        if day_left <= 0:
            print(Fore.WHITE + f'(PASSED) {name} → {day_left} day passed (Deadline: "{deadline}") \n ---- DONE?: {done}')
        elif day_left <= 3:
            print(Fore.RED + f'{name} → {day_left} left (Deadline: "{deadline}") \n ---- DONE?: {done}')   # Cấp bách!
        elif day_left <= 7:
            print(Fore.YELLOW + f'{name} → {day_left} left (Deadline: "{deadline}") \n ---- DONE?: {done}')  # Sắp tới
        else:
            print(Fore.GREEN + f'{name} → {day_left} left (Deadline: "{deadline}") \n ---- DONE?: {done}')   # Còn nhiều thời gian
    input()
    clear()
    

def mark_done():
    while True:
        try: 
            with open(TASK_FILE, "r") as file:
                list_tasks = json.load(file)
            
            # In danh sách task kèm số thứ tự để user chọn
            for i, task in enumerate(list_tasks): 
                print(f"{i+1}. {task['name']} - ({task['done']})")

            choice = int(input("Choose your task to mark it as done: "))
            list_tasks[choice - 1]["done"] = True  # Đổi field "done" thành True (-1 vì index bắt đầu từ 0)
            with open(TASK_FILE, 'w') as file:
                json.dump(list_tasks, file, indent=4)  # Ghi lại file với thay đổi
            
            clear()
            print(f"Marked!".center(width))
            input()
            break

        except FileNotFoundError:
            print("File not found!")
            break
        except ValueError:
            print("Please enter a number!")
            input()


def delete_task():
    while True:
        try:
            with open(TASK_FILE, 'r') as file:
                list_task = json.load(file)

            # In danh sách task kèm số thứ tự để user chọn
            for i, task in enumerate(list_task):
                print(f"{i+1}. {task['name']}")
            
            choice = int(input("Choose your task to Delete: "))
            if choice <= 0:
                print("Choice cannot be < 0  ".center(width))
                input()
                clear()
            else:
                list_task.pop(choice - 1)  # Xóa phần tử tại index đó khỏi list (-1 vì index từ 0)
            
                with open(TASK_FILE, "w") as file:
                    json.dump(list_task, file, indent=4)  # Ghi lại list sau khi đã xóa
                print("Deleted!")
                input()
                break

        except ValueError:
            print("Please enter a number!")
        except FileNotFoundError:
            print("File Not Found!")
            input()
            break
        except TypeError:
            print("No tasks to delete!")
            input()
            break
        except IndexError:
            print("Cannot delete task: Task does not exist!")
            input()
            clear()


def menu():
    



    while True:
        clear()
        print("")
        print("Please enter your choice!".center(width))
        print("1. Add tasks")
        print("2. To view tasks")
        print("3. Mark done")
        print("4. Delete a task")
        choice = input(">>>")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_file()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()


def banner():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    clear()
    # In logo chính bằng block Unicode (không dùng splitlines vì không cần rainbow ở đây)
    print(r"""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ 
          """
)
    print("~THE~".center(width))
    # Tách ASCII art thành từng dòng để loop và gán màu khác nhau cho mỗi dòng → hiệu ứng rainbow
    lines = r"""
 _____                 _ _ _                ______                                      
(____ \               | | (_)              |  ___ \                                     
 _   \ \ ____ ____  _ | | |_ ____   ____   | | _ | | ____ ____   ____  ____  ____  ____ 
| |   | / _  ) _  |/ || | | |  _ \ / _  )  | || || |/ _  |  _ \ / _  |/ _  |/ _  )/ ___)
| |__/ ( (/ ( ( | ( (_| | | | | | ( (/ /   | || || ( ( | | | | ( ( | ( ( | ( (/ /| |    
|_____/ \____)_||_|\____|_|_|_| |_|\____)  |_||_||_|\_||_|_| |_|\_||_|\_|| |\____)_|    
                                                                     (_____|            


                                                                                                                                   
""".splitlines()
    for i, line in enumerate(lines):
        print(colors[i % len(colors)] + line)  # i % len(colors) → lặp lại màu khi hết danh sách
    print("Press enter to continue...")

banner()  # Hiển thị banner trước khi vào menu
input()
menu()   # Vào vòng lặp chính của chương trình
    LOCKED = 0
    UNLOCKING = 1
    UNLOCKED = 2

state = LockState.LOCKED
state_lock = threading.Lock()

# ================= WINDOW CONTROL =================
def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd:
        ctypes.windll.user32.ShowWindow(whnd, 0)

def open_app_again(app_name):
    try:
        subprocess.Popen(app_name, shell=True)
    except:
        pass

# ================= PROCESS MONITOR =================
def get_target_process():
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name and name.lower() in TARGET_APPS:
                return proc
        except:
            pass
    return None


def kill_process(proc):
    try:
        proc.terminate()
    except:
        pass


# ================= AUTH UI =================
def show_lock_ui():
    global state

    def unlock_password():
        global state
        if entry.get() == PASSWORD:
            with state_lock:
                state = LockState.UNLOCKED
            root.destroy()
        else:
            error_label.config(text="Wrong password bro 💀")
            entry.delete(0, tk.END)

    def toggle():
        if entry.cget("show") == "":
            entry.config(show="*")
            toggle_btn.config(text="Show")
        else:
            entry.config(show="")
            toggle_btn.config(text="Hide")

    root = tk.Tk()
    root.title("App Locker 🔒")
    root.geometry("360x220")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    tk.Label(root, text="Locked App Detected", font=("Arial", 14, "bold")).pack(pady=10)

    entry = tk.Entry(root, show="*", font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus()

    toggle_btn = tk.Button(root, text="Show", command=toggle)
    toggle_btn.pack()

    tk.Button(root, text="Unlock", command=unlock_password).pack(pady=5)

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    root.bind("<Return>", lambda e: unlock_password())
    root.mainloop()


# ================= MONITOR LOOP =================
def monitor():
    global state

    while True:
        proc = get_target_process()

        with state_lock:
            current_state = state

        if proc and current_state != LockState.UNLOCKED:
            kill_process(proc)

            with state_lock:
                state = LockState.UNLOCKING

            show_lock_ui()

        elif not proc:
            with state_lock:
                state = LockState.LOCKED

        time.sleep(1)


# ================= START =================
hide_console()

threading.Thread(target=monitor, daemon=True).start()

while True:
    time.sleep(10)