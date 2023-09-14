import tkinter as tk
import socket

robot_ip = "192.168.163.128"
robot_port = 30001  

positions = {
    1: "movej([0.1, -1.2, 2.0, -3.0, 4.0, -1.5], a=1.0, v=1.0)",
    2: "movej([0.5, -0.5, 1.5, -2.0, 3.0, -1.0], a=1.0, v=1.0)",
    3: "movej([0.0, -1.0, 1.0, -1.0, 2.0, -1.0], a=1.0, v=1.0)",
    4: "movej([0.2, -1.5, 2.5, -2.5, 4.0, -1.8], a=1.0, v=1.0)",
}

def send_position(position_num):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((robot_ip, robot_port))
            command = positions.get(position_num)
            if command:
                s.sendall(command.encode())
                print(f"Sent command: {command}")
            else:
                print("Invalid position number.")
    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Robot Control")

for position_num in range(1, 5):
    button = tk.Button(
        root,
        text=f"Position {position_num}",
        command=lambda num=position_num: send_position(num),
    )
    button.pack(pady=10)

root.mainloop()
