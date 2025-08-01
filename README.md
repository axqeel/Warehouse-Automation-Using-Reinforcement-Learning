# 🤖 Warehouse Robot Coordination System

A full-stack Python project that simulates a warehouse robot coordination system using **Reinforcement Learning** and integrates with PostgreSQL database and a React-based frontend interface.

## 🧠 Core Features

### **Reinforcement Learning-Powered Robot Coordination**
- **Multi-Agent RL Environment**: Custom Gymnasium-compatible environment (`WarehouseEnv`) supporting multiple warehouse robots
- **PPO Algorithm**: Uses Stable Baselines3 PPO for training intelligent robot agents
- **Dynamic Task Execution**: Robots learn optimal paths for collection, deposit, and movement operations
- **Collision Avoidance**: Built-in collision detection and avoidance mechanisms
- **Task Prioritization**: Intelligent task queuing and prioritization system

### **Warehouse Operations**
1. **Collect**: AI agents navigate to target coordinates and collect items
2. **Deposit**: Robots move to specified locations and deposit products
3. **Move**: Agents pick up items from source and place at destination
4. **View**: Query product locations or check what's at specific coordinates

## 🏗️ Technology Stack

### **Backend (Python)**
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: ORM for database operations
- **PostgreSQL**: Primary database for storing warehouse state
- **Stable Baselines3**: Reinforcement learning library with PPO implementation
- **Gymnasium**: Custom environment for multi-agent warehouse simulation
- **NumPy**: Numerical computations for RL algorithms

### **Frontend (React)**
- **React**: Modern JavaScript library for building user interfaces
- **React Three Fiber**: 3D visualization library for warehouse grid
- **Three.js**: 3D graphics library for real-time rendering
- **Axios**: HTTP client for API communication
- **React Router**: Client-side routing

### **Database**
- **PostgreSQL**: Robust, open-source relational database
- **Alembic**: Database migration tool (optional)

## 🚀 Quick Start

### **Prerequisites**
- Python 3.9+ (recommended: 3.10)
- Node.js 18+
- PostgreSQL 13+
- Git

### **Installation**

#### 1. **Clone the Repository**
```bash
git clone <repository-url>
cd warehouse-automation
```

#### 2. **Set Up PostgreSQL**
```sql
-- Create database
CREATE DATABASE warehouse_db;

-- Create user (if needed)
CREATE USER postgres WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE warehouse_db TO postgres;
```

#### 3. **Backend Setup**
```bash
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create .env file with:
# DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/warehouse_db

# Run the backend
uvicorn app.main:app --reload
```

#### 4. **Frontend Setup**
```bash
cd frontend
npm install
npm start
```

#### 5. **Access the Application**
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🧠 Reinforcement Learning Architecture

### **Environment Design**
```python
class WarehouseEnv(gym.Env):
    def __init__(self, grid_size=(20, 20, 5), n_agents=3, n_shelves=5):
        # Multi-agent 3D grid environment
        # Supports dynamic routing and collision avoidance
```

### **Key RL Components**

#### **1. State Space**
- **Robot Positions**: Current (x, y, z) coordinates of all agents
- **Product Locations**: Positions of all warehouse items
- **Task Queue**: Pending operations and priorities
- **Grid State**: Occupancy map of warehouse space

#### **2. Action Space**
- **Movement Actions**: 6 discrete actions per agent (up, down, left, right, forward, backward)
- **Task Actions**: Pick, drop, collect, deposit operations
- **Multi-Agent Coordination**: Synchronized actions across all robots

#### **3. Reward Function**
- **Positive Rewards**: Successful task completion, efficient pathfinding
- **Negative Rewards**: Collisions, time penalties, inefficient routes
- **Sparse Rewards**: Long-term task completion bonuses

#### **4. Training Process**
```python
# PPO Training Configuration
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    verbose=1
)
model.learn(total_timesteps=100000)
```

### **Multi-Agent Coordination**
- **Decentralized Control**: Each robot operates independently
- **Shared Environment**: Agents interact through the same warehouse space
- **Task Distribution**: Intelligent assignment of tasks to available robots
- **Conflict Resolution**: Built-in mechanisms for handling simultaneous requests

## 📊 Database Schema

### **Core Tables**
```sql
-- Products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    x INTEGER,
    y INTEGER,
    z INTEGER,
    status VARCHAR(50) -- 'in_transit' or 'stored'
);

-- Robots table
CREATE TABLE robots (
    id SERIAL PRIMARY KEY,
    x INTEGER,
    y INTEGER,
    z INTEGER,
    status VARCHAR(50), -- 'idle' or 'active'
    current_task TEXT
);

-- Task history table
CREATE TABLE task_history (
    id SERIAL PRIMARY KEY,
    operation VARCHAR(100),
    product_id INTEGER REFERENCES products(id),
    robot_id INTEGER REFERENCES robots(id),
    timestamp TIMESTAMP DEFAULT NOW(),
    details TEXT
);
```

## 🌐 API Endpoints

### **Robot Operations**
- `POST /api/collect` - Collect item from target location
- `POST /api/deposit` - Deposit item at destination
- `POST /api/move` - Move item from source to destination
- `POST /api/view` - Query product or location information

### **System State**
- `GET /api/state` - Get current warehouse state (robots, products)
- `GET /api/tasks` - Get task history and queue

## 🎮 Frontend Interface

### **Command Panel**
- **Dynamic Forms**: Input fields adapt based on selected operation
- **Real-time Status**: Live updates on robot task execution
- **Error Handling**: Comprehensive error messages and validation
- **Settings**: Configurable grid dimensions and agent count

### **Live Grid View**
- **3D Visualization**: Real-time 3D warehouse representation
- **Robot Animation**: Animated robot movement and task execution
- **Product Markers**: Color-coded product and shelf indicators
- **Interactive Controls**: Zoom, pan, and rotation capabilities
- **Task Queue**: Side panel showing pending and completed tasks

## 🔧 Configuration

### **Environment Variables**
```bash
# Backend (.env)
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/warehouse_db
GRID_SIZE_X=20
GRID_SIZE_Y=20
GRID_SIZE_Z=5
NUM_AGENTS=3
NUM_SHELVES=5
```

### **RL Training Parameters**
```python
# Training configuration
TRAINING_STEPS = 100000
LEARNING_RATE = 3e-4
BATCH_SIZE = 64
GAMMA = 0.99
```

## 🚀 Advanced Features

### **Scalability**
- **Dynamic Agent Addition**: Support for adding/removing robots at runtime
- **Grid Size Configuration**: Adjustable warehouse dimensions
- **Task Queue Management**: Priority-based task scheduling
- **Performance Monitoring**: Real-time metrics and analytics

### **Future Enhancements**
- **Advanced RL Algorithms**: A3C, SAC, or custom algorithms
- **Multi-Objective Optimization**: Balance efficiency vs. energy consumption
- **Predictive Analytics**: ML-based demand forecasting
- **Real-time Optimization**: Dynamic route recalculation
- **Integration APIs**: Connect with real warehouse management systems

## 🐛 Troubleshooting

### **Common Issues**
1. **404 Errors**: Ensure backend is running and proxy is configured
2. **Database Connection**: Verify PostgreSQL is running and credentials are correct
3. **RL Training**: Check GPU availability for faster training
4. **3D Rendering**: Ensure WebGL is enabled in browser

### **Performance Optimization**
- **RL Training**: Use GPU acceleration for faster convergence
- **Database**: Index frequently queried columns
- **Frontend**: Implement virtual scrolling for large datasets
- **API**: Add caching for frequently accessed data

## 📚 Learning Resources

### **Reinforcement Learning**
- [Stable Baselines3 Documentation](https://stable-baselines3.readthedocs.io/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [PPO Algorithm Paper](https://arxiv.org/abs/1707.06347)

### **Technologies Used**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Stable Baselines3** team for the RL framework
- **FastAPI** creators for the modern web framework
- **React Three Fiber** community for 3D visualization tools
- **PostgreSQL** community for the robust database system

---

**Built with ❤️ using Reinforcement Learning for intelligent warehouse automation** 