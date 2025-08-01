
# 📦 Warehouse Automation Using Reinforcement Learning

A full-stack AI project simulating autonomous warehouse robots trained using reinforcement learning (PPO algorithm) to **collect**, **deposit**, and **move** items in a grid-based warehouse environment. This system includes a user-friendly frontend, PostgreSQL integration for real-time inventory and task tracking, and live animated visualization of robot actions.

---

## 🚀 Features

- ✅ **AI-Powered Agents** trained using Proximal Policy Optimization (PPO) from Stable Baselines3  
- 📦 **Task-based Simulation**: Collect, Deposit, Move, and View products in a 3D warehouse grid  
- 🧠 **Custom Gym Environment** (`WarehouseEnv`) with multi-agent support  
- 💻 **Minimalist Frontend Interface** with real-time task control and robot monitoring  
- 🎥 **Live Animation Tab** that visualizes robot paths and object movements  
- 🗃️ **PostgreSQL Integration** for storing product inventory, robot status, and task logs  
- 🔍 **Search by Product or Location** using the View panel

---

## 🖼️ Interface Overview

### **Command Panel Tab**
- Select from four actions: `Collect`, `Deposit`, `Move`, `View`
- Enter task-specific inputs (product ID, coordinates, etc.)
- Submit tasks and monitor active task queue and status

### **Live Grid View Tab**
- Displays animated 2D/3D map of the warehouse
- Color-coded agents and products
- Real-time updates with zoom/pan support


## 🧠 Technologies Used

- **Python 3.11+**
- **Stable Baselines3 (PPO)**  
- **Gymnasium**  
- **FastAPI / Flask**  
- **PostgreSQL + psycopg2**  
- **Jinja2 or React (frontend templating)**  
- **HTML5, CSS3, JS (canvas animations)**

---

## 🗃️ Database Schema (PostgreSQL)

- **products**: id, name, current_location (x, y, z), status  
- **robots**: id, current_position, is_active, current_task  
- **tasks**: id, type (collect/deposit/move), product_id, src/dest, timestamps  

---

## ⚙️ How to Run

1. Clone the repository  
2. Create a virtual environment and install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Set up PostgreSQL and run the schema:

\`\`\`bash
psql -U postgres -f sql/schema.sql
\`\`\`

4. Train the model:

\`\`\`bash
python train.py
\`\`\`

5. Run the backend server:

\`\`\`bash
uvicorn backend.app:app --reload
\`\`\`

6. Open browser and go to: `http://localhost:8000`

---

## 🎯 Future Improvements

- WebSocket integration for live updates
- Multi-agent reinforcement learning using PettingZoo
- GUI-based drag-and-drop task planner
- Inventory heatmaps and reporting dashboard

---

## 🙌 Contributing

Pull requests and feature suggestions are welcome! Feel free to fork and customize the project for different layouts, multi-floor systems, or use with real-world robots.
