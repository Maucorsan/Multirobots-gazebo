import tkinter as tk
from tkinter import messagebox
import yaml
import os
import subprocess

def save_params_to_yaml(params, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(params, file)

def run_sh_script():
    
    subprocess.run([f"./project.sh"])

def submit_initial():
    params = {
        'num_of_robots': int(num_robots_entry.get()),
        'ref_robot_id': int(ref_robot_id_entry.get()),
        'robot_model': robot_model_entry.get(),
        'distribution_type': distribution_type_var.get(),
        'distribution_params': {
            'center_x': float(center_x_entry.get()),
            'center_y': float(center_y_entry.get()),
        }
    }

    if distribution_type_var.get() == "circle":
        params['distribution_params']['radius'] = float(radius_entry.get())
    elif distribution_type_var.get() == "ARC":
        params['distribution_params']['width'] = float(width_entry.get())
        params['distribution_params']['height'] = float(height_entry.get())
    else:
        params['distribution_params']['separation'] = float(separation_entry.get())
        params['distribution_params']['angle'] = float(angle_entry.get())

    save_params_to_yaml(params, "/home/trinckets/catkin_ws/src/gazebo_multi_robot_spawn_ow/params.yaml")
    messagebox.showinfo("Info", "Initial parameters saved.")
    switch_to_final()

def submit_final():
    params = {
        'num_of_robots': int(num_robots_entry.get()),
        'ref_robot_id': int(ref_robot_id_entry.get()),
        'robot_model': robot_model_entry.get(),
        'distribution_type': distribution_type_var.get(),
        'distribution_params': {
            'center_x': float(center_x_entry.get()),
            'center_y': float(center_y_entry.get()),
        }
    }

    if distribution_type_var.get() == "circle":
        params['distribution_params']['radius'] = float(radius_entry.get())
    elif distribution_type_var.get() == "ARC":
        params['distribution_params']['width'] = float(width_entry.get())
        params['distribution_params']['height'] = float(height_entry.get())
    else:
        params['distribution_params']['separation'] = float(separation_entry.get())
        params['distribution_params']['angle'] = float(angle_entry.get())

    save_params_to_yaml(params, "/home/trinckets/catkin_ws/src/gazebo_multi_robot_spawn_ow/goal_params.yaml")
    messagebox.showinfo("Info", "Final parameters saved.")
    root.destroy()
    run_sh_script()

def switch_to_final():
    current_state.set('Final')
    submit_button.config(text="Save Final Parameters", command=submit_final)

def update_fields(*args):
    distribution_type = distribution_type_var.get()
    radius_label.grid_remove()
    radius_entry.grid_remove()
    width_label.grid_remove()
    width_entry.grid_remove()
    height_label.grid_remove()
    height_entry.grid_remove()
    separation_label.grid_remove()
    separation_entry.grid_remove()
    angle_label.grid_remove()
    angle_entry.grid_remove()

    if distribution_type == "circle":
        radius_label.grid(row=8, column=0, sticky='w', padx=5, pady=5)
        radius_entry.grid(row=8, column=1, sticky='ew', padx=5, pady=5)
    elif distribution_type == "ARC":
        width_label.grid(row=8, column=0, sticky='w', padx=5, pady=5)
        width_entry.grid(row=8, column=1, sticky='ew', padx=5, pady=5)
        height_label.grid(row=9, column=0, sticky='w', padx=5, pady=5)
        height_entry.grid(row=9, column=1, sticky='ew', padx=5, pady=5)
    else:
        separation_label.grid(row=8, column=0, sticky='w', padx=5, pady=5)
        separation_entry.grid(row=8, column=1, sticky='ew', padx=5, pady=5)
        angle_label.grid(row=9, column=0, sticky='w', padx=5, pady=5)
        angle_entry.grid(row=9, column=1, sticky='ew', padx=5, pady=5)

# Create the main window
root = tk.Tk()
root.title("ROS Launch Parameters")

# Define labels and entries
labels = [
    "Number of robots:",
    "Reference Robot ID:",
    "Robot Model:",
    "Distribution Type:",
    "Center X:",
    "Center Y:"
]

entries = []

for idx, label in enumerate(labels):
    lbl = tk.Label(root, text=label, width=20)
    lbl.grid(row=idx, column=0, sticky='w', padx=5, pady=5)
    if label == "Distribution Type:":
        distribution_type_var = tk.StringVar()
        distribution_type_var.trace("w", update_fields)
        distribution_type_menu = tk.OptionMenu(root, distribution_type_var, "circle", "line", "two_lines", "three_lines", "ARC")
        distribution_type_menu.grid(row=idx, column=1, sticky='ew', padx=5, pady=5)
        entries.append(distribution_type_var)
    else:
        entry = tk.Entry(root)
        entry.grid(row=idx, column=1, sticky='ew', padx=5, pady=5)
        entries.append(entry)

num_robots_entry, ref_robot_id_entry, robot_model_entry, distribution_type_var, center_x_entry, center_y_entry = entries

# Create specific field labels and entries
separation_label = tk.Label(root, text="Separation:", width=20)
separation_entry = tk.Entry(root)

angle_label = tk.Label(root, text="Angle:", width=20)
angle_entry = tk.Entry(root)

radius_label = tk.Label(root, text="Radius:", width=20)
radius_entry = tk.Entry(root)

width_label = tk.Label(root, text="Width:", width=20)
width_entry = tk.Entry(root)

height_label = tk.Label(root, text="Height:", width=20)
height_entry = tk.Entry(root)

# Set default values
num_robots_entry.insert(0, "0")
ref_robot_id_entry.insert(0, "2")
robot_model_entry.insert(0, " ")
#distribution_type_var.set("ARC")
center_x_entry.insert(0, "0")
center_y_entry.insert(0, "0")
separation_entry.insert(0, "1")
angle_entry.insert(0, "90")
radius_entry.insert(0, "2")
width_entry.insert(0, "4")
height_entry.insert(0, "2")

update_fields()

# Current state variable
current_state = tk.StringVar(value='Initial')

# Submit button
submit_button = tk.Button(root, text="Save Initial Parameters", command=submit_initial)
submit_button.grid(row=10, column=1, pady=10, sticky='ew')

# Run the application
root.mainloop()
